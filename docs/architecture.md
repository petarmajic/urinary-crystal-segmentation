# Model and experimental design

The main result uses **Ultralytics YOLO11m-seg**, initialised from `yolo11m-seg.pt` and fine-tuned on the prepared **15-class** crystal dataset. I used the Ultralytics architecture and prepared the dataset, merged duplicate labels, trained the models and evaluated their results.

![Dataset preparation, five-fold validation design and the multiscale YOLO11m-seg segmentation architecture.](../assets/workflow.svg)

**Figure 1.** (a) Images and expert polygon annotations are prepared for five-fold validation. (b) The model combines multiscale feature maps with mask prototypes and instance-specific coefficients. Tensor labels use height × width × channels. The microscopy image illustrates the source collection; volumes and fold cells are schematic.

## Dataset preparation

The source annotations use 41 class IDs. Five IDs are alternative labels for species already listed, so I merged them to obtain 36 class names. I then kept classes with labels in at least five images, giving 19 classes and 607 usable images. Removing four more classes and images without remaining annotations produced the main training set: **583 images, 15 classes and 7,371 annotated instances**.

The instance total is the sum of cell 35's [class counts](../metadata/derived/drop4-class-support.csv). [Dataset preparation](data.md#preparation-stages) describes the source collection and intermediate sets.

Metadata extraction produces a separate 659-row table for dataset review. Species, pH and mixture fields inferred from filenames are **not concatenated with the model's image features**. Manual polygons come from the CHU Orléans medical engineers' CVAT annotations.

## Feature extraction and fusion

The following dimensions are derived for a square **1024 × 1024** network input. Channels and module arguments agree with the model summary printed in notebook cell 37; spatial sizes follow the model's downsampling strides.

| Stage | Saved module / index | Feature shape, H × W × C |
| --- | --- | --- |
| Input | RGB image tensor | 1024 × 1024 × 3 |
| Backbone P3 | C3k2, layer 4 | 128 × 128 × 512 |
| Backbone P4 | C3k2, layer 6 | 64 × 64 × 512 |
| Backbone P5 | C3k2 → SPPF → C2PSA, layers 8–10 | 32 × 32 × 512 |
| Fused P3 | Upsample, concatenate, C3k2, layer 16 | **128 × 128 × 256** |
| Fused P4 | Downsample, concatenate, C3k2, layer 19 | **64 × 64 × 512** |
| Fused P5 | Downsample, concatenate, C3k2, layer 22 | **32 × 32 × 512** |

The backbone supplies features at strides 8, 16 and 32. The neck combines coarse and fine features through upsampling, concatenation and subsequent downsampling. All three fused outputs feed the `Segment` head. The diagram shows the dimensions of these feature tensors.

The saved summary reports **254 layers and 22,370,781 parameters**, with **22,370,765 parameters used for gradient updates**. These values describe the recorded 15-class configuration, not the original 80-class pretrained model. [The extracted module table](../results/yolo11m-layer-summary.csv) preserves all 24 top-level module rows and their printed arguments.

## From features to instance masks

The recorded head arguments are `Segment[15, 32, 256, 16, None, [256, 512, 512]]`. The relevant parts are:

| Head component | Meaning |
| --- | --- |
| `nc = 15` | Fifteen class-score outputs per candidate |
| `nm = 32` | Thirty-two instance-specific mask coefficients |
| Prototype branch | Reads the fused P3 tensor; outputs 32 prototype maps |
| Prototype spatial size | 256 × 256 for the nominal 1024 × 1024 input, after the prototype module's 2× upsampling |
| Detection outputs | Decoded bounding boxes and class scores, followed by non-maximum suppression |
| Final segmentation output | One mask, class label and confidence score per retained instance |

For instance *i*, the mask logit map is a learned linear combination of the prototype maps:

$$L_i(u,v)=\sum_{j=1}^{32} a_{ij}P_j(u,v).$$

Here, `a` denotes instance-specific mask coefficients and `P` the shared prototype maps. Postprocessing crops and resizes masks using the detected boxes. Ultralytics implements the reconstruction and postprocessing.

## Validation design

The notebook records which of the 15 classes appears in each image as a binary **583 × 15** matrix. It then applies `MultilabelStratifiedKFold(n_splits=5, shuffle=True, random_state=42)`. Multilabel stratification accounts for images containing more than one class when assigning them to folds.

One pretrained YOLO11m-seg model is initialised independently for each fold. Training uses batch size 4, up to 100 epochs and early-stopping patience 20. The reported summary selects each fold's highest validation mask mAP50–95 epoch.

[Actual fold sizes](data.md#trainvalidation-strategy) · [Training arguments and selected epochs](experiments.md)

## Sources

- **Project notebook:** notebook cells 29–38, including the printed model summary in cell 37.
- **Versioned architecture:** [Ultralytics 8.4.14 YOLO11 segmentation YAML](https://github.com/ultralytics/ultralytics/blob/v8.4.14/ultralytics/cfg/models/11/yolo11-seg.yaml).
- **Head implementation:** [Segment](https://github.com/ultralytics/ultralytics/blob/v8.4.14/ultralytics/nn/modules/head.py) and [Proto](https://github.com/ultralytics/ultralytics/blob/v8.4.14/ultralytics/nn/modules/block.py).
- **Microscopy illustration:** unchanged embedded image from the original project poster; see [asset sources](../assets/README.md).

[Back to project overview](../README.md)
