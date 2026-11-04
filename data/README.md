# Image data and annotation export

| Location | Contents |
| --- | --- |
| [Original image collection](raw/) | Original microscopy collection, retaining species folders and original image names |
| [CVAT annotation export](annotated/) | CVAT/Ultralytics export, retaining its internal images/labels hierarchy, YAML and split files |

The collection is in `raw/`, and the annotation export is in `annotated/`. The export YAML uses `path: .`, relative to the dataset directory.

## Existing split files

| File | Entries | Interpretation |
| --- | --- | --- |
| [train.txt](annotated/train.txt) | 659 | Source export image list |
| [train_split.txt](annotated/train_split.txt) | 490 | Earlier random training subset |
| [val_split.txt](annotated/val_split.txt) | 123 | Earlier random validation subset |
| [test_split.txt](annotated/test_split.txt) | 46 | Unannotated images, despite the historical filename |

These are **not** the five-fold lists generated later in Colab. The cleaned `dataset_clean` and `dataset_clean_drop4` directories, their fold YAML files, run CSVs and trained checkpoints are not included as standalone artifacts. Their creation and saved training outputs appear in the [original notebook](../notebooks/PRI_train.ipynb).

## Path audit

The current export contains **659 image files and 612 nonempty polygon-label files**, with no repeated exact image stems. Every entry in `train.txt` resolves against the source tree. The early split lists have Unicode normalisation differences in accented names: **130 training paths, 36 validation paths and 7 unannotated paths** differ byte-for-byte from the tree. All resolve after NFC normalisation. The split files retain their original encoding.

After NFC normalisation, the early train and validation lists have no overlapping paths or exact image blob hashes. This check covers exact-byte duplicates in that early split only. It does not establish specimen independence, rule out related crops, or validate the later notebook folds.

The dataset was supplied through the hospital collaboration. A general redistribution licence is not included.
