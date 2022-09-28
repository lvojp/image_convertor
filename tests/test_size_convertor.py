import cv2
import shutil
from src.size_convertor import SizeConvertor


def test_is_horizontal():
    sc = SizeConvertor()
    img = cv2.imread("./assets/size_convertor/input/portrait.jpg")
    assert sc.is_horizontal(img) is False

    img = cv2.imread("./assets/size_convertor/input/horizontal.jpg")
    assert sc.is_horizontal(img) is True


def test_scale_to_width():
    sc = SizeConvertor()
    img_in = cv2.imread("./assets/size_convertor/input/portrait.jpg")
    img_out = sc.scale_to_width(img_in, 1220)
    assert img_out.shape[1] == 1220

    img_in = cv2.imread("./assets/size_convertor/input/horizontal.jpg")
    img_out = sc.scale_to_width(img_in, 1440)
    assert img_out.shape[1] == 1440


def test_make_dest_path():
    sc = SizeConvertor()
    img_in_path = "./assets/size_convertor/input/portrait.jpg"
    img_in_cv2 = cv2.imread(img_in_path)
    result = sc.make_dest_path(img_in_path, img_in_cv2)
    print(result)
    assert result == "./assets/size_convertor/input/4000x/portrait.jpg"


def test_main(tmpdir):
    shutil.copy("./assets/size_convertor/input/portrait.jpg", tmpdir)
    shutil.copy("./assets/size_convertor/input/horizontal.jpg", tmpdir)

    sc = SizeConvertor()
    sc.main(f"{tmpdir}/portrait.jpg")
    sc.main(f"{tmpdir}/horizontal.jpg")

    assert cv2.imread(f"{tmpdir}/1220x/portrait.jpg") is not None
    assert cv2.imread(f"{tmpdir}/1440x/horizontal.jpg") is not None

