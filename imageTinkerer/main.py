# standard number of imports

from PyQt6.QtWidgets import QApplication
import sys

import windowInit
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""QPushButton{
                            color: blue;
                            font-size: 25px;
                            font-weight: 500;
                    }""")

    window = windowInit.MainWindow()
    window.show()
    sys.exit(app.exec())
    
    # TODO: dodać resizing obrazów; przemyśleć resizing okna programu
    # IDEA - resize:
    #   najpierw program odczytuje rozmiar pliku i można to dostosować do wymaganych ograniczeń, np. max 2MB, albo rozmiar obrazu
    