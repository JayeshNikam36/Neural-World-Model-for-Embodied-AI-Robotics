import os

def make_dir(path):
    os.makedirs(path, exist_ok=True)

def make_file(path):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    if not os.path.exists(path):
        with open(path, "w"):
            pass

# -----------------------------
# Directories
# -----------------------------

dirs = [
    ".github/workflows",
    ".github/ISSUE_TEMPLATE",

    "data/raw/robonet",
    "data/raw/bridge",
    "data/raw/mime",
    "data/processed/train/videos",
    "data/processed/train/depths",
    "data/processed/train/states",
    "data/processed/val/videos",
    "data/processed/val/depths",
    "data/processed/val/states",
    "data/processed/test/videos",
    "data/processed/test/depths",
    "data/processed/test/states",
    "data/cache/encoded_features",

    "models/encoders",
    "models/diffusion",
    "models/physics",

    "configs/model",
    "configs/data",
    "configs/training",
    "configs/deployment",

    "scripts/data",
    "scripts/training",
    "scripts/optimization",
    "scripts/inference",
    "scripts/utils",

    "notebooks",

    "tests/unit",
    "tests/integration",
    "tests/performance",

    "outputs/videos/train_samples",
    "outputs/videos/val_samples",
    "outputs/videos/test_samples",
    "outputs/videos/demo_videos",
    "outputs/images/data_samples",
    "outputs/images/predictions",
    "outputs/images/comparisons",
    "outputs/images/metrics",

    "checkpoints/vae",
    "checkpoints/world_model",
    "checkpoints/optimized",

    "logs/tensorboard/vae_training",
    "logs/tensorboard/world_model_training",
    "logs/wandb",
    "logs/training_logs",

    "docs/images",
    "docs/tutorials",

    "deployment/docker",
    "deployment/kubernetes",
    "deployment/cloud",
    "deployment/edge",

    "demo/assets/sample_videos",
    "demo/assets/screenshots",
    "demo/examples",

    ".vscode",
]

for d in dirs:
    make_dir(d)

# -----------------------------
# Files
# -----------------------------

