# Dataset and preprocessing

## Source collection

CHU Orléans medical experts supplied microscopy images with species codes and acquisition clues in their filenames. The original collection contains **659 images**. Images vary in resolution, illumination and morphology, and some show several species. The initial [dataset review](domain-notes/initial-dataset-review-fr.docx) explains why a directory name cannot be used directly as a complete label.

The [metadata CSV](../metadata/image_metadata.csv) consolidates names, paths, inferred species, mixture flags, abbreviations and pH. [Its field guide](../metadata/README.md) distinguishes extracted metadata from expert ground truth.

## Preparation stages

| Stage | Recorded count | Source |
| --- | --- | --- |
| Source image collection | 659 images | Metadata CSV; report Chapter 4 |
| Early random split | 490 train + 123 validation + 46 unannotated | Preserved dataset split lists |
| Later notebook matching | 612 labeled image stems | Notebook cells 3/6/10; report §6.1 |
| After alias merging and support filtering | 607 usable images, 19 classes, 7,492 retained instances | Notebook cell 10 |
| After dropping four classes and images with no remaining annotations | 583 images, 15 classes | Notebook cells 29–36 |

The early split accounts for 613 labeled images, while the later notebook matching stage counts 612. The notebook matches by filename stem and applies its own filtering. The exact one-image discrepancy has not been resolved. Treat these as separate recorded stages, rather than a verified lossless funnel.

## Annotations and class mapping

Medical engineers performed manual annotation in **CVAT**, then exported **Ultralytics YOLO Segmentation 1.0** labels. Each `.txt` line describes one instance:

```text
class_id x1 y1 x2 y2 ... xn yn
```

Coordinates are normalised polygon vertices. An image may contain multiple instances and multiple class IDs. These labels support instance segmentation rather than just one image-level category.

The source [`data.yaml`](../data/annotated/data.yaml) contains 41 class IDs. Notebook cell 6 merges five aliases:

| Original ID/name | Canonical target |
| --- | --- |
| 0 / brushite | 13 / Br_brushite |
| 1 / calcite | 17 / CAL_calcite |
| 2 / caoxite | 16 / C3_caoxite |
| 3 / cystine | 22 / CYS_cystine |
| 4 / dihydroxyadénine | 23 / DHAd_dihydroxyadénine |

This produces 36 unique canonical names. The notebook then removes classes without support and keeps classes present in at least five labeled images, producing the 19-class experiment. The 15-class variant additionally removes `ATZ_atazanavir`, `Cylindre`, `CEF_ceftriaxonate_de_calcium` and `CHOL_cholestérol`. Class IDs are remapped separately for each derived dataset. The source annotations remain unchanged in this repository.

## Class imbalance

![Recorded image and instance support for each of the 15 retained classes](../assets/class-support.svg)

Source: saved notebook cell 35, also available as [CSV](../metadata/derived/drop4-class-support.csv). Image counts overlap because an image can contain several species. Instance counts count annotated objects. A class with relatively few images can have many objects in each image.

The figure uses the original source codes. The full species names are in the CSV and [domain coding guide](domain-notes/crystal-coding-guide-fr.docx). `PACC_Plaque_vitreuse` is retained as the original training label, without reinterpreting its clinical meaning.

## Image compatibility and matching

Notebook cells 22–23 inspect TIFF image modes and convert two RGBA images to RGB in the cleaned working copy, after making backups there. The raw collection is preserved. Other preparation steps remove unusable annotations and remap retained class IDs.

Some notebook operations index images and labels by stem rather than full relative path. Any future pipeline refactor should check name collisions before flattening directories. The source review also mentions crops, duplicate photographs and different lighting views of a sample. Image-level folds do not by themselves establish independence at patient or specimen level.

The current export has 659 images and 612 nonempty label files. A tree-based audit found no repeated exact image stems. The early split lists also contain Unicode normalisation differences in accented names, described in the [path audit](../data/README.md#path-audit). This check does not replace pixel-level or specimen-level analysis.

## Train/validation strategy

The early helper scripts perform random 80/20 splitting with seed 42. The later notebook constructs a binary vector of class presence per image and uses `MultilabelStratifiedKFold(n_splits=5, shuffle=True, random_state=42)`.

Each fold holds out one subset for validation. Fold sizes in the 15-class experiment are **469/114, 463/120, 466/117, 467/116 and 467/116** for train/validation. These are the splits associated with the main reported results. They are distinct from the original random split files.

The source file named `test_split.txt` contains unannotated images. It cannot provide ground-truth test metrics. [Experiment interpretation](experiments.md) and [data layout](../data/README.md) explain the distinction.
