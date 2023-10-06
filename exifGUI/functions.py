import subprocess
import re
from pathlib import Path

# QT
from PyQt6 import QtWidgets as widget
from PyQt6 import QtGui
from PyQt6.QtCore import QStandardPaths

import strings

def read_metafile():
    meta_list = []
    
    try:
        file_path = __choose_file()
        
        # insert message box
        # file_processing_dialog = widget.QProgressDialog("Przetwarzanie", "Zatrzymaj", 0, 2)
        
        proc = subprocess.check_output("exiftool\exiftool.exe \"{}\"".format(file_path))
        data = proc.decode('utf-8')
        group = re.findall(r"(.+): (.+)", data)

        # file_processing_dialog.setValue(1)

        for data in group:
            mini = []
            mini.append(data[0].strip())
            mini.append(data[1].strip())
            meta_list.append(mini)
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise TypeError
    except:
        raise ValueError
    
    # close message box
    # file_processing_dialog.setValue(2)
    
    return meta_list

def __choose_file():
    try:
        file = widget.QFileDialog.getOpenFileName(caption = strings.file_choice_caption,
                                                  filter = strings.file_choice_filter,
                                                  directory = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation))

        if file[0] == "":
            raise AttributeError
        file_name = Path(file[0])
        print("DEBUG_FILE:", file_name)
        return file_name
    
    # catch exception - e.g. while video selection window was closed before choosing a file
    except:
        print("DEBUG: file selection aborted!")
        raise AttributeError
    
def color_picker():
    color: QtGui.QColor = widget.QColorDialog.getColor()
    print(color.name())
    print(type(color))
    return color

def switch_color(color_name: str):
    if color_name == "hacker":
        return "#149414"
    elif color_name == "white":
        return "#FFFFFF"
    else:
        return "#FFFFFF"