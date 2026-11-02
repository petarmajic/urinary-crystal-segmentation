import random
import os

# Define paths
base_dir = 'cristals-YOLO_Ultralytics_v1.0'
train_txt_path = os.path.join(base_dir, 'train.txt')
train_split_path = os.path.join(base_dir, 'train_split.txt')
val_split_path = os.path.join(base_dir, 'val_split.txt')

# Read all image paths from train.txt
with open(train_txt_path, 'r') as f:
    lines = f.readlines()

# Remove empty lines and strip whitespace
lines = [line.strip() for line in lines if line.strip()]

# Shuffle the data
random.seed(42)  # For reproducibility
random.shuffle(lines)

# Calculate split index (80% train, 20% val)
split_idx = int(len(lines) * 0.8)

# Split the data
train_data = lines[:split_idx]
val_data = lines[split_idx:]

# Write to new files
with open(train_split_path, 'w') as f:
    f.write('\n'.join(train_data))

with open(val_split_path, 'w') as f:
    f.write('\n'.join(val_data))

print(f"Total images: {len(lines)}")
print(f"Training images: {len(train_data)}")
print(f"Validation images: {len(val_data)}")
print(f"Created {train_split_path} and {val_split_path}")
