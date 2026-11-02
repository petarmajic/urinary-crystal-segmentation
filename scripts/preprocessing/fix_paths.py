
import os

train_file = '/Users/petarmajic/nodulesproject-crystalclassification/cristals-YOLO_Ultralytics_v1.0/train.txt'

with open(train_file, 'r') as f:
    lines = f.readlines()

new_lines = [line.replace('data/images/', 'images/') for line in lines]

with open(train_file, 'w') as f:
    f.writelines(new_lines)

print(f"Updated {len(new_lines)} lines in {train_file}")
