import os
import re
import csv
import json

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# Loading species and abbreviation data
species_data = load_json('species_mapping.json')
abbreviation_data = load_json('abbreviation_mapping.json')

# dictionary for species
species_lookup = {}
for item in species_data:
    for variant in item['variants']:
        species_lookup[variant.lower()] = (item['code'], item['canonical'])

# dictionary for abbreviations
abbreviation_lookup = {}
for item in abbreviation_data:
    for variant in item['variants']:
        abbreviation_lookup[variant.lower()] = (item['code'], item['explanation'])


def find_species(text):
    found = set()
    text_normalized = text.lower()
    text_normalized = re.sub(r'[+\(\)\[\]_\-/]', ' ', text_normalized)
    
    for variant in species_lookup:
        pattern = r'(?:^|[^a-z0-9])' + re.escape(variant) + r'(?:[^a-z0-9]|$)'
        if re.search(pattern, text_normalized):
            found.add(species_lookup[variant][0])
    
    return sorted(found)


def find_abbreviations(text):
    found = []
    text_no_ext = os.path.splitext(text)[0].lower()
    sorted_variants = sorted(abbreviation_lookup.keys(), key=len, reverse=True)
    temp = text_no_ext
    
    for variant in sorted_variants:
        pattern = r'(?:^|[^a-z0-9])' + re.escape(variant) + r'(?:[^a-z0-9]|$)'
        matches = list(re.finditer(pattern, temp))
        if matches:
            found.append(abbreviation_lookup[variant][0])
            for match in matches:
                start, end = match.span()
                temp = temp[:start] + ' ' * (end - start) + temp[end:]
    
    return sorted(set(found))

def extract_ph(text):
    """Extract pH value from filename."""
    # Match patterns!!
    # pH85, pH8.5, pH_85, ph85, pH 85
    match = re.search(r'ph\s*[_\-]?\s*(\d{1,2})\.?(\d*)', text, re.IGNORECASE)
    if match:
        ph_value = match.group(1)
        # Convert to standard format (85 -> 8.5, 62 -> 6.2)
        if '.' not in ph_value and len(ph_value) == 2:
            return f"{ph_value[0]}.{ph_value[1]}"
        return ph_value
    return ''



# Filename is registration number??
def is_registration_number(filename):
    name = os.path.splitext(filename)[0]
    return bool(re.match(r'^P[A-Z]?[A-Z]?[0-9]+', name, re.IGNORECASE))


def process_images(data_folder, project_root):
    """Process all images and extract metadata."""
    results = []
    
    for folder_path, _, filenames in os.walk(data_folder):
        folder_name = os.path.basename(folder_path)
        folder_species = find_species(folder_name)
        
        for filename in filenames:
            if not re.search(r'\.(jpg|jpeg|png|bmp|tif|tiff)$', filename, re.IGNORECASE):
                continue
            
            full_path = os.path.join(folder_path, filename)
            rel_path = os.path.relpath(full_path, project_root)
            
            file_species = find_species(filename)
            notes = []
            
            if file_species:
                species = file_species
            elif is_registration_number(filename):
                species = folder_species
                if species:
                    notes.append('species from directory (registration number)')
            else:
                species = folder_species
                if species:
                    notes.append('species from directory')
            
            if not species:
                notes.append('species not found')
            
            # format species with descriptions
            species_text = ', '.join([
                f"{s} ({species_lookup[s.lower()][1]})"
                for s in species if s.lower() in species_lookup
            ])

            # format abbreviations with explanations
            abbr_codes = find_abbreviations(filename)
            abbr_text = ', '.join([
                f"{code} ({abbreviation_lookup[code.lower()][1]})"
                for code in abbr_codes if code.lower() in abbreviation_lookup
            ])
            
            ph_value = extract_ph(filename)
            
            results.append({
                'filename': filename,
                'rel_path': rel_path,
                'species': species_text,
                'mixture': 'Yes' if len(species) > 1 else 'No',
                'abbreviations': abbr_text,
                'ph': ph_value,
                'notes': '; '.join(notes)
            })
    
    return results


def save_csv(data, filename):
    columns = ['filename', 'rel_path', 'species', 'mixture', 'abbreviations', 'ph', 'notes']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    project_root = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(project_root, 'RawData/SÇlection cristaux Hennet')
    
    print("Processing images...")
    results = process_images(data_folder, project_root)
    
    print(f"Found {len(results)} images")
    print("Saving to CSV...")
    
    save_csv(results, 'image_metadata.csv')
    
    print("Done!")