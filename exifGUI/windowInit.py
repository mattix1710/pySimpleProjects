from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QPushButton, QFileDialog, QHBoxLayout, QStackedLayout, QSlider, QSizePolicy, QScrollArea
from PyQt6.QtCore import Qt, QSize, QStandardPaths
from PyQt6 import QtGui, uic

from PyQt6 import QtWidgets as widget
from PyQt6 import QtGui

import gui, functions

class MainWindow(widget.QMainWindow):
    
    ############################
    #------- Qt objects -------#
    ############################
    
    # OPTIONS widgets
    
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui  = gui.Ui_ExifGUI()
        self.ui.setupUi(self)
        # uic.loadUi('gui/main.ui', self)
        
        self.UI_manager()
        self.show()                     # show the GUI
        
    def UI_manager(self):
        # palette = QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.window, "blue")
        # self.setStyleSheet("background-color: #A0A0A0;")
        
        #===================================
        # connect buttons to their functions
        #===================================
        self.ui.butt_metadata.clicked.connect(self.read_file)
        
        #===================================
        ## populate table with initial data
        #===================================
        # disable cell editing
        self.ui.table.setEditTriggers(widget.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.table.setColumnCount(2)
        self.ui.table.setHorizontalHeaderLabels(["Parametr", "Dane"])
        
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, widget.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, widget.QHeaderView.ResizeMode.Stretch)
            
    def read_file(self):
        meta_list = functions.read_metafile()
        
        # TODO: add try except while got no elements in the list...
        
        self.ui.table.setRowCount(len(meta_list))
        
        for el, counter in zip(meta_list, range(len(meta_list))):
            self.ui.table.setItem(counter, 0, widget.QTableWidgetItem(el[0]))
            self.ui.table.setItem(counter, 1, widget.QTableWidgetItem(el[1]))
            
    