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
1.  To train the model, follow a standard workflow using your system's terminal or command line interface.
2.  Navigate to the project directory: First, open a new terminal window and change your current directory to the folder containing your training scripts.
    Activate the project environment: Run the command to activate the virtual environment you created for this project. This step ensures all the necessary             libraries and dependencies are loaded correctly.
3.  Start the training process: Once the environment is active, execute the training script using the Python interpreter. The command python train.py will initiate     the model training.

## Evaluation

Model performance is evaluated using the following key metrics:

* **mAP@0.5**: This is the primary metric for the hackathon and measures the model's accuracy in detecting and classifying objects with a 50% Intersection over Union (IoU) threshold.
* **Precision and Recall**: These metrics provide insight into the correctness of positive predictions and the model's ability to find all positive instances, respectively.
* **Confusion Matrix**: A visualization that highlights class-wise performance and helps identify misclassifications.

## Results

<img width="1920" height="1100" alt="image" src="https://github.com/user-attachments/assets/424d7c9f-bca7-47a3-aebc-0f971090ed5b" />


<img width="3000" height="2250" alt="image" src="https://github.com/user-attachments/assets/5f28169f-a37e-4597-b5e4-7bcb84bbb318" />


<img width="2250" height="1500" alt="image" src="https://github.com/user-attachments/assets/d03a0fd6-a8c5-45c5-9058-c324d45d370b" />





