from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from functools import partial
import sys
import os
# import math

import functions

# from PIL import Image, ImageFilter

HEIGHT_LABEL = 200

class MainWindow(QWidget):
    
    img = ""      # Image variable
    
    def __init__(self):
        super().__init__()
        self.resize(1280, 720)
        self.setWindowTitle("ImageCreator")
        
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        img_label = QLabel(self)
        img_label.resize(self.width(), HEIGHT_LABEL)
        
        butt_open_file = QPushButton("Open file")
        butt_open_file.clicked.connect(partial(self.chooseImage, img_label))
        
        main_layout.addWidget(butt_open_file)
        main_layout.addWidget(img_label)
        
    #-----------------------------------------------
    # the rest of class methods
        
    def chooseImage(self, label: QLabel):
        file = QFileDialog.getOpenFileName(self,
                                               "Opening image",
                                               filter="Image files (*.jpg *.png);;All files (*.*)")
        self.img = functions.pil2pixmap(file[0])
        label.setPixmap(self.img.scaled(label.size(), Qt.AspectRatioMode.IgnoreAspectRatio))
        
        