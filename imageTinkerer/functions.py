import os
from PIL import Image, ImageFilter, ImageQt
from PyQt6 import QtGui
from PyQt6.QtCore import QSize

def pil2pixmap(im: Image):
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

def greaterThan(obj1: QSize, obj2: QSize):
    if obj1.width() > obj2.width() or obj1.height() > obj2.height():
        return True
    return False

def imageBlur(inImg: Image):
    img_processed = inImg.filter(ImageFilter.GaussianBlur(3))
    img_pix = pil2pixmap(img_processed)
    return img_pix, img_processed