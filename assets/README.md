# Chart sources

| Asset | Source and interpretation |
| --- | --- |
| `fold-validation.svg` | Five saved mask mAP50–95 values in notebook cell 38; mean and sample SD; best validation epoch per fold |
| `class-support.svg` | Two aligned bar plots from saved notebook cell 35: images containing a class and annotated instance counts |
| `workflow.svg` | Documentation diagram summarising four verified stages of the project |

Notebook cell positions are zero-based. Tabulated chart inputs are in [`results/recorded-fold-metrics.csv`](../results/recorded-fold-metrics.csv) and [`metadata/derived/drop4-class-support.csv`](../metadata/derived/drop4-class-support.csv). The charts replot existing summaries and do not imply new training or evaluation.

The original poster, report, presentations and recorded video are listed in the [material guide](../docs/media-guide.md), with their contents and the source locations of the prediction collage and confusion matrices.

Source notebook Git blob: `f5aab47db35e68bb1b32476462df486b4ef3847c`. Source report: `b97a7d25a2963ba8882e28c6fec022b3c8dbed28`. Source poster: `386ec6b88a52a27c7f775fe6c3b68db8c41b38cd`. Source defence: `468e7160737d238215b3b07c74cba2f863087bfb`. Source video: `683cc31d7c3da7bcac2fe048169e928d79bbed26`.

## Preview provenance

| Asset | Original source |
| --- | --- |
| `validation-predictions.jpg` | JPEG extracted unchanged from report Figure 6.3, PDF page 23 |
| `reported-confusion-matrices.png` | PNG extracted unchanged from report Figure 6.2, PDF page 22 |
| `poster-preview.jpg` | Rendered poster PDF page 1, resized |
| `video-preview.jpg` | Original video frame near 12.5 seconds, resized |
| `defence-preview.jpg` | Rendered defence slide 1, resized |
| `metadata-slide.jpg` | Rendered defence slide 5 |
| `annotation-slide.jpg` | Rendered defence slide 11 |
| `folds-slide.jpg` | Rendered defence slide 15 |

The previews preserve their source contents. Masks and class labels were not redrawn or corrected. The source collage does not establish its exact checkpoint identity.
