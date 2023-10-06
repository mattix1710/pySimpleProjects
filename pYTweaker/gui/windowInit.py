from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QPushButton, QFileDialog, QHBoxLayout, QStackedLayout, QSlider, QSizePolicy, QScrollArea
from PyQt6.QtCore import Qt, QSize, QStandardPaths
from PyQt6 import QtGui, uic

from PyQt6 import QtWidgets as widget
from PyQt6 import QtGui

import requests

import layout, functions


HEIGHT_LABEL = 200

class MainWindow(widget.QMainWindow):
    
    ############################
    #------- Qt objects -------#
    ############################
    
    # OPTIONS widgets
    element_handler = functions.VideoHandler()
    
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui  = layout.Ui_MainWindow()
        self.ui.setupUi(self)
        # uic.loadUi('gui/main.ui', self)
        
        self.UI_manager()
        self.tempo()
        
        # uic.load_ui('main.ui', self)    # loading the .ui file
        self.show()                     # show the GUI
        
    def tempo(self):
        self.ui.click_box_video.setEnabled(False)
        self.ui.click_box_audio.addItems(['96', '128', '320'])
        
        
    def UI_manager(self):
        self.ui.butt_search.clicked.connect(self.handle_inserted_text)

    def handle_inserted_text(self):
        # Check if given text is a proper URL or is there anything
        searched_text = self.ui.insert_url_edit.toPlainText()
        print(searched_text.find("https://youtu.be/"))
        
        
        # if given text is YouTube video URL
        if searched_text.find("https://youtu.be/") != -1 or searched_text.find("https://www.youtube.com/") != -1:
            # create new YouTube video object
            self.element_handler.setUrl(self.ui.insert_url_edit.toPlainText())
            self.ui.label_result.setText(self.element_handler.getTitle())

            # set thumbnail picture
            image = QtGui.QImage()
            image.loadFromData(requests.get(self.element_handler.getThumbnailPicUrl()).content)
            img_pixmap = QtGui.QPixmap(image).scaledToHeight(180, mode = Qt.TransformationMode.SmoothTransformation)#self.ui.label_md.height())
            
            self.ui.label_md.setPixmap(img_pixmap)
            
            # TODO: add elements to the list of available video download options (video and audio selection)
            return
        
        # if given text is NOT a YouTube video URL
        
        msg = widget.QMessageBox()
        msg.setIcon(widget.QMessageBox.Icon.Warning)
        msg.setText("Wrong URL has been submitted!")
        msg.setInformativeText("Video URL should have a form of:\nhttps://www.youtube.com/ or\nhttps://youtu.be/")
        
        msg.setStandardButtons(widget.QMessageBox.StandardButton.Ok)
        
        msg.exec()