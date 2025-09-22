# Astro-Suraksha
# Duality AI's Space Station Challenge: Safety Object Detection #2

## Overview
This project addresses the Duality AI Space Station Challenge, focusing on training a robust object detection model to identify seven key pieces of safety equipment in a simulated space station environment. The model was trained using a synthetic dataset from Duality AI's Falcon digital twin simulation platform.

## Getting Started

### Prerequisites
* The provided Hackathon dataset.
* Python 3.10.0: The specific Python version under which the project was developed and tested.
* PyTorch (torch-2.8.0+cpu): The machine learning framework used by YOLOv8.


### Installation and Setup
1.  Create a Falcon account to access the dataset and tools.
2.  Download the dataset to your local machine.
3.  Navigate to the `ENV_SETUP` subfolder and run `setup_env.bat` (Windows) or an equivalent `setup_env.sh` script (Mac/Linux) to create the `EDU` environment with all necessary dependencies.

### Training the Model
1.  Open an Anaconda Prompt or terminal and navigate to the training scripts directory.
2.  Activate the environment by running `conda activate EDU.
3. Start training with the command: `python train.py`.

## Evaluation

Model performance is evaluated using the following key metrics:

* **mAP@0.5**: This is the primary metric for the hackathon and measures the model's accuracy in detecting and classifying objects with a 50% Intersection over Union (IoU) threshold.
* **Precision and Recall**: These metrics provide insight into the correctness of positive predictions and the model's ability to find all positive instances, respectively.
* **Confusion Matrix**: A visualization that highlights class-wise performance and helps identify misclassifications.


