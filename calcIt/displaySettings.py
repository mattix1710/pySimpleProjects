from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

def setDisplayLabel(label: QLabel, customSettings = None, cancel = False):
    if cancel:
        label.setText("0")
        
    label.setFont(QFont("Lato", 30))
    label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight)
    
    settings = "border: 2px solid grey; background-color: rgba(199, 199, 199, 0.479); color: black;"
    
    if customSettings:
        settings += " " + customSettings
    
    label.setStyleSheet(settings)