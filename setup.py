from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="neural-world-model-robotics",
    version="0.1.0",
    author="Jayesh, Mahadi", # Changed to a string and added the missing comma
    packages=find_packages(),
    install_requires=requirements,
    description="Neural World Model for Embodied AI Robotics",
)