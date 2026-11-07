# Metadata and code mappings

I used the hospital’s species codes and abbreviations to index the image collection. This made it possible to find likely mixtures and lighting conditions while reviewing the images. The expert polygons supplied the training labels.

| File | Role |
| --- | --- |
| [image_metadata.csv](image_metadata.csv) | 659 image records produced during the dataset review |
| [species_mapping.json](species_mapping.json) | Species codes, names and recognised spelling variants |
| [abbreviation_mapping.json](abbreviation_mapping.json) | Abbreviation codes, explanations and variants used by the parser |
| [abbreviation_mapping.csv](abbreviation_mapping.csv) | Tabular abbreviation reference |
| [derived/drop4-class-support.csv](derived/drop4-class-support.csv) | Image and instance counts from the 15-class experiment in notebook cell 35 |

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

When the parser finds no species in the filename, it tries the folder name and records that fallback in `notes`. The [French coding guide](../docs/domain-notes/crystal-coding-guide-fr.docx) explains the original terminology.

`rel_path` retains the old `RawData/SÇlection cristaux Hennet` prefix. The corresponding source collection is now in [`data/raw/`](../data/raw/). The pH parser can store `pH8.5` as `8`, so check the original filename before reusing decimal pH values. [Execution notes](../docs/reproducibility.md#known-issues).
