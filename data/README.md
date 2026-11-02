# Image data and annotation export

| Location | Contents |
| --- | --- |
| [Original image collection](raw/) | Original microscopy collection, retaining species folders and original image names |
| [CVAT annotation export](annotated/) | CVAT/Ultralytics export, retaining its internal images/labels hierarchy, YAML and split files |

The original collection is in `raw/`, and the CVAT export is in `annotated/`. File contents and the internal directory hierarchy of each collection are unchanged. The [migration map](../docs/archive/migration-map.csv) records original paths, current locations and Git blob identities. `data.yaml` uses `path: .`; resolve that against the dataset directory when configuring a future run.

## Existing split files

| File | Entries | Interpretation |
| --- | --- | --- |
| [train.txt](annotated/train.txt) | 659 | Source export image list |
| [train_split.txt](annotated/train_split.txt) | 490 | Earlier random training subset |
| [val_split.txt](annotated/val_split.txt) | 123 | Earlier random validation subset |
| [test_split.txt](annotated/test_split.txt) | 46 | Unannotated images, despite the historical filename |

These are **not** the five-fold lists generated later in Colab. The cleaned `dataset_clean` and `dataset_clean_drop4` directories, their fold YAML files, run CSVs and trained checkpoints are not included as standalone artifacts. Their creation and saved training outputs appear in the [original notebook](../notebooks/PRI_train.ipynb).

## Path audit

The current export contains **659 image files and 612 nonempty polygon-label files**, with no repeated exact image stems. Every entry in `train.txt` resolves against the source tree. The early split lists have Unicode normalisation differences in accented names: **130 training paths, 36 validation paths and 7 unannotated paths** differ byte-for-byte from the tree. All resolve after NFC normalisation. The original list contents are retained, so these differences need handling in a runnable copy on filesystems that distinguish the two Unicode forms.

After NFC normalisation, the early train and validation lists have no overlapping paths or exact image blob hashes. This check covers exact-byte duplicates in that early split only. It does not establish specimen independence, rule out related crops, or validate the later notebook folds.

The dataset originates from a hospital collaboration. No general redistribution licence is supplied here. Confirm permission and any attribution requirements with the data providers before distributing the images or model artifacts outside the authorised project context.
