import cv2
import shutil
import matplotlib.pyplot as plt
from src.size_convertor import SizeConvertor



def test_is_horizontal():
    sc = SizeConvertor()
    img = cv2.imread("./assets/input/portrait.jpg")
    assert sc.is_horizontal(img) is False

    img = cv2.imread("./assets/input/horizontal.jpg")
    assert sc.is_horizontal(img) is True


def test_scale_to_width():
    sc = SizeConvertor()
    img_in = cv2.imread("./assets/input/portrait.jpg")
    img_out = sc.scale_to_width(img_in, 1220)
    assert img_out.shape[1] == 1220

    img_in = cv2.imread("./assets/input/horizontal.jpg")
    img_out = sc.scale_to_width(img_in, 1440)
    assert img_out.shape[1] == 1440


def test_make_dest_path(tmpdir):
    shutil.copy("./assets/input/portrait.jpg", tmpdir)
    sc = SizeConvertor()
    img_in_path = f"{tmpdir}/portrait.jpg"
    img_in_cv2 = cv2.imread(img_in_path)
    result = sc._make_dest_path(img_in_path, img_in_cv2)
    assert result == f"{tmpdir}/4000x/portrait.jpg"


def test_main(tmpdir):
    shutil.copy("./assets/input/portrait.jpg", tmpdir)
    shutil.copy("./assets/input/horizontal.jpg", tmpdir)

    sc = SizeConvertor()
    sc.main(f"{tmpdir}/portrait.jpg")
    sc.main(f"{tmpdir}/horizontal.jpg")

    assert cv2.imread(f"{tmpdir}/1220x/portrait.jpg") is not None
    assert cv2.imread(f"{tmpdir}/1440x/horizontal.jpg") is not None

