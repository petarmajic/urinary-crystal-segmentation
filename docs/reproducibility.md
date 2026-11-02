# Environment and execution

## Notebook and data paths

The [Colab notebook](../notebooks/PRI_train.ipynb) mounts Drive, extracts the dataset ZIP under `/content/ds/cristals-YOLO_Ultralytics_v1.0`, prepares the clean datasets and generates fold files. Its saved cells include training attempts and retries; a complete fresh execution has not been verified.

| Path or file | Role |
| --- | --- |
| `data/annotated/` | Source CVAT/YOLO image and polygon export |
| `dataset_clean` | Colab working dataset for the 19-class experiment |
| `dataset_clean_drop4` | Colab working dataset for the 15-class experiment |
| `kfold/data_fold_*_abs.yaml` | Generated per-fold image lists and dataset configuration |
| `runs_kfold_drop4_yolo11m` | Later training runs, referenced by the saved summaries |

The clean datasets, generated fold lists, original run CSVs and trained checkpoints are not included as standalone files. Their creation and outputs are recorded in the notebook. The existing source split files describe the earlier 80/20 division; see [data layout](../data/README.md).

## Recorded environment

| Component | Saved version or device |
| --- | --- |
| Python | 3.12.12 |
| Ultralytics | 8.4.14 |
| PyTorch | 2.9.0+cu126 |
| Earlier experiment GPU | NVIDIA L4 |
| Later 15-class experiment GPU | NVIDIA A100-SXM4-80GB |

Other packages used directly include NumPy, pandas, PyYAML, Pillow and iterative-stratification. A complete environment lockfile is unavailable.

## Known issues

| Component | Current behaviour |
| --- | --- |
| Metadata script | Resolves JSON mappings from the working directory and uses a historical `RawData/SÇlection cristaux Hennet` prefix. |
| pH extraction | The parser does not consistently include the decimal part; stored values such as `pH8.5` require correction before reuse. |
| Local helper scripts | Contain absolute `/Users/petarmajic/...` paths. |
| Earlier split lists | 173 accented paths differ from the source names in Unicode normalisation. They resolve after NFC normalisation. |
| Image matching | Some notebook stages match files by stem. |
| Notebook cell 25 | Contains a saved `FileNotFoundError` from run-path inspection. |

For training, the notebook's Drive ZIP and working paths must point to the available data. The chosen experiment's fold YAML files determine its train/validation split. [Training settings and result selection](experiments.md) describe both protocols.

## Rebuild the figures

From the repository root, with Matplotlib, NumPy and Pillow installed:

```bash
python scripts/documentation/research_figures.py
```

The script extracts the saved module table and renders five SVG figures from the notebook outputs, CSV tables and existing image/polygon files. It runs no training or inference. [Figure sources](../assets/README.md).
