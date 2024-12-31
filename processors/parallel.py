import sys
import os
import cv2
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import load_images
from multiprocessing import Pool


def apply_filter(image_path: str):
    img = cv2.imread(image_path)
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    output_path = image_path.replace("person", "person/output_parallel")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, blurred)

def apply_filter_parallel(image_path: str):

    images = load_images(image_path)
    os.makedirs(os.path.join(image_path, "output_parallel"), exist_ok=True)
    with Pool() as pool:
        pool.map(apply_filter, images)

