# Project context and contributions

## Problem

Microscopy images can contain several urinary crystal species and multiple objects of each species. Folder names and filenames help identify the contents of an image, but they do not label each crystal. This project uses instance segmentation to locate crystals and assign a class to each instance.

## Academic context

The work was completed for the **Research and Innovation Project (PRI)** at **Polytech Tours, Université de Tours**, during my Erasmus exchange. It involved **CHU Orléans** and was supervised by **Gilles Venturini** and **Barthélémy Serres**.

The report, *Detection of crystals in medical images — Research and Innovation Project*, is dated February 2026; the poster identifies the academic year 2025–2026.

## My contribution

I reviewed the images, extracted filename metadata and matched images to their polygon annotations. I then merged different labels for the same species, removed classes with too few examples and prepared the training sets. I fine-tuned the YOLO segmentation models and analysed the results across five validation folds. The report, poster and recorded presentation describe the methods and results.

CHU Orléans medical engineers produced the manual CVAT polygon annotations used for training and validation. Their coding guide and dataset notes explain the species names and filename abbreviations.

| Work | Code and materials |
| --- | --- |
| Dataset review and metadata | [Extraction script](../scripts/preprocessing/data_preprocessing_image_metadata.py), [CSV and mappings](../metadata/README.md) |
| Annotation processing and folds | [Notebook](../notebooks/PRI_train.ipynb), cells 6–16 and 29–36 |
| Model training and evaluation | Notebook cells 24, 26–27 and 37–38; [experiment results](experiments.md) |
| Technical communication | [Report](reports/project-report.pdf), [poster and presentation](media-guide.md) |

The results describe a research experiment on the supplied dataset. Clinical reliability and hospital deployment were not evaluated.
