# standard number of imports

from PyQt6.QtWidgets import QApplication
import sys

import windowInit
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""QPushButton{
                            color: red;
                            min-height: 60px;
                    }""")

    window = windowInit.MainWindow()
    window.show()
    sys.exit(app.exec())