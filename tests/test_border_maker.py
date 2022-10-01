import shutil
import cv2
import matplotlib.pyplot as plt
from src.border_maker import BorderMaker


def test_make_white_canvas(tmpdir):
    bm = BorderMaker()
    white_img = bm.make_white_canvas(1024)
    assert white_img.shape == (1024, 1024, 3)


def test_main(tmpdir):
    shutil.copy("./assets/input/portrait.jpg", tmpdir)
    shutil.copy("./assets/input/horizontal.jpg", tmpdir)
    bm = BorderMaker()
    bm.main(f"{tmpdir}/portrait.jpg", 1500, 150)
    bm.main(f"{tmpdir}/horizontal.jpg", 1500, 150)

    assert cv2.imread(f"{tmpdir}/bordered/portrait.jpg") is not None
    assert cv2.imread(f"{tmpdir}/bordered/horizontal.jpg") is not None
