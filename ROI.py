import cv2
import numpy as np

# https://blog.electroica.com/select-roi-or-multiple-rois-bounding-box-in-opencv-python/

# 'androidparty.png'

def ROI(img_path):
    img = cv2.imread(img_path)
    roi = cv2.selectROI(img)
    print(roi)
    return roi

if __name__ == '__main__':
    ROI('androidparty.png')