# Figure sources

The figures use the model summary, fold results, class counts and source images listed below.

| Figure | Data or source |
| --- | --- |
| `fold-validation.svg` | Five mask mAP50–95 values from cell 38, with their mean and sample SD. |
| `class-support.svg` | Image and annotated-instance counts from cell 35. |
| `workflow.svg` | Preparation code and saved YOLO11m-seg module summary, cell 37; architecture mechanics checked against Ultralytics 8.4.14. Volumes and fold cells are schematic. |
| `annotation-example.svg` | `C2_taill_heter_lb.jpg` and all seven polygons from its matching label file. Source ID 15 maps to ID 4 in the prepared dataset. |
| `source/microscopy-example.jpg` | Embedded microscopy image from the original project poster, used to illustrate the input collection. |

The plotted values are available in [fold metrics](../results/recorded-fold-metrics.csv), [class support](../metadata/derived/drop4-class-support.csv) and the [module summary](../results/yolo11m-layer-summary.csv).

## Report and presentation images

| Asset | Source |
| --- | --- |
| `validation-predictions.jpg` | Report Figure 6.3, PDF page 23; embedded JPEG. |
| `prediction-overview.jpg` | Top-row excerpt of Figure 6.3, crop `(0, 0, 1920, 440)`. |
| `reported-confusion-matrices.png` | Report Figure 6.2, PDF page 22. |
| Poster and video previews | Rendered poster page and video frame near 12.5 seconds. |
| Defence slide previews | Slides 1, 5, 11 and 15. |
| Metadata and annotation excerpts | Embedded images from defence slides 5 and 11, framed for display. |

[Rendering command and dependencies](../docs/reproducibility.md#rebuild-the-figures) · [Architecture references](../docs/architecture.md#sources)
