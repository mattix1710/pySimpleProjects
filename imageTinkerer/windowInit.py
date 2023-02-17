from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QPushButton, QFileDialog, QHBoxLayout, QStackedLayout, QSlider, QSizePolicy
from PyQt6.QtCore import Qt, QSize, QStandardPaths
from PyQt6 import QtGui
from functools import partial
import sys
import os
from pathlib import Path
from PIL import Image
# import math

import functions

# from PIL import Image, ImageFilter

HEIGHT_LABEL = 200

class MainWindow(QWidget):
    
    img_pix = ""      # Image variable
    img_PIL = ""
    img_PIL_TEMP = ""
    
    file_selected = False
    
    ############################
    #------- Qt objects -------#
    ############################
    img_disp = ""
    
    # OPTIONS widgets
    optionsPack = []
    butt_blur = ""
    butt_crop = ""
    
    def __init__(self):
        super().__init__()
        self.resize(1280, 720)
        self.setWindowTitle("ImageCreator")
        
        self.UILayouts()
        
        # self.showMaximized()
        
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        # print("Hello")
        # self.img = self.img.scaled(self.img_disp.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        return super().resizeEvent(a0)    
    
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
        self.butt_blur = QPushButton("Blur image")
        self.butt_blur.setStyleSheet("padding: 0px 20px; font-size: 20px;")
        self.butt_crop = QPushButton("Crop image")
        self.butt_crop.setStyleSheet("padding: 0px 20px; font-size: 20px;")
        
        self.butt_blur.clicked.connect(partial(self.changeSettingsOptions, 1))
        self.butt_crop.clicked.connect(partial(self.changeSettingsOptions, 2))
        
        layout.addWidget(self.butt_blur)
        layout.addWidget(self.butt_crop)

        self.optionsPack.append(self.butt_blur)
        self.optionsPack.append(self.butt_crop)

        self.setOptions(self.optionsPack)
        
        
    def settingsLayout(self, layout: QStackedLayout):
        disp_none = QLabel(self)
        disp_none.setStyleSheet("background-color: #c1c1c1;")
        
        # SETTINGS_1
        option_1_container = QWidget()
        option_1_layout = QVBoxLayout(option_1_container)
        # disp_option_1 = QLabel("BLUR")
        # disp_option_1.setStyleSheet("font-size: 30px; color: green; font-weight:500; border: 2px solid;")
        disp_option_1 = QPushButton("BLUR image")
        disp_option_1.clicked.connect(partial(self.settingsBlurImage))
        
        disp_slider_1 = QSlider(Qt.Orientation.Horizontal)
        disp_slider_1.setTickPosition(QSlider.TickPosition.TicksAbove)
        
        # SETTINGS_2
        disp_option_2 = QLabel("CROP")
        disp_option_2.setStyleSheet("font-size: 30px; color: blue; font-weight:500; border: 2px solid;")
        
        layout.addWidget(disp_none)
        option_1_layout.addWidget(disp_option_1)
        option_1_layout.addWidget(disp_slider_1)
        layout.addWidget(option_1_container)
        
        # layout.addWidget(disp_option_1)
        layout.addWidget(disp_option_2)
        
    def imageDisplayLayout(self, layout: QVBoxLayout):
        img_label = QLabel(self)
        img_label.setMaximumHeight(30)
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_label.setStyleSheet("border: 2px solid;")
        img_label.setText("No image selected")
        
        self.img_disp = QLabel(self)
        self.img_disp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # buttons section
        butt_img_reset = QPushButton("Clear the selection")
        butt_img_reset.clicked.connect(partial(self.clearTheImage, img_label, butt_img_reset))
        butt_img_reset.hide()       # hide this button by default before choosing an image
        
        butt_open_file = QPushButton("Open file")
        butt_open_file.clicked.connect(partial(self.chooseImage, img_label, self.img_disp, butt_img_reset))
        
        # managing layout
        layout.addWidget(butt_open_file)
        layout.addWidget(img_label)
        layout.addWidget(self.img_disp)
        layout.addWidget(butt_img_reset)
        
        
    #===============================================
    # the rest of class methods
    
    def chooseImage(self, label: QLabel, image: QLabel, butt_reset: QPushButton):
        try:
            file = QFileDialog.getOpenFileName(self,
                                                "Opening image",
                                                filter="Image files (*.jpg *.png);;All files (*.*)",
                                                directory=QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation))
            
            file_name = Path(file[0]).name
            self.img_PIL = Image.open(file[0])
            self.img_pix = functions.pil2pixmap(self.img_PIL)
            
            label.setText(str(file_name))
            # image.setPixmap(self.img.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatio))
            
            # if image size is greater than current window size - resize it:
            if functions.greaterThan(self.img_pix.size(), image.size()):
                self.img_pix = self.img_pix.scaled(image.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            
            image.setPixmap(self.img_pix)
            butt_reset.show()
            self.file_selected = True
            self.setOptions(self.optionsPack)
            
            
        # catch exception - e.g. while image selection window was closed before choosing a file
        except AttributeError:
            print("DEBUG: image selection aborted!")
            
    def clearTheImage(self, label: QLabel, butt_reset: QPushButton):
        self.img_disp.clear()
        butt_reset.hide()
        label.setText("No image selected")
        
    def changeSettingsOptions(self, currIndex: int):
        self.settings_layout.setCurrentIndex(currIndex)
        
    def settingsBlurImage(self):
        self.img_pix, self.img_PIL_TEMP = functions.imageBlur(self.img_PIL)
        self.img_disp.setPixmap(self.img_pix)
        
    def setOptions(self, buttons: list):
        print("BUTTONS here:")
        for butt in buttons:
            print(butt)
            butt.setEnabled(self.file_selected)