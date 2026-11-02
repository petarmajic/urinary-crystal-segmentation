# Recorded metric tables

[`recorded-fold-metrics.csv`](recorded-fold-metrics.csv) contains ten rows extracted from the saved text tables in the original notebook: five from zero-based cell 26 and five from cell 38. It preserves the reported fold identifiers, displayed metric precision, source cell and epoch-selection rule. This is a transcription of recorded summaries, not the missing original per-epoch run CSVs.

The `epoch` field is empty for the earlier experiment because that summary does not print the selected last epoch number. For the 15-class experiment it records each fold's best validation epoch. The `fold_116` name is retained exactly as printed.

See [experiment details](../docs/experiments.md) before comparing the two groups. The README's metric plot uses only `yolo11m_drop4_15_classes`.
