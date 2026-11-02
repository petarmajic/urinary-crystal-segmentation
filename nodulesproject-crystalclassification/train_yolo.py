from ultralytics import YOLO
import yaml

# Load hyperparameters
with open('/Users/petarmajic/nodulesproject-crystalclassification/hyp.yaml', 'r') as f:
    hyp = yaml.safe_load(f)

# Load a model
model = YOLO('yolo11n-seg.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(
    data='/Users/petarmajic/nodulesproject-crystalclassification/cristals-YOLO_Ultralytics_v1.0/data.yaml',
    epochs=50,
    imgsz=640,
    project='/Users/petarmajic/nodulesproject-crystalclassification/runs',
    name='crystal_yolo_v1',
    **hyp
)
