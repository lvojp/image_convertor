import cv2
import os
import glob
import argparse
import numpy as np
from size_convertor import SizeConvertor
from typing import Tuple

CANVAS_SIZE = 1500

class BorderMaker:
    def __init__(self):
        self.sc = SizeConvertor()

    def _make_white_canvas(self, canvas_size: int) -> np.ndarray:
        size = (canvas_size, canvas_size)
        black_img = np.zeros(size, np.uint8)
        white_img = black_img + 255
        result = cv2.cvtColor(white_img, cv2.COLOR_GRAY2BGR)
        return result

    def _make_dest_path(self, img_path: str) -> str:
        org_path_dir = os.path.dirname(img_path)
        org_path_name = os.path.basename(img_path)
        dest_dir = os.path.join(org_path_dir, "bordered")
        os.makedirs(dest_dir, exist_ok=True)
        result = os.path.join(dest_dir, org_path_name)
        return result

    def _make_resized_picture(self, img: cv2, border_size: int = 0) -> np.ndarray:
        if self.sc.is_horizontal(img):
            result = self.sc.scale_to_width(img, CANVAS_SIZE - border_size * 2)
        else:
            result = self.sc.scale_to_height(img, CANVAS_SIZE - border_size * 2)
        return result

    def _get_correct_margin(self, canvas: cv2, img: cv2) -> Tuple[int, int]:
        canvas_height, canvas_width, _ = canvas.shape
        img_height, img_width, _ = img.shape
        margin_x = (canvas_width - img_width) // 2
        margin_y = (canvas_height - img_height) // 2
        return margin_x, margin_y

    def main(self, img_path: str, canvas_size: int = CANVAS_SIZE, border_size: int = 0):
        try:
            img = cv2.imread(img_path)
            canvas = self._make_white_canvas(canvas_size)
            resized_img = self._make_resized_picture(img, border_size)
            margin_x, margin_y = self._get_correct_margin(canvas, resized_img)
            canvas[margin_y:margin_y + resized_img.shape[0], margin_x:margin_x + resized_img.shape[1]] = resized_img
            dest_path = self._make_dest_path(img_path)
            cv2.imwrite(dest_path, canvas)
        except Exception as e:
            raise Exception(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Make border to images")
    parser.add_argument("-d", "--img_dir", required=True, type=str, help="Image path directory")
    parser.add_argument("-s", "--img_size", type=int, default=1500, help="Size of image")
    parser.add_argument("-bs", "--border_size", type=int, default=20, help="Size of border")
    args = parser.parse_args()
    dir_path = args.img_dir
    img_size = args.img_size
    border_size = args.border_size
    try:
        available_extensions = ["jpg", "jpeg", "png"]
        for ext in available_extensions:
            for img_path in glob.glob(f"{dir_path}/*.{ext}"):
                print(f"Processing {img_path}")
                bm = BorderMaker()
                if img_size is not None and border_size is not None:
                    bm.main(img_path, canvas_size=img_size, border_size=border_size)
                elif img_size is not None:
                    bm.main(img_path, canvas_size=img_size)
                elif border_size is not None:
                    bm.main(img_path, border_size=border_size)
                else:
                    bm.main(img_path)
                print(f"Done")
    except Exception as e:
        print("Something went wrong: ", e)
