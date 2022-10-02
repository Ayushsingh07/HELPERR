import cv2 as cv
import mediapipe as mp
import time
import numpy as np

class PoseTracker:
    
    def __init__(self, device_index=0, min_detection_confidence=0.5, min_tracking_confidence=0.5, cam_width=1280, cam_height=800):
        
        self.cap = cv.VideoCapture(device_index)
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(min_detection_confidence=min_detection_confidence, min_tracking_confidence=min_tracking_confidence)
        self.cap.set(3, cam_width)
        self.cap.set(4, cam_height)

    def detect(self):
        success, self.img = self.cap.read()
        self.shape = self.img.shape
        assert success, 'Could not capture the image correctly'
        img_RGB = cv.cvtColor(self.img, cv.COLOR_BGR2RGB)

        self.results = self.pose.process(img_RGB)
        self.mp_draw.draw_landmarks(self.img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

    def display(self):
        cv.imshow('Image', self.img)

    
    def get_euclidean_distance(self, l1_index, l2_index):
        h, w, _ = self.shape

        l1 = self.results.pose_landmarks.landmark[l1_index]
        l2 = self.results.pose_landmarks.landmark[l2_index]

        l1x = l1.x * w
        l2x = l2.x * w

        l1y = l1.y * h
        l2y = l2.y * h

        distance = abs(l1x - l2x), abs(l1y - l2y)

        euclidean = np.sqrt(distance[0]**2 + distance[1]**2)
        return euclidean

    def y_distance(self, l1_index, l2_index):
        l1 = self.results.pose_landmarks.landmark[l1_index]
        l2 = self.results.pose_landmarks.landmark[l2_index]

        return abs(l1.y - l2.y)

    def x_distance(self, l1_index, l2_index):
        l1 = self.results.pose_landmarks.landmark[l1_index]
        l2 = self.results.pose_landmarks.landmark[l2_index]

        return abs(l1.x - l2.x)



if __name__ == '__main__':
    detector = PoseTracker()

    while True:
        previous_time = time.time()
        detector.detect()
        detector.display()
        current_time = time.time()
        fps = 1/(current_time-previous_time)
        print(f'FPS: {fps}')
        cv.waitKey(1)