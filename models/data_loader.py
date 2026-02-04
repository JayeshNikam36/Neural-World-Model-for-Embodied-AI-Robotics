import os
import h5py
import imageio.v3 as iio
from io import BytesIO
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset
import torchvision.transforms as T

class RoboNetDataset(Dataset):
    def __init__(self, file_list, data_root, camera_idx=0, resize_to=(128, 128), seq_len=15):
        self.file_list = file_list
        self.data_root = data_root
        self.camera_idx = camera_idx
        self.resize_to = resize_to
        self.seq_len = seq_len

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        file_path = os.path.join(self.data_root, self.file_list[idx])

        with h5py.File(file_path, 'r') as f:
            cam_key = f'env/cam{self.camera_idx}_video/frames'
            video_bytes = f[cam_key][()].tobytes()
            frames_np = iio.imread(BytesIO(video_bytes), extension=".mp4", plugin="pyav")

            # --- STANDARD DIMENSION FIXES ---
            # 1. Fix Actions (Force to dim 4)
            raw_actions = torch.from_numpy(f['policy/actions'][:]).float()
            if raw_actions.shape[-1] < 4:
                padding = torch.zeros((raw_actions.shape[0], 4 - raw_actions.shape[-1]))
                actions_all = torch.cat([raw_actions, padding], dim=-1)
            else:
                actions_all = raw_actions[:, :4]

            # 2. Fix States (Force to dim 5)
            # This is where your current error is coming from!
            raw_states = torch.from_numpy(f['env/state'][:]).float()
            if raw_states.shape[-1] < 5:
                padding = torch.zeros((raw_states.shape[0], 5 - raw_states.shape[-1]))
                states_all = torch.cat([raw_states, padding], dim=-1)
            else:
                states_all = raw_states[:, :5]

        # Convert frames
        frames_all = torch.from_numpy(frames_np).permute(0, 3, 1, 2).float() / 255.0

        # --- FIXED WINDOW SLICING ---
        T_total = frames_all.shape[0]
        if T_total >= self.seq_len:
            start = torch.randint(0, T_total - self.seq_len + 1, (1,)).item()
            frames = frames_all[start : start + self.seq_len]
            states = states_all[start : start + self.seq_len]
            actions = actions_all[start : start + self.seq_len - 1]
        else:
            # Emergency padding if the whole video is too short
            frames = frames_all
            states = states_all
            actions = actions_all[:frames.shape[0]-1]

        if self.resize_to:
            frames = F.interpolate(frames, size=self.resize_to, mode='bilinear', align_corners=False)

        return {
            'frames': frames,
            'actions': actions,
            'states': states
        }