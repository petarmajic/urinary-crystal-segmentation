# Urinary crystal instance segmentation

I prepared a microscopy dataset for instance segmentation and fine-tuned YOLO11 models to locate and identify individual urinary crystals. The work covers filename-based metadata extraction, annotation preparation, class harmonisation and five-fold evaluation on an imbalanced dataset with mixed crystal species.

**Python · Ultralytics YOLO11 · NumPy · pandas · Pillow · Google Colab**

[Training notebook](notebooks/PRI_train.ipynb) · [Technical report](docs/reports/project-report.pdf) · [Recorded presentation · 2:17](docs/media/project-presentation.mp4)

## Project workflow

![Overview of source images, metadata extraction, expert polygons, two training variants and recorded outputs](assets/workflow.svg)

[Dataset and class distribution](docs/data.md) · [Experiment details](docs/experiments.md) · [Environment and execution notes](docs/reproducibility.md)

## What I worked on

| Area | Work in this project | Evidence |
| --- | --- | --- |
| **Data preprocessing** | Reviewed inconsistent filenames, species mixtures and image formats. Matched images to annotations and converted incompatible RGBA TIFFs to RGB in the working dataset. | [Data preparation](docs/data.md) |
| **Metadata extraction** | Built species and abbreviation mappings and a 659-row CSV, retaining original paths, mixture flags, pH fields and provenance notes. | [Python script](scripts/preprocessing/data_preprocessing_image_metadata.py) · [CSV](metadata/image_metadata.csv) |
| **Annotation preparation** | Worked with expert CVAT polygon annotations, merged five class aliases and filtered sparse classes before training. | [Class mapping and support](docs/data.md#annotations-and-class-mapping) |
| **Deep learning** | Fine-tuned pretrained YOLO11n-seg and YOLO11m-seg models at 1024 px, with a separate 15-class dataset and explicit augmentations for the latter. | [Notebook guide](notebooks/README.md) |
| **Evaluation** | Constructed multilabel-stratified folds and summarised mask precision, recall and mAP across five validation folds. | [Protocols and results](docs/experiments.md) |
| **Technical communication** | Documented the dataset issues and experiments in a report, poster, recorded presentation and defence slides. | [Project materials](docs/media-guide.md) |

## Example predictions

<p align="center">
  <a href="assets/validation-predictions.jpg"><img src="assets/validation-predictions.jpg" alt="Original collage of predicted crystal masks, class names and confidence scores" width="620"></a>
</p>

The [original prediction collage](docs/reports/project-report.pdf#page=23) shows instance masks, class labels and confidence scores across microscopy images. It appears in Figure 6.3 of the report and in the [project poster](docs/reports/project-poster.pdf). The source figure does not identify its exact model run. [Visual sources and interpretation](docs/media-guide.md#prediction-collage).

## Five-fold results

**YOLO11m-seg · 583 images · 15 classes · 1024 px**

| Mask precision | Mask recall | Mask mAP50 | Mask mAP50–95 |
| --- | --- | --- | --- |
| 0.7022 ± 0.0335 | 0.6306 ± 0.0513 | 0.6813 ± 0.0427 | **0.4874 ± 0.0453** |

Mean ± standard deviation across five folds, selecting the epoch with the highest validation mask mAP50–95 within each fold. These are validation results. The earlier 19-class experiment uses a different dataset and result-selection rule. [Full protocol, per-fold values and limitations](docs/experiments.md).

![Five recorded fold scores for YOLO11m-seg, with their mean and standard deviation](assets/fold-validation.svg)

## Presentation and poster

| Recorded project presentation · 2:17 | Original poster · 1 page |
| :---: | :---: |
| [<img src="assets/video-preview.jpg" alt="Recorded project presentation" height="220">](docs/media/project-presentation.mp4) | [<img src="assets/poster-preview.jpg" alt="Original project poster" height="220">](docs/reports/project-poster.pdf) |

[Defence slides · 20 slides](docs/presentations/project-defence.pptx) · [All materials and reading guide](docs/media-guide.md)

Research and Innovation Project (PRI), completed during my Erasmus exchange at **Polytech Tours, Université de Tours**, in collaboration with **CHU Orléans**. Medical engineers at the hospital provided the manual annotations. [Project context and contributions](docs/project.md).
