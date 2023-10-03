from PyQt6.QtWidgets import QApplication
import sys

import windowInit
import subprocess
import re
        
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


# proc = subprocess.check_output("exiftool porwaniekm.mov")

# data = proc.decode('utf-8')
# # print(type(proc))

# group = re.findall(r"(.+): (.+)", data)

# meta_list = []

# for data in group:
#     mini = []
#     mini.append(data[0].strip())
#     mini.append(data[1].strip())
#     meta_list.append(mini)