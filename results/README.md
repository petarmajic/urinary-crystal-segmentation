# Experiment results

I used the notebook’s saved outputs for the fold chart and the architecture diagram. The tables retain the original precision, so you can check the means in the README against the five underlying scores.

| File | Contents |
| --- | --- |
| [recorded-fold-metrics.csv](recorded-fold-metrics.csv) | Five fold results from each experiment, with source cells and the rule used to select the reported epoch. |
| [yolo11m-layer-summary.csv](yolo11m-layer-summary.csv) | Twenty-four module rows from the saved 15-class model summary: connections, repeats, parameters and arguments. |

For YOLO11n-seg, cell 26 printed metrics from the last row of each run without its epoch number. I left `epoch` empty for those rows and kept the recorded retry name `fold_116`. For YOLO11m-seg, cell 38 recorded the epoch with the highest validation mask mAP50–95 in each fold.

[Protocols and metric interpretation](../docs/experiments.md) · [Model structure](../docs/architecture.md)
