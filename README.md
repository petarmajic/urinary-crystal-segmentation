# Urinary crystal instance segmentation

**Instance segmentation of urinary crystals in microscopy images**, where several species can appear in the same field of view. I prepared the images and expert polygon labels, harmonised the class vocabulary, and fine-tuned pretrained YOLO11 segmentation models with five-fold validation.

**Python · Ultralytics YOLO11 · NumPy · pandas · Pillow · multilabel stratification**

[Training notebook](notebooks/PRI_train.ipynb) · [Architecture](docs/architecture.md) · [Data](docs/data.md) · [Technical report](docs/reports/project-report.pdf)

## Method and architecture

![Research diagram showing annotation preparation, the 583-image dataset, five-fold validation and the multiscale YOLO11m-seg mask-prediction architecture.](assets/workflow.svg)

**Figure 1.** The main **15-class YOLO11m-seg experiment**: prepared image–polygon pairs, multilabel-stratified folds, multiscale features and instance-mask prediction. The model architecture is provided by Ultralytics; tensor volumes and fold cells are schematic. Filename metadata supports the dataset audit and is not a model input.

[Model structure, tensor dimensions and mask reconstruction →](docs/architecture.md)

## Segmentation targets

The main experiment retains **15 labels across 583 images**, with **7,371 annotated instances** in the saved counts. Each image can contain several classes and several objects of the same class.

| IDs 0–4 | IDs 5–9 | IDs 10–14 |
| --- | --- | --- |
| **AMO** · Amoxicillin trihydrate | **C3** · Caoxite | **NASM** · N-acetylsulfamethoxazole hydrochloride |
| **AU2** · Uric acid dihydrate | **CAL** · Calcite | **PACC** · Plaque vitreuse¹ |
| **Br** · Brushite | **CYS** · Cystine | **PAM** · Struvite |
| **C1** · Whewellite | **DHAd** · Dihydroxyadenine | **UrAm** · Anhydrous ammonium urate |
| **C2** · Weddellite | **NASD** · N-acetylsulfadiazine | **VAT** · Vaterite |

¹ Original training-label wording retained. [Exact class names, remapped IDs and support counts](docs/data.md#segmentation-classes).

![One original microscopy field and its seven expert polygon annotations for C2 weddellite.](assets/annotation-example.svg)

**Figure 2.** Seven expert-annotated **C2 (weddellite)** instances in one microscopy field. The contours come directly from the source polygon labels. [Annotation source](docs/data.md#annotation-example) · [Recorded model predictions](docs/media-guide.md#prediction-collage).

## What I worked on

- **Data preparation:** matched image/label files, handled incompatible TIFFs and extracted a 659-row metadata table from filenames and domain mappings. [Script](scripts/preprocessing/data_preprocessing_image_metadata.py) · [CSV](metadata/image_metadata.csv)
- **Annotation processing:** merged five aliases, filtered sparse classes and remapped the retained polygon labels. [Preparation stages](docs/data.md#annotations-and-class-mapping)
- **Model training:** fine-tuned YOLO11n-seg and YOLO11m-seg at 1024 px using distinct prepared datasets and training configurations. [Notebook guide](notebooks/README.md)
- **Evaluation:** generated multilabel-stratified folds and analysed mask precision, recall and mAP across five validation folds. [Protocol](docs/experiments.md)

## Five-fold validation

**YOLO11m-seg · 583 images · 15 classes · input 1024 px · batch 4**

| Mask precision | Mask recall | Mask mAP50 | Mask mAP50–95 |
| --- | --- | --- | --- |
| 0.7022 ± 0.0335 | 0.6306 ± 0.0513 | 0.6813 ± 0.0427 | **0.4874 ± 0.0453** |

![Five recorded fold mask mAP50–95 values with their mean and one sample standard deviation.](assets/fold-validation.svg)

**Figure 3.** Mean ± sample standard deviation across five folds, selecting each fold's highest validation mask mAP50–95 epoch. These are validation results. The earlier 19-class run has a different dataset and result-selection rule. [Selected epochs, per-fold values and interpretation →](docs/experiments.md)

## Code and project materials

| Resource | Contents |
| --- | --- |
| [Notebook](notebooks/PRI_train.ipynb) · [Preprocessing scripts](scripts/preprocessing/) | Image/label preparation, metadata, class processing, training and saved outputs. |
| [Data](docs/data.md) · [Architecture](docs/architecture.md) | Dataset stages, the 15 retained labels, feature scales and the mask head. |
| [Experiments](docs/experiments.md) · [Execution notes](docs/reproducibility.md) | Run settings, fold metrics, historical paths and preparation for a new run. |
| [Report](docs/reports/project-report.pdf) · [Poster](docs/reports/project-poster.pdf) | Original methodology, discussion and visual evidence. |
| [Recorded presentation · 2:17](docs/media/project-presentation.mp4) · [Defence slides](docs/presentations/project-defence.pptx) | Project explanation and original presentation materials. |

[All materials and source guide](docs/media-guide.md) · [Figure sources and regeneration](assets/README.md)

*Research and Innovation Project (PRI), completed during my Erasmus exchange at Polytech Tours, Université de Tours. CHU Orléans medical engineers provided the manual annotations. [Project context](docs/project.md).*