files = [
    # GitHub
    ".github/workflows/ci.yml",
    ".github/workflows/tests.yml",
    ".github/workflows/deploy.yml",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/PULL_REQUEST_TEMPLATE.md",

    # data
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/cache/.gitkeep",
    "data/processed/train/metadata.json",
    "data/processed/val/metadata.json",
    "data/processed/test/metadata.json",

    # models
    "models/__init__.py",
    "models/world_model.py",
    "models/data_loader.py",
    "models/data_utils.py",

    "models/encoders/__init__.py",
    "models/encoders/rgb_encoder.py",
    "models/encoders/depth_encoder.py",
    "models/encoders/proprio_encoder.py",
    "models/encoders/fusion.py",
    "models/encoders/multimodal_encoder.py",

    "models/diffusion/__init__.py",
    "models/diffusion/vae_encoder.py",
    "models/diffusion/vae_decoder.py",
    "models/diffusion/vae.py",
    "models/diffusion/unet.py",
    "models/diffusion/scheduler.py",
    "models/diffusion/pipeline.py",
    "models/diffusion/attention.py",

    "models/physics/__init__.py",
    "models/physics/optical_flow.py",
    "models/physics/collision.py",
    "models/physics/dynamics.py",
    "models/physics/gravity.py",
    "models/physics/physics_losses.py",

    # configs
    "configs/model/encoder_config.yaml",
    "configs/model/vae_config.yaml",
    "configs/model/diffusion_config.yaml",
    "configs/model/physics_config.yaml",
    "configs/model/world_model_config.yaml",

    "configs/data/robonet_config.yaml",
    "configs/data/bridge_config.yaml",
    "configs/data/preprocessing_config.yaml",
    "configs/data/augmentation_config.yaml",

    "configs/training/base.yaml",
    "configs/training/vae_training.yaml",
    "configs/training/world_model_training.yaml",
    "configs/training/hyperparameters.yaml",

    "configs/deployment/local_inference.yaml",
    "configs/deployment/tensorrt_config.yaml",
    "configs/deployment/jetson_config.yaml",

    # scripts
    "scripts/__init__.py",
    "scripts/data/download_robonet.py",
    "scripts/data/download_bridge.py",
    "scripts/data/preprocess_data.py",
    "scripts/data/validate_data.py",
    "scripts/data/create_splits.py",
    "scripts/data/visualize_data.py",

    "scripts/training/train_vae.py",
    "scripts/training/train_world_model.py",
    "scripts/training/resume_training.py",
    "scripts/training/evaluate_model.py",

    "scripts/optimization/quantize_model.py",
    "scripts/optimization/prune_model.py",
    "scripts/optimization/convert_to_onnx.py",
    "scripts/optimization/convert_to_tensorrt.py",

    "scripts/inference/inference.py",
    "scripts/inference/batch_inference.py",
    "scripts/inference/realtime_inference.py",

    "scripts/utils/setup_check.py",
    "scripts/utils/gpu_monitor.py",
    "scripts/utils/benchmark.py",
    "scripts/utils/export_model.py",

    "scripts/test_pytorch.py",
    "scripts/test_gpu.py",
    "scripts/test_imports.py",

    # tests
    "tests/__init__.py",
    "tests/conftest.py",
    "tests/unit/__init__.py",
    "tests/unit/test_data_loader.py",
    "tests/unit/test_encoders.py",
    "tests/unit/test_vae.py",
    "tests/unit/test_diffusion.py",
    "tests/unit/test_physics.py",
    "tests/unit/test_world_model.py",

    "tests/integration/__init__.py",
    "tests/integration/test_data_pipeline.py",
    "tests/integration/test_training_pipeline.py",
    "tests/integration/test_inference_pipeline.py",

    "tests/performance/__init__.py",
    "tests/performance/test_encoding_speed.py",
    "tests/performance/test_inference_speed.py",
    "tests/performance/test_memory_usage.py",

    # outputs
    "outputs/.gitkeep",
    "outputs/metrics/vae_metrics.json",
    "outputs/metrics/world_model_metrics.json",
    "outputs/metrics/physics_metrics.json",
    "outputs/metrics/benchmark_results.json",

    # checkpoints
    "checkpoints/.gitkeep",

    # logs
    "logs/.gitkeep",
    "logs/training_logs/vae_training.log",
    "logs/training_logs/world_model_training.log",

    # docs
    "docs/PROJECT_PLAN.md",
    "docs/ARCHITECTURE.md",
    "docs/DATASET.md",
    "docs/EXPERIMENTS.md",
    "docs/NOTES.md",
    "docs/DEPLOYMENT.md",
    "docs/API.md",
    "docs/TROUBLESHOOTING.md",

    "docs/images/architecture_diagram.png",
    "docs/images/data_flow.png",
    "docs/images/model_architecture.png",

    "docs/tutorials/01_getting_started.md",
    "docs/tutorials/02_training_guide.md",
    "docs/tutorials/03_inference_guide.md",
    "docs/tutorials/04_optimization_guide.md",

    # deployment
    "deployment/docker/Dockerfile.dev",
    "deployment/docker/Dockerfile.prod",
    "deployment/docker/Dockerfile.jetson",
    "deployment/docker/docker-compose.yml",

    "deployment/kubernetes/deployment.yaml",
    "deployment/kubernetes/service.yaml",

    "deployment/cloud/kaggle_notebook.ipynb",
    "deployment/cloud/colab_notebook.ipynb",
    "deployment/cloud/aws_setup.sh",

    "deployment/edge/jetson_setup.sh",
    "deployment/edge/optimize_for_edge.py",

    # demo
    "demo/app.py",
    "demo/demo_utils.py",
    "demo/requirements_demo.txt",
    "demo/README.md",

    # vscode
    ".vscode/settings.json",
    ".vscode/launch.json",
    ".vscode/extensions.json",

    # root
    ".gitignore",
    ".env.example",
    ".dockerignore",
    "requirements.txt",
    "requirements-dev.txt",
    "requirements-demo.txt",
    "setup.py",
    "pyproject.toml",
    "environment.yml",
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "Makefile",
]

for f in files:
    make_file(f)

print("✅ neural-world-model-robotics structure created successfully!")
