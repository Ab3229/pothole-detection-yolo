from ultralytics import YOLO
import cv2

# Load model
model = YOLO("best.pt")

# Input video
cap = cv2.VideoCapture("potholes.mp4")

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create VideoWriter (output file)
out = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detection
    results = model(frame)

    # Draw boxes
    annotated_frame = results[0].plot()

    # Save frame to video
    out.write(annotated_frame)

    # Show (optional)
    cv2.imshow("Pothole Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
