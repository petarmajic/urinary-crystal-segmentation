# Urinary crystal instance segmentation

**Instance segmentation of urinary crystals in microscopy images**, where several species can appear in the same field of view. I prepared the images and expert polygon labels, harmonised the class vocabulary, and fine-tuned pretrained YOLO11 segmentation models with five-fold validation.

**Python · Ultralytics YOLO11 · NumPy · pandas · Pillow · multilabel stratification**

[Training notebook](notebooks/PRI_train.ipynb) · [Technical report](docs/reports/project-report.pdf)

## Method and architecture

![Research diagram showing annotation preparation, the 583-image dataset, five-fold validation and the multiscale YOLO11m-seg mask-prediction architecture.](assets/workflow.svg)

**Figure 1.** Data preparation, five-fold validation and the Ultralytics YOLO11m-seg architecture. Tensor volumes and fold cells are schematic. [Architecture details](docs/architecture.md).

## Segmentation targets

**15 classes · 583 images · 7,371 annotated instances.** An image can contain several classes and multiple instances of each class.

| IDs 0–4 | IDs 5–9 | IDs 10–14 |
| --- | --- | --- |
| **AMO** · Amoxicillin trihydrate | **C3** · Caoxite | **NASM** · N-acetylsulfamethoxazole hydrochloride |
| **AU2** · Uric acid dihydrate | **CAL** · Calcite | **PACC** · Plaque vitreuse¹ |
| **Br** · Brushite | **CYS** · Cystine | **PAM** · Struvite |
| **C1** · Whewellite | **DHAd** · Dihydroxyadenine | **UrAm** · Anhydrous ammonium urate |
| **C2** · Weddellite | **NASD** · N&#8209;acetylsulfadiazine | **VAT** · Vaterite |

¹ Original training label. [Class IDs and support counts](docs/data.md#segmentation-classes).

![One original microscopy field and its seven expert polygon annotations for C2 weddellite.](assets/annotation-example.svg)

**Figure 2.** Seven **C2 (weddellite)** instances with expert polygon annotations. [Data details](docs/data.md#annotation-example) · [Model predictions](docs/media-guide.md#prediction-collage).

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

**Figure 3.** Mean ± sample SD across five folds, selecting each fold's best validation mask mAP50–95 epoch. [Experiment details](docs/experiments.md).

## Repository guide

| Location | Contents |
| --- | --- |
| [notebooks/](notebooks/) | Training code and saved outputs. |
| [scripts/](scripts/) | Preprocessing and training helpers. |
| [data/](data/) | Microscopy images and polygon labels. |
| [metadata/](metadata/) | Image metadata and class mappings. |
| [results/](results/) | Fold metrics and model summary. |
| [docs/](docs/) | Methodology, experiments and reports. |

## Poster and presentation

| Recorded presentation · 2:17 | Project poster |
| :---: | :---: |
| [<img src="assets/video-preview.jpg" alt="Recorded project presentation" height="200">](docs/media/project-presentation.mp4) | [<img src="assets/poster-preview.jpg" alt="Project poster" height="200">](docs/reports/project-poster.pdf) |

[Defence slides](docs/presentations/project-defence.pptx)

*Completed for the Research and Innovation Project (PRI) during my Erasmus exchange at Polytech Tours, Université de Tours. Expert annotations provided by CHU Orléans medical engineers.*
