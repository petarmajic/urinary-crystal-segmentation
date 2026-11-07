# Figure sources

The two images at the top of the README show the same weddellite field, `C2_taill_heter_lb.jpg`. To make the expert panel, I drew all seven polygons from the field’s label file. For the prediction panel, I cropped row 2, column 3 of the report collage (pixel bounds `1280, 448, 1920, 896`). The neighbouring panel’s green label text crosses the left edge in the original collage. The report does not name the checkpoint. [Expert annotation](weddellite-expert.jpg) · [Prediction](weddellite-prediction.jpg) · [Uncropped collage](validation-predictions.jpg).

| Figure | Data or source |
| --- | --- |
| [Image splits and validation folds](validation-fold-layout.svg) | Counts from the three original split lists, train/validation sizes from notebook cell 36 and selected epochs with their mask scores from cell 38. Each highlighted group is held out once. |
| [Class counts](class-support.svg) | Image and annotated-instance counts from cell 35. |
| [Single-crystal mask](single-crystal-mask.svg) | The circle marks the lower C2 crystal in the original field. The enlarged mask is a crop of report Figure 6.3 (pixel bounds `1606, 816, 1701, 880`). The intermediate labels describe the recorded YOLO11m-seg head. |
| [Architecture and preparation](workflow.svg) | Preparation code and saved YOLO11m-seg module summary, cell 37; architecture mechanics checked against Ultralytics 8.4.14. Volumes and fold cells are schematic. |
| [Expert polygons](annotation-example.svg) | `C2_taill_heter_lb.jpg` and all seven polygons from its matching label file. Source ID 15 maps to ID 4 in the prepared dataset. |
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
