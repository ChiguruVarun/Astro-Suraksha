from ultralytics import YOLO

def evaluate_model():
    """
    Loads a trained YOLOv8 model and evaluates its performance on the test set.
    """
    # 1. Load the best-performing trained model weights
    # This path points to the 'best.pt' file saved during training
    model = YOLO('C:/Users/chigu/OneDrive/Desktop/hackathon/runs/detect/yolov8_custom_training4/weights/best.pt')
    
    # 2. Run the evaluation
    # The 'val' mode automatically calculates all key metrics and saves them.
    results = model.val(data='config.yaml')

    # 3. Print the key metrics
    print("--- Evaluation Metrics ---")
    
    # Access the metrics directly from the results dictionary
    metrics = results.results_dict
    
    # The metrics dictionary provides the overall precision and recall as scalar values
    overall_precision = metrics['metrics/precision(B)']
    overall_recall = metrics['metrics/recall(B)']
    
    print(f"mAP@0.5: {metrics['metrics/mAP50(B)']:.3f}")
    
    print(f"Precision: {overall_precision:.3f}")
    print(f"Recall: {overall_recall:.3f}")

if __name__ == '__main__':
    evaluate_model()