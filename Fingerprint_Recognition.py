import cv2
import numpy as np


def extract_fingerprint(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    max_cnt = None

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            max_cnt = cnt

    if max_cnt:
        return cv2.boundingRect(max_cnt)
    return None


def main():
    image = cv2.imread("fingerprint.jpg")
    fingerprint = extract_fingerprint(image)
    if fingerprint:
        pass
