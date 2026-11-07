# Report and presentation materials

The report contains the full method and experiments. The poster and its 2:17 recorded presentation give a shorter introduction to the microscopy problem.

| Material | Format | Contents |
| --- | --- | --- |
| [Technical report](reports/project-report.pdf) | 24 pages | Data review, annotation preparation, training and evaluation |
| [Poster](reports/project-poster.pdf) | 1 page | Project summary, microscopy examples and predicted instances |
| [Recorded presentation](media/project-presentation.mp4) | 2:17 | Recorded explanation of the poster |
| [Project defence](presentations/project-defence.pptx) | 20 slides | Metadata, CVAT annotations, folds and model experiments |
| [Training workflow](presentations/training-workflow.pptx) | 8 slides | Earlier planning and background references |
| [Training and validation](presentations/train-and-validation.pptx) | 7 slides | Earlier split and validation planning |

## Prediction collage

[![Original validation collage from report Figure 6.3](../assets/validation-predictions.jpg)](../assets/validation-predictions.jpg)

**Figure 1.** Predicted crystal masks, class labels and confidence scores across microscopy fields (report Figure 6.3, PDF page 23).

The report does not identify the model, fold or checkpoint, so it cannot be linked to a specific row in the metric table.

The [README](../README.md#one-microscopy-field) pairs the weddellite field from row 2, column 3 of this collage with the seven expert polygons for the same field. The confidence values come from the printed predictions. The green text at the left edge belongs to the adjacent panel in the source collage.

## Defence overview

| Slides | Subject |
| --- | --- |
| 1–4 | Objectives, tools and project phases |
| 5–9 | Metadata, mixtures and acquisition variability |
| 10–11 | CVAT annotation by the hospital engineers |
| 12–15 | Label filtering, images per class and fold preparation |
| 16–20 | Training calls, confusion matrices and result summaries |

Slide 15 describes the earlier dataset of 607 images and 19 classes. The later experiment used 583 images and 15 classes. [Protocols for both experiments](experiments.md#protocols).

## Earlier planning slides

The planning slides include an external YOLOv9 workflow reference and possible augmentation choices. The implemented experiments use YOLO11n-seg and YOLO11m-seg. The early split slides contain a validation-size typo. The original `val_split.txt` has **123 entries**, which accounts for the remaining images after 490 of the 613 labelled images went into training.

## Confusion matrices

Report Figure 6.2, PDF page 22, contains the original confusion matrices. Their generating checkpoints are not identified. The report flags a negative entry in the earlier normalised matrix as an error; that matrix is not used for the quantitative summaries.
