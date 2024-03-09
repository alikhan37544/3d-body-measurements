import cv2


def detect_objects(frame):
    """
    Detects objects in the given frame. This placeholder function
    just draws a fixed rectangle on the frame.

    :param frame: The video frame from the webcam.
    :return: Tuple of the modified frame with detected objects highlighted and detection data.
    """
    # Example: Draw a fixed rectangle to simulate detection
    # You might want to replace this with actual object detection logic
    start_point = (50, 50)  # Top left corner of the rectangle
    end_point = (200, 200)  # Bottom right corner of the rectangle
    color = (0, 255, 0)  # Green color in BGR
    thickness = 2  # Thickness of the rectangle border

    # Draw the rectangle on the frame
    cv2.rectangle(frame, start_point, end_point, color, thickness)

    # Placeholder for detection data
    # This could be bounding box coordinates, class labels, confidence scores, etc.
    detections = {'bbox': (start_point, end_point),
                  'label': 'object', 'confidence': 0.8}

    return frame, detections
