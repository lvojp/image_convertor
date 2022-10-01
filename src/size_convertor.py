import cv2
import os
import glob
import argparse


class SizeConvertor:
    def is_horizontal(self, img: cv2) -> bool:
        return img.shape[0] < img.shape[1]

    def scale_to_width(self, img: cv2, width: int) -> cv2:
        """幅が指定した値になるように、アスペクト比を固定して、リサイズする。
        """
        h, w = img.shape[:2]
        height = round(h * (width / w))
        result = cv2.resize(img, dsize=(width, height))
        return result

    def scale_to_height(self, img: cv2, height: int) -> cv2:
        """高さが指定した値になるように、アスペクト比を固定して、リサイズする。
        """
        h, w = img.shape[:2]
        width = round(w * (height / h))
        result = cv2.resize(img, dsize=(width, height))
        return result

    def make_dest_path(self, img_path: str, cv2_img: cv2) -> str:
        org_path_dir = os.path.dirname(img_path)
        org_path_name = os.path.basename(img_path)
        width = cv2_img.shape[1]
        dest_dir = os.path.join(org_path_dir, f"{width}x")
        os.makedirs(dest_dir, exist_ok=True)
        result = os.path.join(dest_dir, org_path_name)
        return result

    def main(self, img_path: str, horizontal_width: int = 1440, portrait_width: int = 1220) -> None:
        cv2_img = cv2.imread(img_path)
        if self.is_horizontal(cv2_img):
            resized_cv2_img = self.scale_to_width(cv2_img, width=horizontal_width)
        else:
            resized_cv2_img = self.scale_to_width(cv2_img, width=portrait_width)
        dest_path = self.make_dest_path(img_path, resized_cv2_img)
        cv2.imwrite(dest_path, resized_cv2_img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='auto resize images, each horizontal image and portrait image.')
    parser.add_argument('-path', '--img_path_dir', required=True, type=str, help='image path directory')
    parser.add_argument('-hw', '--horizontal_width', type=int, help='horizontal image width')
    parser.add_argument('-pw', '--portrait_width', type=int, help='portrait image width')
    args = parser.parse_args()
    dir_path = args.img_path_dir
    hw = args.horizontal_width
    pw = args.portrait_width

    sc = SizeConvertor()
    available_extends = ["jpg", "jpeg", "png"]
    for ext in available_extends:
        for img_path in glob.glob(f"{dir_path}/*.{ext}"):
            print('resize:', img_path)
            if hw is not None and pw is not None:
                sc.main(img_path, horizontal_width=hw, portrait_width=pw)
            elif hw is not None:
                sc.main(img_path, horizontal_width=hw)
            elif pw is not None:
                sc.main(img_path, portrait_width=pw)
            else:
                sc.main(img_path)
            print('finish:', img_path)
