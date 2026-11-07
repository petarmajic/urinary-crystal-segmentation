# Project context and contributions

## Problem

Microscopy images can contain several urinary crystal species and multiple objects of each species. A filename can identify a species without telling us which pixels belong to it. I used instance segmentation so that two touching crystals could each have a class and a mask.

## Academic context

I completed the work for the **Research and Innovation Project (PRI)** at **Polytech Tours, Université de Tours**, during my Erasmus exchange. I worked with **CHU Orléans** under the supervision of **Gilles Venturini** and **Barthélémy Serres**.

The report, *Detection of crystals in medical images — Research and Innovation Project*, is dated February 2026. The poster lists the academic year as 2025–2026.

## My contribution

I matched the images to their polygon files and checked how often each species appeared. Some species had two labels in the export, so I merged those aliases before filtering rare classes. I fine-tuned two pretrained YOLO11 segmentation models and analysed their mask metrics across five validation folds.

CHU Orléans medical engineers produced the manual CVAT polygon annotations used for training and validation. Their coding guide and dataset notes explain the species names and filename abbreviations.

| Work | Code and materials |
| --- | --- |
| Dataset review and metadata | [Extraction script](../scripts/preprocessing/data_preprocessing_image_metadata.py), [CSV and mappings](../metadata/README.md) |
| Annotation processing and folds | [Notebook](../notebooks/PRI_train.ipynb), cells 6–16 and 29–36 |
| Model training and evaluation | Notebook cells 24, 26–27 and 37–38; [experiment results](experiments.md) |
| Technical communication | [Report](reports/project-report.pdf), [poster and presentation](media-guide.md) |

I evaluated the models on image-level folds from the supplied collection. The project did not include a clinical evaluation or hospital deployment.
