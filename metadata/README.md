# Metadata and code mappings

| File | Role |
| --- | --- |
| [image_metadata.csv](image_metadata.csv) | 659 image records produced during the dataset review |
| [species_mapping.json](species_mapping.json) | Species codes, canonical names and recognised text variants |
| [abbreviation_mapping.json](abbreviation_mapping.json) | Abbreviation codes, explanations and variants used by the parser |
| [abbreviation_mapping.csv](abbreviation_mapping.csv) | Tabular abbreviation reference |
| [derived/drop4-class-support.csv](derived/drop4-class-support.csv) | Class support transcribed programmatically from saved notebook cell 35; 15-class experiment |

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

There are **581 rows marked `No` and 78 marked `Yes`** in the mixture field. Only **65 rows** contain a pH value. These are outputs of filename parsing, not a separate expert annotation of every field. In particular, `No` does not prove that an image contains a single species.

The script preserves useful clues from inconsistent source names, including tokens for polarised light and mixtures. It also records folder-based fallbacks. The [French coding guide](../docs/domain-notes/crystal-coding-guide-fr.docx) explains the original terminology.

`rel_path` retains the old `RawData/SÇlection cristaux Hennet` prefix. The corresponding source collection is now in [`data/raw/`](../data/raw/). Do not treat the stored path as a current executable path. Decimal pH parsing has a known implementation issue; see [execution notes](../docs/reproducibility.md#known-issues).
