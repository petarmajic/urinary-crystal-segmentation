# Chart sources

| Asset | Source and interpretation |
| --- | --- |
| `fold-validation.svg` | Five saved mask mAP50–95 values in notebook cell 38; mean and sample SD; best validation epoch per fold |
| `class-support.svg` | Two aligned bar plots from saved notebook cell 35: images containing a class and annotated instance counts |
| `workflow.svg` | Two-panel research schematic: dataset preparation / five-fold roles and the 15-class YOLO11m-seg feature and mask-prediction architecture. Project dimensions and module arguments come from notebook cell 37, with head/prototype mechanics checked against Ultralytics 8.4.14 source. |
| `annotation-example.svg` | Original `C2_taill_heter_lb.jpg` field and all seven polygons from its matching source label file. Source class ID 15 is `C2_weddellite`; it maps to ID 4 in the 15-class experiment. This is expert annotation, not model inference. |
| `source/microscopy-example.jpg` | Unchanged JPEG extracted from the original project poster (`poster-p1-img2.jpeg` in the review extraction); illustrative microscopy input, with no class or prediction assigned. |

Notebook cell positions are zero-based. Tabulated chart inputs are in [`results/recorded-fold-metrics.csv`](../results/recorded-fold-metrics.csv) and [`metadata/derived/drop4-class-support.csv`](../metadata/derived/drop4-class-support.csv). The charts replot existing summaries and do not imply new training or evaluation. All text in the SVG figures is exported as vector outlines, keeping font appearance consistent when viewed on GitHub or on a device without the original font.

The four figures use STIX typography, exported as vector outlines. The original poster, report, presentations and recorded video are listed in the [material guide](../docs/media-guide.md), with their contents and the source locations of the prediction collage and confusion matrices.

The model drawing represents the Ultralytics architecture that was fine-tuned. It does not imply a custom architecture, display measured feature activations or pair the illustrative raw image with a prediction. The fold grid illustrates training/validation roles, not equal subset sizes. The main 15-class protocol is separate from the earlier 19-class experiment.

The [architecture guide](../docs/architecture.md) records feature dimensions, the head configuration and versioned upstream references. The [module summary CSV](../results/yolo11m-layer-summary.csv) is extracted from saved notebook text. Rebuild the figures with `python scripts/documentation/research_figures.py`; this does not run a model.

The annotation figure uses the existing source image (Git blob `01ff8160587150095262c29ed09a4088f3eecdce`) and matching label file (`b564fbda930e01ff3f7392963d7684430f054c8a`). All seven polygons are shown. See the [annotation example](../docs/data.md#annotation-example) for the original and remapped class IDs.

Source notebook Git blob: `f5aab47db35e68bb1b32476462df486b4ef3847c`. Source report: `b97a7d25a2963ba8882e28c6fec022b3c8dbed28`. Source poster: `386ec6b88a52a27c7f775fe6c3b68db8c41b38cd`. Source defence: `468e7160737d238215b3b07c74cba2f863087bfb`. Source video: `683cc31d7c3da7bcac2fe048169e928d79bbed26`.

## Preview provenance

| Asset | Original source |
| --- | --- |
| `validation-predictions.jpg` | JPEG extracted unchanged from report Figure 6.3, PDF page 23 |
| `prediction-overview.jpg` | Top row of that collage, crop rectangle (0, 0, 1920, 440); no masks, class labels or scores redrawn |
| `reported-confusion-matrices.png` | PNG extracted unchanged from report Figure 6.2, PDF page 22 |
| `poster-preview.jpg` | Rendered poster PDF page 1, resized |
| `video-preview.jpg` | Original video frame near 12.5 seconds, resized |
| `defence-preview.jpg` | Rendered defence slide 1, resized |
| `metadata-slide.jpg` | Rendered defence slide 5, linked from the original-slide reference section |
| `annotation-slide.jpg` | Rendered defence slide 11, linked from the original-slide reference section |
| `folds-slide.jpg` | Rendered defence slide 15, linked from the original-slide reference section |
| `metadata-excerpt.png` | Source image embedded in defence slide 5, with the bottom portal bar cropped and a neutral frame added |
| `annotation-excerpt.png` | Source image embedded in defence slide 11, fitted to the same frame without changing the annotation content |

The previews preserve their source contents. Masks and class labels were not redrawn or corrected. The source collage does not establish its exact checkpoint identity.
