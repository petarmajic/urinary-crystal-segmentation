# Experiments and recorded results

## How to read the results

The main README reports the **15-class YOLO11m-seg experiment**. Its summary selects the epoch with the highest validation mask mAP50–95 in each fold, then calculates the mean and sample standard deviation across five folds. This selection uses validation data, so the reported result is not an unbiased estimate on a separate test set.

The source is the saved output of zero-based cell 38 in [`PRI_train.ipynb`](../notebooks/PRI_train.ipynb). [Recorded per-fold metrics](../results/recorded-fold-metrics.csv) preserve the table values and selection rules. The figures and tables here use these recorded outputs; they are not results of a new training run.

## Protocols

| Setting | Earlier experiment | 15-class experiment |
| --- | --- | --- |
| Initial model weights | `yolo11n-seg.pt` | `yolo11m-seg.pt` |
| Prepared dataset | `dataset_clean` | `dataset_clean_drop4` |
| Images / classes | 607 / 19 | 583 / 15 |
| Input size | 1024 | 1024 |
| Batch size | 4 | 4 |
| Maximum epochs | 50 | 100 |
| Early-stopping patience | 10 | 20 |
| Fold strategy | 5-fold multilabel stratification | 5-fold multilabel stratification |
| Split seed | 42 | 42 |
| Saved summary rule | Last CSV row in discovered `fold*` directories | Best validation mask mAP50–95 row in each of `fold_1` to `fold_5` |
| Source cells | 24, 26–27 | 29–38 |

The 15-class variant removes four labels and any image left without a retained instance. Its training call sets `degrees=15`, `translate=0.10`, `scale=0.50`, `fliplr=0.5`, `flipud=0.5`, `mosaic=0`, `mixup=0`, `hsv_h=0.01`, `hsv_s=0.10`, `hsv_v=0.10` and `workers=0`. Other settings follow the installed library's behaviour. The split seed is distinct from the trainer seed; saved trainer output records `seed=0`.

The earlier experiment needs particular care. The report describes a configuration with augmentations disabled, and notebook cell 20 contains that attempt. The later successful call in cell 24 omits those overrides. Its saved trainer log shows defaults including `mosaic=1.0`, `fliplr=0.5` and `scale=0.5`. The summary includes `fold_116`, reflecting retries. Use the code and saved run output when interpreting the actual experiment, rather than assuming all earlier runs used the settings in the report.

The local [`train_yolo.py`](../scripts/training/train_yolo.py) and [`hyp.yaml`](../configs/hyp.yaml) describe a **separate 640 px setup**. They should not be used to explain the 1024 px Colab results.

## YOLO11m-seg: per-fold mask metrics

| Fold | Selected epoch | Precision | Recall | mAP50 | mAP50–95 |
| --- | --- | --- | --- | --- | --- |
| 1 | 74 | 0.70804 | 0.70550 | 0.74196 | 0.54213 |
| 2 | 86 | 0.72261 | 0.57173 | 0.63074 | 0.43539 |
| 3 | 96 | 0.70589 | 0.65048 | 0.69201 | 0.50307 |
| 4 | 86 | 0.72940 | 0.62664 | 0.68972 | 0.51075 |
| 5 | 79 | 0.64486 | 0.59843 | 0.65183 | 0.44580 |
| **Mean ± SD** | — | **0.7022 ± 0.0335** | **0.6306 ± 0.0513** | **0.6813 ± 0.0427** | **0.4874 ± 0.0453** |

![Mask mAP50–95 values across five validation folds](../assets/fold-validation.svg)

Fold 1 has the highest recorded selected-epoch mAP50–95. Reporting only its 0.54213 would hide the spread between folds. The shaded band shows one sample standard deviation around the mean, not a confidence interval.

## Earlier YOLO11n-seg result

| Recorded directory | Mask precision | Mask recall | Mask mAP50 | Mask mAP50–95 |
| --- | --- | --- | --- | --- |
| `fold_116` | 0.61371 | 0.56273 | 0.57343 | 0.41634 |
| `fold_2` | 0.67119 | 0.67146 | 0.66148 | 0.46970 |
| `fold_3` | 0.57843 | 0.51078 | 0.54918 | 0.37283 |
| `fold_4` | 0.64063 | 0.56732 | 0.58160 | 0.40381 |
| `fold_5` | 0.51591 | 0.49205 | 0.50193 | 0.35498 |
| **Mean ± SD** | **0.6040 ± 0.0599** | **0.5609 ± 0.0699** | **0.5735 ± 0.0581** | **0.4035 ± 0.0443** |

These rows come from the **last recorded epoch**, as selected by notebook cell 26. They should not be relabelled as each fold's best epoch.

## What the metrics measure

- **Mask precision / recall:** the evaluator's segmentation-mask precision and recall outputs for the run.
- **Mask mAP50:** mean average precision for masks at IoU 0.50.
- **Mask mAP50–95:** mean average precision for masks across IoU thresholds 0.50 to 0.95 in steps of 0.05.

The tables use the `(M)` columns from Ultralytics results. They are separate from bounding-box `(B)` metrics and from image classification accuracy. Model confidence scores displayed on a prediction image are also separate quantities.

## Interpretation and limitations

The later configuration has higher recorded scores, but **several factors change together**: model size, retained classes, image set, augmentation settings, training budget and summary selection. The experiments do not isolate the effect of any one change. No relative improvement percentage is attributed solely to YOLO11m.

Five-fold stratification balances image-level class presence. It does not establish separation by patient, specimen or acquisition session. The original review describes crops, duplicates and views of the same sample under different lighting. Group identifiers and perceptual similarity would need separate investigation before stronger generalisation claims.

The report's confusion matrices and prediction collage provide qualitative evidence, but their exact generating checkpoints are not identified in the figure files. The report also notes a negative entry in an earlier normalised confusion matrix. That plot is retained in the original report rather than reconstructed or treated as a valid probability table. Background row/column interpretation requires checking the original evaluator's axis convention.

The unannotated `test_split.txt` subset has no ground truth for quantitative testing. There is no independent external or clinical test in the inspected artifacts. Class imbalance and limited support for rare species remain relevant when reading the aggregate scores.

## Available evidence

| Artifact | Available here |
| --- | --- |
| Notebook code and saved training logs | [Original notebook](../notebooks/PRI_train.ipynb) |
| Recorded fold summary values | [CSV](../results/recorded-fold-metrics.csv) |
| Written methodology and original figures | [Report](reports/project-report.pdf), Chapter 6 |
| Per-epoch run CSVs / exported model checkpoints | Not present as standalone files in the inspected source tree |
| Original run ZIP | Its export log is saved in notebook cell 39; the ZIP itself is not included |

The report preserves its original wording. This guide clarifies differences between that narrative, the notebook calls and the saved outputs.
