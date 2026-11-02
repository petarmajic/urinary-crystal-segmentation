# Training notebook

[Open `PRI_train.ipynb`](PRI_train.ipynb)

The original Colab notebook contains preprocessing, training attempts and saved outputs. The index below uses **zero-based cell positions**, matching the notebook JSON, rather than execution counts. Execution counts can repeat or be absent.

| Cells | Content |
| --- | --- |
| 0–5 | Mount Drive, extract the dataset, locate images/labels and inspect the export |
| 6–12 | Merge aliases, count class support and retain usable labeled images |
| 13–16 | Build the clean dataset and multilabel-stratified fold files |
| 17–24 | Install/check dependencies, initial training attempts, inspect TIFF modes and convert RGBA copies to RGB, then train YOLO11n-seg |
| 25–27 | Inspect run paths and summarise the earlier experiment |
| 28–36 | Build the `drop4` dataset and its five folds |
| 37–38 | Train YOLO11m-seg and summarise each fold's best validation epoch |
| 39 | Export run artifacts to a ZIP in the original Colab environment |

The notebook retains historical paths, retries and an error output. Follow the [execution notes](../docs/reproducibility.md) before attempting to run it. [Experiment details](../docs/experiments.md) explain how the saved metrics were selected.

`archive/PRI_training_script.ipynb` is an identical copy supplied with the original deliverables. Both retain Git blob `f5aab47db35e68bb1b32476462df486b4ef3847c`; the top-level notebook is the canonical reading link.
