from models.data_loader import RoboNetDataset

# Quick re-test
dataset = RoboNetDataset(files[:1], DATA_RAW, camera_idx=0, resize_to=(128, 128))
sample = dataset[0]

print("Imported from models/data_loader.py")
print("Filename:", sample['filename'])
print("Frames shape:", sample['frames'].shape)