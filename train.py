from ultralytics import YOLO

# Load a pre-trained YOLOv8n model
model = YOLO('yolov8n.pt')

# Train the model using the configuration from the YAML file
# The 'data' argument now points to the path of your config.yaml
results = model.train(
    data='config.yaml',
    epochs=10,
    patience=4,
    imgsz=640,
    name='yolov8_custom_training'
)

print("Training completed. Results are saved.")