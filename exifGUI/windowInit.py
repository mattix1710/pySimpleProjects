from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QPushButton, QFileDialog, QHBoxLayout, QStackedLayout, QSlider, QSizePolicy, QScrollArea
from PyQt6.QtCore import Qt, QSize, QStandardPaths
from PyQt6 import QtGui, uic

from PyQt6 import QtWidgets as widget
from PyQt6 import QtGui

from functools import partial

# local imports
import gui, functions, strings

class MainWindow(widget.QMainWindow):
    
    ############################
    #------- Qt objects -------#
    ############################
    
    # state FLAGS
    file_set = False
    
    
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
        
        table_font = QtGui.QFont()
        table_font.setPointSize(11)
        table_font.setFamily("Roboto")
        self.ui.table.setFont(table_font)
        
        # self.ui.table.setStyleSheet("{color: #149414}")
        
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, widget.QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, widget.QHeaderView.ResizeMode.Stretch)
        
        
        # MENU
        # enable when the file was loaded
        self.ui.action_theme_table_choose_font_color.triggered.connect(self.table_font_color)
        self.ui.action_theme_table_font_hacker_green.triggered.connect(partial(self.table_font_color, "hacker"))
        self.ui.action_theme_table_font_white.triggered.connect(partial(self.table_font_color, "white"))
        self.ui.menu_theme_table.setEnabled(False)
            
    def read_file(self):
        try:
            meta_list = functions.read_metafile()
            
            self.ui.table.setRowCount(len(meta_list))
        
            for el, counter in zip(meta_list, range(len(meta_list))):
                
                parameter_item = widget.QTableWidgetItem(el[0])
                parameter_item.setForeground(QtGui.QBrush(QtGui.QColor(strings.font_color_hacker)))
                
                data_item = widget.QTableWidgetItem(el[1])
                data_item.setForeground(QtGui.QBrush(QtGui.QColor(strings.font_color_hacker)))
                
                self.ui.table.setItem(counter, 0, parameter_item)
                self.ui.table.setItem(counter, 1, data_item)
                
            self.file_set = True
            self.ui.menu_theme_table.setEnabled(True)
            
        except TypeError:
            # if there was an error concerning the subprocess (wrong file was chosen)
            # raise bad fileyype error dialog
            msg_error = widget.QMessageBox()
            msg_error.setWindowTitle(strings.msg_title_warning)
            msg_error.setIcon(widget.QMessageBox.Icon.Warning)
            msg_error.setText(strings.msg_error_bad_file_type)
            msg_error.setInformativeText(strings.msg_error_bad_file_type_desc)
            msg_error.setStandardButtons(widget.QMessageBox.StandardButton.Ok)
            
            msg_error.exec()
        except ValueError:
            # if there was an error concerning the file choosing cancelling
            # raise cancellation dialog
            msg_cancellation = widget.QMessageBox()
            msg_cancellation.setWindowTitle(strings.msg_title_info)
            msg_cancellation.setIcon(widget.QMessageBox.Icon.Information)
            msg_cancellation.setText(strings.msg_file_cancellation)
            msg_cancellation.setInformativeText(strings.msg_file_cancellation_desc)
            msg_cancellation.setStandardButtons(widget.QMessageBox.StandardButton.Ok)
            
            msg_cancellation.exec()
        else:
            self.file_set = False

    def table_font_color(self, specific_color: str = ""):
        color = QtGui.QColor("#FFFFFF")
        
        if specific_color == "":
            color = functions.color_picker()
        else:
            color = QtGui.QColor(functions.switch_color(specific_color))
        
        # for each item in the table, change font color
        for row in range(self.ui.table.rowCount()):
            for col in range(self.ui.table.columnCount()):
                self.ui.table.item(row, col).setForeground(QtGui.QBrush(color))