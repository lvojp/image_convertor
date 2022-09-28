import cv2
import os


class SizeConvertor:
    def __init__(self, path: str) -> None:
        self.cv2_img = cv2.imread(path)

    def is_horizontal(self, img: cv2) -> bool:
        return img.shape[0] < img.shape[1]

    def scale_to_width(self, img: cv2, width: int) -> cv2:
        """幅が指定した値になるように、アスペクト比を固定して、リサイズする。
        """
        h, w = img.shape[:2]
        height = round(h * (width / w))
        result = cv2.resize(img, dsize=(width, height))
        return result

    def main(self) -> None:
        img = self.cv2_img
        if self.is_horizontal(img):
            result = self.scale_to_width(img, width=1440)
        else:
            result = self.scale_to_width(img, width=1220)
        return result


if __name__ == '__main__':
    print('test')
