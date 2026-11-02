import os
import random
from pathlib import Path

# Define base paths
base_dir = '/Users/petarmajic/nodulesproject-crystalclassification/cristals-YOLO_Ultralytics_v1.0'
images_dir = os.path.join(base_dir, 'images')
labels_dir = os.path.join(base_dir, 'labels')

# Output files
train_split_path = os.path.join(base_dir, 'train_split.txt')
val_split_path = os.path.join(base_dir, 'val_split.txt')
test_split_path = os.path.join(base_dir, 'test_split.txt')

# Extensions to look for
valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff'}

labeled_images = []
unlabeled_images = []

print("Scanning for images and matching labels...")

# Walk through the images directory
for root, dirs, files in os.walk(images_dir):
    for file in files:
        if os.path.splitext(file)[1].lower() in valid_extensions:
            image_path = os.path.join(root, file)
            
            # Construct expected label path
            # Replace 'images' with 'labels' in the path
            # This assumes the structure mirrors exactly: .../images/... -> .../labels/...
            rel_path = os.path.relpath(image_path, images_dir)
            label_rel_path = os.path.splitext(rel_path)[0] + '.txt'
            label_path = os.path.join(labels_dir, label_rel_path)
            
            if os.path.exists(label_path):
                # Verify label file is not empty
                if os.path.getsize(label_path) > 0:
                    # Store relative path from the dataset root (for YOLO)
                    # YOLO expects paths relative to the 'path' in data.yaml or absolute paths
                    # We will use relative paths to 'path' (which is '.')
                    # So we need 'images/train/...'
                    rel_path_from_root = os.path.relpath(image_path, base_dir)
                    labeled_images.append(rel_path_from_root)
                else:
                    # Store relative path for unlabeled images too
                    rel_path_from_root = os.path.relpath(image_path, base_dir)
                    unlabeled_images.append(rel_path_from_root)
            else:
                rel_path_from_root = os.path.relpath(image_path, base_dir)
                unlabeled_images.append(rel_path_from_root)

# Shuffle and split
random.seed(42)
random.shuffle(labeled_images)

split_idx = int(len(labeled_images) * 0.8)
train_data = labeled_images[:split_idx]
val_data = labeled_images[split_idx:]

# Write to files
with open(train_split_path, 'w') as f:
    f.write('\n'.join(train_data))

with open(val_split_path, 'w') as f:
    f.write('\n'.join(val_data))

with open(test_split_path, 'w') as f:
    f.write('\n'.join(unlabeled_images))

print("-" * 30)
print(f"Total images found: {len(labeled_images) + len(unlabeled_images)}")
print(f"Labeled images (usable): {len(labeled_images)}")
print(f"Unlabeled images (skipped): {len(unlabeled_images)}")
print("-" * 30)
print(f"Training set size: {len(train_data)}")
print(f"Validation set size: {len(val_data)}")
print(f"Test set size (unlabeled): {len(unlabeled_images)}")
print("-" * 30)
print(f"Created files:\n{train_split_path}\n{val_split_path}\n{test_split_path}")
