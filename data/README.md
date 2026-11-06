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

These lists describe the earlier random split. The notebook later creates five folds for `dataset_clean` and `dataset_clean_drop4`. The generated datasets, fold YAML files, run CSVs and trained checkpoints are not included as separate files, but the preparation code and training outputs are in the [notebook](../notebooks/PRI_train.ipynb).

## Image and label paths

The current export contains **659 image files and 612 nonempty polygon-label files**, with no repeated exact image stems. Every entry in `train.txt` resolves against the source tree. The early split lists have Unicode normalisation differences in accented names: **130 training paths, 36 validation paths and 7 unannotated paths** use a different Unicode representation from the source filenames. All resolve after NFC normalisation. The split files retain their original encoding.

After NFC normalisation, the early train and validation lists have no overlapping paths or identical image files. This check applies to those two lists. Different crops or lighting views of the same specimen can still be related, and the later notebook folds use their own split.

The dataset was supplied through the hospital collaboration. A general redistribution licence is not included.
