# Neural World Model for Embodied AI & Robotics

<p align="center">
  <img src="docs/images/architecture_diagram.png" width="800" alt="Project Architecture">
  <br>
  <em>Building a physics-informed, multi-modal neural world model for real robot prediction and planning</em>
</p>

## Overview

This project develops a **neural world model** capable of predicting future states of robotic manipulation tasks from multi-modal inputs (RGB video, depth, proprioception).  
Trained on real-world datasets like **RoboNet**, the model generates video rollouts conditioned on actions — a key building block for model-based reinforcement learning, sim-to-real transfer, and embodied AI.

### Key Features (Planned)
- Multi-modal encoder (RGB + depth + robot states)
- Diffusion-based latent video prediction
- Physics-informed training (optical flow, collision, dynamics)
- Long-horizon open-loop rollouts
- TensorRT optimization for edge deployment (Jetson)
- Interactive Gradio demo

## Project Status
- Phase 0: Setup & Environment → **In Progress**
- Phase 1: Data Pipeline → Not started
- Phase 2: Encoder Models → Not started
- Phase 3: World Model Core → Not started
- Phase 4: Physics Integration → Not started
- Phase 5: Training Pipeline → Not started
- Phase 6: Optimization & TensorRT → Not started
- Phase 7: Demo & Documentation → Not started

## Installation (Placeholder)

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_GITHUB_USERNAME/neural-world-model-robotics.git
cd neural-world-model-robotics

# 2. Create and activate conda environment
conda create -n world_model python=3.10
conda activate world_model

# 3. Install dependencies (to be updated)
pip install -r requirements.txt

# 4. (Later) Run demo / training
python scripts/inference.py --help