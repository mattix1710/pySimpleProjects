from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QPushButton, QFileDialog, QHBoxLayout, QStackedLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6 import QtGui
from functools import partial
import sys
import os
from pathlib import Path
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
        
        self.UILayouts()
        
        # self.showMaximized()
        
        
    #-----------------------------------------------
    # setting layouts
    
    def UILayouts(self):
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        
        options_layout = QVBoxLayout()
        main_layout.addLayout(options_layout)
        
        self.settings_layout = QStackedLayout()
        main_layout.addLayout(self.settings_layout)
        
        display_img_container = QWidget()
        display_img_layout = QVBoxLayout()
        display_img_container.setLayout(display_img_layout)
        display_img_container.setFixedWidth(int(self.width()*0.6))
        main_layout.addWidget(display_img_container)
        
        self.optionsLayout(options_layout)
        self.settingsLayout(self.settings_layout)
        self.imageDisplayLayout(display_img_layout)

        
    def optionsLayout(self, layout: QVBoxLayout):
        butt_blur = QPushButton("Blur image")
        butt_blur.setStyleSheet("padding: 0px 20px; font-size: 20px;")
        butt_crop = QPushButton("Crop image")
        butt_crop.setStyleSheet("padding: 0px 20px; font-size: 20px;")
        
        butt_blur.clicked.connect(partial(self.changeSettingsOptions, 1))
        butt_crop.clicked.connect(partial(self.changeSettingsOptions, 2))
        
        layout.addWidget(butt_blur)
        layout.addWidget(butt_crop)
        
        
    def settingsLayout(self, layout: QStackedLayout):
        disp_none = QLabel(self)
        disp_none.setStyleSheet("background-color: #c1c1c1;")
        
        
        disp_option_1 = QLabel("BLUR")
        disp_option_1.setStyleSheet("font-size: 30px; color: green; font-weight:500; border: 2px solid;")
        
        disp_option_2 = QLabel("CROP")
        disp_option_2.setStyleSheet("font-size: 30px; color: blue; font-weight:500; border: 2px solid;")
        
        layout.addWidget(disp_none)
        layout.addWidget(disp_option_1)
        layout.addWidget(disp_option_2)
        
    def imageDisplayLayout(self, layout: QVBoxLayout):
        img_label = QLabel(self)
        img_label.setMaximumHeight(30)
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_label.setStyleSheet("border: 2px solid;")
        
        img_disp = QLabel(self)
        img_disp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        butt_open_file = QPushButton("Open file")
        butt_open_file.clicked.connect(partial(self.chooseImage, img_label, img_disp))
        layout.addWidget(butt_open_file)
        layout.addWidget(img_label)
        layout.addWidget(img_disp)
        
        
    #===============================================
    # the rest of class methods
        
    def chooseImage(self, label: QLabel, image: QLabel):
        try:
            file = QFileDialog.getOpenFileName(self,
                                                "Opening image",
                                                filter="Image files (*.jpg *.png);;All files (*.*)")
            
            file_name = Path(file[0]).name
            self.img = functions.pil2pixmap(file[0])
            label.setText(str(file_name))
            # image.setPixmap(self.img.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatio))
            image.setPixmap(self.img)
            
            
        # catch exception - e.g. while image selection window was closed before choosing a file
        except AttributeError:
            print("DEBUG: image selection aborted!")
        
    def changeSettingsOptions(self, currIndex: int):
        self.settings_layout.setCurrentIndex(currIndex)
        