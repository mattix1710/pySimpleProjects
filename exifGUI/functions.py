import subprocess
import re
from pathlib import Path

# QT
from PyQt6 import QtWidgets as widget
from PyQt6 import QtGui
from PyQt6.QtCore import QStandardPaths

def read_metafile():
    meta_list = []
    
    file_path = __choose_file()
    
    # insert message box
    file_processing_dialog = widget.QProgressDialog("Przetwarzanie", "Zatrzymaj", 0, 2)
    
    proc = subprocess.check_output("exiftool {}".format(file_path))
    data = proc.decode('utf-8')
    group = re.findall(r"(.+): (.+)", data)

    file_processing_dialog.setValue(1)

    for data in group:
        mini = []
        mini.append(data[0].strip())
        mini.append(data[1].strip())
        meta_list.append(mini)
    
    # close message box
    file_processing_dialog.setValue(2)
    
    return meta_list

def __choose_file():
    try:
        file = widget.QFileDialog.getOpenFileName(caption = "Wybieranie pliku",
                                                  filter = "Pliki wideo (*.mp4 *.mov);; Obrazy (*.jpg *.png)",
                                                  directory = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DesktopLocation))

        file_name = Path(file[0])
        print("FILE:", file_name)
        return file_name
    
    # catch exception - e.g. while video selection window was closed before choosing a file
    except AttributeError:
        print("DEBUG: file selection aborted!")
        return "."