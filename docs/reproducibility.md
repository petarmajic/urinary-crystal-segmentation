# Environment and execution notes

## Start with the saved experiment

Open [`notebooks/PRI_train.ipynb`](../notebooks/PRI_train.ipynb) to inspect the original code and outputs. The [cell index](../notebooks/README.md) separates preparation, training attempts and the two result summaries. Read [experiments.md](experiments.md) before comparing results.

The notebook was written for Google Colab with a Drive-hosted ZIP. It extracts a directory named `cristals-YOLO_Ultralytics_v1.0` under `/content/ds/` and creates cleaned datasets and fold files there. It is an experiment record with retries, rather than a verified clean run-all entry point.

## Recorded environment

Saved training logs show **Python 3.12.12**, **Ultralytics 8.4.14** and **PyTorch 2.9.0+cu126**. Earlier logs record an **NVIDIA L4**; the later 15-class YOLO11m-seg call in cell 37 records an **NVIDIA A100-SXM4-80GB**. These describe saved sessions, not a newly tested installation specification or a guarantee that all cells used the same environment.

Directly used packages visible in the notebook include `ultralytics`, `numpy`, `pandas`, `PyYAML`, `Pillow` and `iterative-stratification`. The metadata extraction script uses Python's standard library. No complete lockfile was supplied. A new pinned environment should be verified separately rather than inferred from the package list.

## Before a new run

1. Prepare a separate working copy of the data. Preserve the raw images and source annotations.
2. Configure the notebook's Drive ZIP and `/content/ds/` paths, or adapt a separate runnable copy to the new location.
3. Confirm full-path image/label matching, image modes and the class mappings for the selected experiment.
4. Generate the intended clean dataset and five fold lists. Do not substitute the early 80/20 lists.
5. Inspect the resulting train/validation paths and class counts before starting a GPU training run.
6. Save the environment, fold lists, training arguments, per-epoch CSVs and checkpoint identities together.

These are preparation instructions, not a claim that the training was rerun during repository organisation.

## Known issues

| Original material | Issue / implication |
| --- | --- |
| Metadata script | Opens JSON mappings relative to the working directory and uses the historical `RawData/SÇlection cristaux Hennet` path |
| pH parser | Captures but does not use the fractional regex group consistently; a value such as `pH8.5` needs correction and a targeted test before trusting regenerated pH fields |
| Existing CSV | Retains historical paths and original extracted values; it has not been silently regenerated |
| Local split/training helpers | Several paths are absolute `/Users/petarmajic/...` paths; adapt a separate working version before execution |
| Original 80/20 split lists | 173 paths differ from the source tree only by Unicode normalisation of accented characters; normalise/resolve paths in a working copy before execution |
| Notebook image indexes | Some stages match by stem, which should be audited before flattening or refactoring |
| Notebook cell 25 | Retains a saved `FileNotFoundError` from exploratory path inspection |
| Intermediate clean dataset YAML | Temporarily points train and validation to `images/all`; the fold-specific lists are required for the described evaluation |
| Earlier experiment summary | Discovers `fold*` directories including retries and selects their last epoch |
| Later experiment summary | Uses validation mAP50–95 to select an epoch per fold; results need a separate test set for unbiased final assessment |

The organisation changes preserve the original source blobs. Logical fixes, a portable CLI and extraction into a Python package are separate future work.

## Rebuild the documentation figures

From the repository root, run:

```bash
python scripts/documentation/research_figures.py
```

This uses Matplotlib, NumPy and Pillow to read the saved notebook summary, the existing CSV tables and preserved source images. It extracts `results/yolo11m-layer-summary.csv`, redraws four SVG figures with STIX typography, including a paired microscopy/expert-annotation view from the existing dataset image and label file. It does not execute training or inference. The [architecture guide](architecture.md) and [asset ledger](../assets/README.md) explain the evidence and image sources.

## Large artifacts

The source repository includes the full image collection and its annotation export. Their contents and internal hierarchy are preserved under `data/`. This relocation does not make the Git history smaller. Dataset/model distribution or Git LFS migration should be planned separately, with data-provider permissions confirmed before external redistribution.
