# Experiment results

| File | Contents |
| --- | --- |
| [recorded-fold-metrics.csv](recorded-fold-metrics.csv) | Five fold results from each experiment, with source cells and the rule used to select the reported epoch. |
| [yolo11m-layer-summary.csv](yolo11m-layer-summary.csv) | Twenty-four module rows from the saved 15-class model summary: connections, repeats, parameters and arguments. |

The earlier experiment's `epoch` field is empty because its summary prints the last-row metrics without an epoch number. The later experiment records the selected best validation epoch for each fold. The earlier retry identifier `fold_116` matches the notebook output.

[Protocols and metric interpretation](../docs/experiments.md) · [Model structure](../docs/architecture.md)
