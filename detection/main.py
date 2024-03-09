import cv2
from camera_input import CameraInput
import object_detection as od
from tracking import Tracker
from repetition_counting import RepetitionCounter


def main():
    # Initialize Camera
    camera = CameraInput()

    # Initialize Tracker and Rep Counter
    tracker = Tracker()
    rep_counter = RepetitionCounter()

    # Flag to indicate if we're currently tracking an object
    tracking_active = False

    try:
        while True:
            frame = camera.get_frame()

            # If not currently tracking, try to detect object and initialize tracker
            if not tracking_active:
                frame, detections = od.detect_objects(frame)
                if detections:
                    # For simplicity, let's assume detections['bbox'] gives us the bounding box
                    bbox = detections['bbox']
                    tracker.init(frame, bbox)
                    tracking_active = True
                    print("Tracking initialized.")
                else:
                    cv2.imshow("Frame", frame)
            else:
                # Update tracking and draw bounding box
                success, bbox = tracker.update(frame)
                if success:
                    p1 = (int(bbox[0]), int(bbox[1]))
                    p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                    cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)

                    # Simple rep counting based on object's vertical movement
                    # Here, we just use the Y coordinate (bbox[1]) of the bounding box
                    rep_counter.update(bbox[1])
                    print(f"Reps: {rep_counter.get_reps()}")

                cv2.imshow("Frame", frame)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
