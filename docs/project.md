# Project context and contributions

## Problem

Microscopy images can contain several urinary crystal species and multiple objects of each species. Folder names and filenames provide useful clues, but do not describe every object. This project uses instance segmentation to locate crystals and assign a class to each instance.

## Academic context

The work was completed for the **Research and Innovation Project (PRI)** at **Polytech Tours, Université de Tours**, during my Erasmus exchange. It involved **CHU Orléans** and was supervised by **Gilles Venturini** and **Barthélémy Serres**.

The report, *Detection of crystals in medical images — Research and Innovation Project*, is dated February 2026; the poster identifies the academic year 2025–2026.

## My contribution

I reviewed the image collection, extracted structured metadata, prepared image–polygon pairs, harmonised and filtered classes, fine-tuned YOLO segmentation models, and analysed five-fold validation results. The report, poster and recorded presentation explain the methodology and findings.

CHU Orléans medical engineers produced the manual CVAT polygon annotations used for training and validation. The collaboration's coding guide and dataset notes supplied the domain terminology.

| Work | Evidence |
| --- | --- |
| Dataset review and metadata | [Extraction script](../scripts/preprocessing/data_preprocessing_image_metadata.py), [CSV and mappings](../metadata/README.md) |
| Annotation processing and folds | [Notebook](../notebooks/PRI_train.ipynb), cells 6–16 and 29–36 |
| Model training and evaluation | Notebook cells 24, 26–27 and 37–38; [experiment results](experiments.md) |
| Technical communication | [Report](reports/project-report.pdf), [poster and presentation](media-guide.md) |

The results describe a research experiment on the supplied dataset. Clinical reliability and hospital deployment were not evaluated.
