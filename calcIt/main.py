# standard number of imports

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("SimplyCalcIt")
        # self.setWindowIcon(QIcon(".png"))
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label = QLabel("Simple calculator")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())