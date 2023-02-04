import os
from PIL import Image, ImageFilter, ImageQt
from PyQt6 import QtGui

def pil2pixmap(im_dir: str):
    im = Image.open(im_dir)
    
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap