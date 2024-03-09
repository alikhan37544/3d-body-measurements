import cv2

class CameraInput:
    def __init__(self, camera_id=0):
        """
        Initializes the camera input with the specified camera ID.
        :param camera_id: The ID for the camera device (default is 0).
        """
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(camera_id)
        if not self.cap.isOpened():
            raise ValueError("Error: Could not open webcam.")

    def get_frame(self):
        """
        Captures a single frame from the camera.
        :return: The captured frame.
        """
        ret, frame = self.cap.read()
        if not ret:
            raise ValueError("Error: Can't receive frame (stream end?).")
        return frame

    def release(self):
        """
        Releases the camera resource.
        """
        self.cap.release()

if __name__ == "__main__":
    camera = CameraInput()
    try:
        while True:
            frame = camera.get_frame()
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()