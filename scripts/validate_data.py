# scripts/validate_data.py
"""
Validate all RoboNet HDF5 files in data/raw/robonet/hdf5
Checks for required keys (frames, actions, states)
Reports missing keys or corrupted files
"""

import os
import h5py
from tqdm import tqdm

DATA_RAW = r"E:\NVIDIA_PROJECTS\Neural-World-Model-for-Embodied-AI-Robotics\data\raw\robonet\hdf5"

files = [f for f in os.listdir(DATA_RAW) if f.endswith(".hdf5")]
print(f"Validating {len(files)} HDF5 files...\n")

issues = []
good_count = 0

for fname in tqdm(files, desc="Validating"):
    path = os.path.join(DATA_RAW, fname)
    try:
        with h5py.File(path, 'r') as f:
            # Required keys
            required = {
                'cam0_frames': 'env/cam0_video/frames',
                'actions': 'policy/actions',
                'states': 'env/state'
            }

            missing = []
            for name, key in required.items():
                if key not in f:
                    missing.append(name)

            if missing:
                issues.append(f"{fname}: missing {', '.join(missing)}")
            else:
                good_count += 1

    except Exception as e:
        issues.append(f"{fname}: error opening file - {str(e)}")

# Summary
print("\n" + "="*60)
print("VALIDATION SUMMARY")
print("="*60)
print(f"Total files checked: {len(files)}")
print(f"Valid files: {good_count} ({good_count/len(files)*100:.1f}%)")
print(f"Files with issues: {len(issues)}")

if issues:
    print("\nIssues found:")
    for issue in issues[:20]:  # show first 20 only
        print("  -", issue)
    if len(issues) > 20:
        print(f"  ... and {len(issues)-20} more")
else:
    print("All files look valid! No issues found.")