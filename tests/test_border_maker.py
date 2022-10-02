import shutil
import cv2
from src.border_maker import BorderMaker


def test_make_white_canvas():
    bm = BorderMaker()
    white_img = bm._make_white_canvas(1500)
    assert white_img.shape == (1500, 1500, 3)


def test_get_correct_margin():
    bm = BorderMaker()
    canvas = bm._make_white_canvas(1500)
    img = cv2.imread("./assets/input/portrait.jpg")
    resized_img = bm._make_resized_picture(img, 150)
    x, y = bm._get_correct_margin(canvas, resized_img)
    assert x == 350
    assert y == 150



def test_main(tmpdir):
    shutil.copy("./assets/input/portrait.jpg", tmpdir)
    shutil.copy("./assets/input/horizontal.jpg", tmpdir)
    bm = BorderMaker()
    bm.main(f"{tmpdir}/portrait.jpg", 1500, 150)
    bm.main(f"{tmpdir}/horizontal.jpg", 1500, 150)

    assert cv2.imread(f"{tmpdir}/bordered/portrait.jpg") is not None
    assert cv2.imread(f"{tmpdir}/bordered/horizontal.jpg") is not None
