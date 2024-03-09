import cv2


class Tracker:
    def __init__(self):
        self.tracker = cv2.TrackerCSRT_create()
        self.initialized = False

    def init(self, frame, bbox):
        """
        Initializes the tracker with the first frame and the bounding box.
        :param frame: The first frame.
        :param bbox: The bounding box (x, y, width, height).
        """
        self.tracker.init(frame, bbox)
        self.initialized = True

    def update(self, frame):
        """
        Updates the tracker with a new frame.
        :param frame: The new frame.
        :return: A tuple (success, bbox). Success is a bool indicating if the update was successful.
                bbox is the new bounding box (x, y, width, height).
        """
        if not self.initialized:
            raise Exception(
                "Tracker has not been initialized with a bounding box.")
        success, bbox = self.tracker.update(frame)
        return success, bbox
