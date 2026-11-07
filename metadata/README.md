# Metadata and code mappings

I used the hospital’s species codes and abbreviations to index the image collection. This made it possible to find likely mixtures and lighting conditions while reviewing the images. The expert polygons supplied the training labels.

| File | Role |
| --- | --- |
| [image_metadata.csv](image_metadata.csv) | 659 image records produced during the dataset review |
| [species_mapping.json](species_mapping.json) | Species codes, names and recognised spelling variants |
| [abbreviation_mapping.json](abbreviation_mapping.json) | Abbreviation codes, explanations and variants used by the parser |
| [abbreviation_mapping.csv](abbreviation_mapping.csv) | Tabular abbreviation reference |
| [derived/drop4-class-support.csv](derived/drop4-class-support.csv) | Image and instance counts from the 15-class experiment in notebook cell 35 |

## Examples from the report

I matched spelling variants against the species and abbreviation dictionaries. For example, `C1`, `whewellite` and `oxalate de calcium monohydraté` all map to C1. I looked in the filename first. If that gave no species, I checked the folder and recorded how I inferred the value.

| Filename | Folder | Extracted fields (abbreviated) |
| --- | --- | --- |
| `C1 (+C2)_intoxication Ethylene_glycol (EG)_3.tif` | `whewellite` | Species C1 and C2, mixture Yes, abbreviation EG |
| `P9130977.JPG` | `whewellite` | Species C1, mixture No, note `species from directory (registration number)` |
| `calcite_pH85_C8097.jpg` | `calcite` | Species CAL, pH 8.5 |
| `Calcite_pol_x200.jpg` | `calcite` | Species CAL, abbreviation `pol` for polarised light |
| `P5092126.JPG` | `artefact` | Species field empty, note `species not found` |

The filenames and paths in the [CSV](image_metadata.csv) are the original strings. I standardised the values in the other columns so the same species could be counted under one code. [Technical report, sections 3.4–3.5 and 4.1](../docs/reports/project-report.pdf).

## CSV fields

| Column | Meaning |
| --- | --- |
| `filename` | Original image name |
| `rel_path` | Historical path recorded during metadata extraction |
| `species` | Species inferred from recognised filename tokens, falling back to the folder name |
| `mixture` | `Yes` when the parser finds more than one species code |
| `abbreviations` | Recognised tokens describing acquisition, morphology or context |
| `ph` | Value extracted from a pH pattern when available |
| `notes` | How a species value was inferred, or that none was found |

Across 659 records, the mixture field contains **581 `No` values and 78 `Yes` values**. A `No` means it found fewer than two species codes. The image itself can still contain multiple species. Only **65 rows** have a pH value.

The `notes` column shows where the folder mattered. I counted 207 rows where the parser took the species from the directory, including 130 registration-number filenames. In another 89 rows it found no recognised species and left the field empty. The [French coding guide](../docs/domain-notes/crystal-coding-guide-fr.docx) explains the original terminology.

`rel_path` retains the old `RawData/SÇlection cristaux Hennet` prefix. The corresponding source collection is now in [`data/raw/`](../data/raw/). The pH parser can store `pH8.5` as `8`, so check the original filename before reusing decimal pH values. [Execution notes](../docs/reproducibility.md#known-issues).
