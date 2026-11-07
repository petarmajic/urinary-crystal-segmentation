# Image data and annotation export

I worked from two copies of the collection. The raw directory retains the hospital’s filenames. The CVAT export pairs microscopy images with polygon label files for training.

| Location | Contents |
| --- | --- |
| [Original image collection](raw/) | Original microscopy collection, retaining species folders and original image names |
| [CVAT annotation export](annotated/) | CVAT/Ultralytics export, retaining its internal images/labels hierarchy, YAML and split files |

The export YAML uses `path: .`, relative to the dataset directory.

## Existing split files

| File | Entries | Interpretation |
| --- | --- | --- |
| [train.txt](annotated/train.txt) | 659 | Source export image list |
| [train_split.txt](annotated/train_split.txt) | 490 | Earlier random training subset |
| [val_split.txt](annotated/val_split.txt) | 123 | Earlier random validation subset |
| [test_split.txt](annotated/test_split.txt) | 46 | Unannotated images, despite the historical filename |

I used the random split early in the project. For the two recorded experiments I generated five folds for `dataset_clean` and `dataset_clean_drop4`. The [notebook](../notebooks/PRI_train.ipynb) contains the preparation code and saved training outputs. To rerun training you need to recreate the clean datasets and fold YAML files. Per-epoch run CSVs and trained checkpoints are absent from this repository.

## Image and label paths

The current export contains **659 image files and 612 nonempty polygon-label files**, with no repeated exact image stems. Every entry in `train.txt` resolves against the source tree. The early split lists have Unicode normalisation differences in accented names: **130 training paths, 36 validation paths and 7 unannotated paths** use a different Unicode representation from the source filenames. All resolve after NFC normalisation. When looking up a file from these lists, compare the list entry and the filename after Unicode NFC normalisation.

After NFC normalisation, the early train and validation lists have no overlapping paths or identical image files. This check applies to those two lists. Different crops or lighting views of the same specimen can still be related, and the later notebook folds use their own split.

The dataset was supplied through the hospital collaboration. The repository includes no general redistribution licence for these images.
