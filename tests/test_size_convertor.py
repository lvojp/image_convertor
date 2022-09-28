import cv2
from src.size_convertor import SizeConvertor


def test_is_horizontal():
    sc = SizeConvertor()
    img = cv2.imread("./assets/size_convertor/input/portrait.jpg")
    assert sc.is_horizontal(img) is False

    img = cv2.imread("./assets/size_convertor/input/horizontal.jpg")
    assert sc.is_horizontal(img) is True


def test_main():
    sc = SizeConvertor()
    # portrait
    img_in = cv2.imread("./assets/size_convertor/input/portrait.jpg")
    img_out = sc.main(img_in)
    cv2.imwrite("./assets/size_convertor/output/portrait.jpg", img_out)

    # horizontal
    img_in = cv2.imread("./assets/size_convertor/input/horizontal.jpg")
    img_out = sc.main(img_in)
    cv2.imwrite("./assets/size_convertor/output/horizontal.jpg", img_out)
