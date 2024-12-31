import sys
import os
import cv2
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import load_images


def apply_filter_sequential(image_path: str):

    images = load_images(image_path)
    output_dir = os.path.join(image_path, "output_sequential")
    os.makedirs(output_dir, exist_ok=True)

    for img_path in images:
        img = cv2.imread(img_path)
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        output_path = os.path.join(output_dir, os.path.basename(img_path))
        cv2.imwrite(output_path, blurred)
