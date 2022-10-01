import cv2
import os
import glob
import argparse
import numpy as np
from src.size_convertor import SizeConvertor


class BorderMaker:
    def make_white_canvas(self, canvas_size: int) -> np.ndarray:
        size = (canvas_size, canvas_size)
        black_img = np.zeros(size, np.uint8)
        white_img = black_img + 255
        result = cv2.cvtColor(white_img, cv2.COLOR_GRAY2BGR)
        return result

    def make_dest_path(self, img_path: str) -> str:
        org_path_dir = os.path.dirname(img_path)
        org_path_name = os.path.basename(img_path)
        dest_dir = os.path.join(org_path_dir, "bordered")
        os.makedirs(dest_dir, exist_ok=True)
        result = os.path.join(dest_dir, org_path_name)
        return result

    def main(self, img_path: str, canvas_size: int = 1500, border_size: int = 0):
        img = cv2.imread(img_path)
        canvas = self.make_white_canvas(canvas_size)
        sc = SizeConvertor()
        if sc.is_horizontal(img):
            resized_img = sc.scale_to_width(img, 1500 - border_size * 2)
            x_offset = border_size
            y_offset = 250
        else:
            resized_img = sc.scale_to_height(img, 1500 - border_size * 2)
            x_offset = 250
            y_offset = border_size
        canvas[y_offset:y_offset + resized_img.shape[0], x_offset:x_offset + resized_img.shape[1]] = resized_img
        dest_path = self.make_dest_path(img_path)
        cv2.imwrite(dest_path, canvas)
