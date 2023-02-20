from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QPushButton, QFileDialog, QHBoxLayout, QStackedLayout, QSlider, QSizePolicy, QScrollArea
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
    
    img_pix = ""        # current image variable (QPixmap)
    img_PIL = ""        # original image
    img_PIL_TEMP = ""   # image with processed operations applied
    img_name = ""       # image name (its file name)
    img_orig_size = []
    img_size_factor = 1.0
    
    file_selected = False
    
    ############################
    #------- Qt objects -------#
    ############################
    img_disp = ""
    
    # OPTIONS widgets
    optionsPack = []
    butt_blur = ""
    butt_crop = ""
    butt_enlarge_img = ""
    butt_decrease_img = ""
    
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
        
        # TODO: insert settingsLayout into QWidget()!
        
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
        self.butt_blur.setStyleSheet("padding: 0px 20px; font-size: 20px; min-height: 60px;")
        self.butt_crop = QPushButton("Crop image")
        self.butt_crop.setStyleSheet("padding: 0px 20px; font-size: 20px; min-height: 60px;")
        
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
        # image label - displays its name
        img_label = QLabel(self)
        img_label.setMaximumHeight(30)
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        img_label.setStyleSheet("border: 2px solid;")
        img_label.setText("No image selected")
        
        SIZE_BUTTON_STYLESHEET = """:enabled { 
                                            background-color: #DEDEDE;
                                            height: 30px}
                                        :disabled {
                                            background-color: #A0004500;
                                            height: 30px;
                                            color: #80000000
                                        }
        """
        
        self.butt_enlarge_img = QPushButton("+")
        self.butt_enlarge_img.clicked.connect(partial(self.changeImageSize, "enlarge"))
        self.butt_enlarge_img.setStyleSheet(SIZE_BUTTON_STYLESHEET)
        self.butt_decrease_img = QPushButton("-")
        self.butt_decrease_img.clicked.connect(partial(self.changeImageSize, "decrease"))
        self.butt_decrease_img.setStyleSheet(SIZE_BUTTON_STYLESHEET)
        
        self.optionsPack.append(self.butt_enlarge_img)
        self.optionsPack.append(self.butt_decrease_img)
        self.setOptions(self.optionsPack)
        
        label_img_container = QWidget()
        label_img_layout = QHBoxLayout()
        label_img_container.setMaximumSize(1000, 50)
        label_img_container.setLayout(label_img_layout)
        label_img_layout.addWidget(img_label)
        label_img_layout.addWidget(self.butt_enlarge_img)
        label_img_layout.addWidget(self.butt_decrease_img)
        
        # display image through QLabel
        scroll_img_area = QScrollArea()
        scroll_img_area.setWidgetResizable(True)
        # scroll_img_area.setBackgroundRole(QtGui.QPalette)
        
        self.img_disp = QLabel(self)
        self.img_disp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_img_area.setWidget(self.img_disp)
        
        # buttons section
        butt_img_reset = QPushButton("Clear the selection")
        butt_img_reset.clicked.connect(partial(self.clearTheImage, img_label, butt_img_reset))
        butt_img_reset.hide()       # hide this button by default before choosing an image
        
        butt_open_file = QPushButton("Open file")
        butt_open_file.clicked.connect(partial(self.chooseImage, img_label, self.img_disp, butt_img_reset))
        
        # managing layout
        layout.addWidget(butt_open_file)
        layout.addWidget(label_img_container)
        # layout.addWidget(self.img_disp)
        layout.addWidget(scroll_img_area)
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
            self.img_PIL_TEMP = self.img_PIL
            self.img_orig_size = [int(self.img_PIL.width), int(self.img_PIL.height)]
            
            self.img_pix = functions.pil2pixmap(self.img_PIL)
            
            self.img_name = str(file_name)
            label.setText(self.img_name)
            # image.setPixmap(self.img.scaled(label.size(), Qt.AspectRatioMode.KeepAspectRatio))
            
            # if image size is greater than current window size - resize it:
            if functions.greaterThan(self.img_pix.size(), image.size()):
                self.img_pix = self.img_pix.scaled(image.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
                curr_img_size = self.img_pix.size()
                self.img_size_factor = functions.setCurrentScaleFactor(self.img_orig_size, curr_img_size)
            
            image.setPixmap(self.img_pix)
            butt_reset.show()
            self.file_selected = True
            self.setOptions(self.optionsPack)
            
            
        # catch exception - e.g. while image selection window was closed before choosing a file
        except AttributeError:
            print("DEBUG: image selection aborted!")
            
    def clearTheImage(self, label: QLabel, butt_reset: QPushButton):
        self.img_disp.clear()
        self.img_pix = ""
        self.img_PIL = ""
        self.img_PIL_TEMP = ""
        self.img_name = ""
        self.img_size_factor = 1
        self.img_orig_size = []
        self.file_selected = False
        self.setOptions(self.optionsPack)
        butt_reset.hide()
        label.setText("No image selected")
        
    def changeSettingsOptions(self, currIndex: int):
        self.settings_layout.setCurrentIndex(currIndex)
        
    def settingsBlurImage(self):
        self.img_pix, self.img_PIL_TEMP = functions.imageBlur(self.img_PIL_TEMP)
        self.img_disp.setPixmap(self.img_pix)
        
    def setOptions(self, buttons: list):
        print("BUTTONS here:")
        for butt in buttons:
            print(butt)
            butt.setEnabled(self.file_selected)
    
    def changeImageSize(self, option):
        # TODO: RETHINK setting scale factor values
        # f.e. for large images, when initial scale is around 13% scaling with initial 5% UP or DOWN gives:
        # 13% + 5% = 18%        <-- image much larger ~ x1,38
        # 13% - 5% = 8%         <-- image much smaller ~ x0,61
        
        if option == 'enlarge':
            self.img_size_factor += 0.05
        elif option == 'decrease':
            self.img_size_factor -= 0.05
            
        self.img_pix = functions.rescaleImage(self.img_PIL_TEMP, functions.multiplyListInt(self.img_orig_size, self.img_size_factor))
        
        self.img_disp.setPixmap(self.img_pix)