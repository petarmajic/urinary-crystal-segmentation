# Training notebook

[Open PRI_train.ipynb](PRI_train.ipynb)

The Colab notebook records data preparation, training and evaluation. Cell numbers below are zero-based positions in the notebook, independent of execution counters.

| Cells | Contents |
| --- | --- |
| 0–5 | Drive mount, dataset extraction and image/label inspection |
| 6–12 | Class aliases, support counts and label filtering |
| 13–16 | Clean dataset and multilabel-stratified folds |
| 17–24 | Dependencies, training attempts, RGBA/RGB conversion and YOLO11n-seg training |
| 25–27 | Run inspection and earlier metric summary |
| 28–36 | Fifteen-class dataset and fold generation |
| 37–38 | YOLO11m-seg training and best-epoch fold summary |
| 39 | Run export in the Colab environment |

[Environment and execution](../docs/reproducibility.md) · [Experiment settings and results](../docs/experiments.md)

`archive/PRI_training_script.ipynb` is the identical copy included in the original deliverables.
