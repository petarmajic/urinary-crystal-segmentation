# Environment and execution

## Notebook and data paths

To inspect the results, open the saved fold summaries in cells 26 and 38 of the [Colab notebook](../notebooks/PRI_train.ipynb). To train again, point the Drive mount and ZIP path to your copy of the CVAT export. The notebook expects the extracted images, labels and YAML under `/content/ds/cristals-YOLO_Ultralytics_v1.0`. Run the preparation cells for the chosen experiment to write its clean dataset and fold files.

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

Use the generated fold YAMLs when running the training cells. The separate local training helper uses 640 px inputs. The published fold scores come from the notebook’s 1024 px runs. [Training settings and result selection](experiments.md).

## Rebuild the figures

With Matplotlib, NumPy and Pillow installed, run the following from the repository root.

```bash
python scripts/documentation/research_figures.py
```

The script extracts the 24-row module table from cell 37. It then writes the five SVG figures and the two JPEG previews from the original split lists, notebook fold sizes, recorded metrics, class counts, expert polygons and report collage. This step uses the saved results and does not require training weights. [Figure sources](../assets/README.md).
