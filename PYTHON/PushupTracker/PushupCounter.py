import cv2 as cv
import time

from PoseTracker import PoseTracker

class PushupCounter(PoseTracker):

    def __init__(self, device_index=0, min_detection_confidence=0.5, min_tracking_confidence=0.5, cam_width=1280, cam_height=800):
        
        super().__init__(
            device_index=device_index,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
            cam_width=cam_width,
            cam_height=cam_height
        )

        self.lock = False
        self.count = 0

    def putText(self):
        cv.putText(self.img, f'Pushups: {self.count}', (10,80), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

    def update_vars(self):

        left_side = self.y_distance(15, 11)
        right_side = self.y_distance(16, 12)

        if (not self.lock) and left_side < 0.2 and right_side < 0.2:
            self.count += 1
            self.lock = True

        if self.lock and left_side > 0.35 and right_side > 0.35:
            self.lock = False



if __name__ == '__main__':

    counter = PushupCounter()

    while True:
        previous_time = time.time()
        counter.detect()
        counter.update_vars()
        counter.putText()
        counter.display()
        current_time = time.time()
        fps = 1/(current_time-previous_time)
        print(f'FPS: {fps}')
        cv.waitKey(1)