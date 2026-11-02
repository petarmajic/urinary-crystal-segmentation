# Figure sources

All generated figures use the saved experiment evidence. Source cell numbers below are zero-based notebook positions.

| Figure | Data or source |
| --- | --- |
| `results-overview.svg` | YOLO11m-seg fold scores from notebook cell 38; mean and sample SD rounded to three decimal places. Dataset size: cell 33; class count: cell 35. |
| `fold-validation.svg` | Five mask mAP50–95 values from cell 38, with their mean and sample SD. |
| `class-support.svg` | Image and annotated-instance counts from cell 35. |
| `workflow.svg` | Preparation code and saved YOLO11m-seg module summary, cell 37; architecture mechanics checked against Ultralytics 8.4.14. Volumes and fold cells are schematic. |
| `annotation-example.svg` | `C2_taill_heter_lb.jpg` and all seven polygons from its matching label file. Source ID 15 maps to ID 4 in the prepared dataset. |
| `source/microscopy-example.jpg` | Embedded microscopy image from the original project poster, used to illustrate the input collection. |

Numeric inputs are available in [fold metrics](../results/recorded-fold-metrics.csv), [class support](../metadata/derived/drop4-class-support.csv) and the [module summary](../results/yolo11m-layer-summary.csv).

## Original visual extracts

| Asset | Source |
| --- | --- |
| `validation-predictions.jpg` | Report Figure 6.3, PDF page 23; embedded JPEG. |
| `prediction-overview.jpg` | Top-row excerpt of Figure 6.3, crop `(0, 0, 1920, 440)`. |
| `reported-confusion-matrices.png` | Report Figure 6.2, PDF page 22. |
| Poster and video previews | Rendered poster page and video frame near 12.5 seconds. |
| Defence slide previews | Slides 1, 5, 11 and 15. |
| Metadata and annotation excerpts | Embedded images from defence slides 5 and 11, framed for display. |

[Rendering command and dependencies](../docs/reproducibility.md#rebuild-the-figures) · [Architecture references](../docs/architecture.md#sources)
