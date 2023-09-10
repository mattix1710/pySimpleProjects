# standard number of imports

from PyQt6.QtWidgets import QApplication
import sys

import windowInit
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet("""QPushButton{
    #                         color: blue;
    #                         font-size: 25px;
    #                         font-weight: 500;
    #                 }""")

    window = windowInit.MainWindow()
    window.show()
    sys.exit(app.exec())