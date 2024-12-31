import os
import cv2
from typing import List

def load_images(image_path: str) -> List[str]:

    return [os.path.join(image_path, file) for file in os.listdir(image_path) if file.endswith(('.jpg', '.jpeg', '.png'))]
