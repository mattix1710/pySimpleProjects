from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QPushButton
from PyQt6.QtCore import Qt
from functools import partial
import math

import displaySettings

NOT_DECIMAL = -1

class MainWindow(QWidget):
    OPERATIONS = {
        "none": 0,
        "addition": 1,
        "subtraction": 2,
        "multiplication": 3,
        "division": 4
    }
    
    memory = 0.0
    num_saved = 0.0
    curr_op = OPERATIONS["none"]
    
    def set_memory(self, num):
        print("curr:", self.memory)
        self.memory = num
        print("neww:", self.memory)
    
    def __init__(self):
        super().__init__()
        self.resize(320, 500)
        self.setWindowTitle("SimplyCalcIt")
        # self.setWindowIcon(QIcon(".png"))
        
        layout = QVBoxLayout()
        # self.setLayout(layout)
        
        label = QLabel("Simple calculator")
        # label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # layout.addWidget(label)
        
        ###########
        # button GRID -> 4x6
        #
        layout_buttons = QGridLayout()
        self.setLayout(layout_buttons)
        
        # init buttons
        butt_num_0 = QPushButton("0")
        butt_num_1 = QPushButton("1")
        butt_num_2 = QPushButton("2")
        butt_num_3 = QPushButton("3")
        butt_num_4 = QPushButton("4")
        butt_num_5 = QPushButton("5")
        butt_num_6 = QPushButton("6")
        butt_num_7 = QPushButton("7")
        butt_num_8 = QPushButton("8")
        butt_num_9 = QPushButton("9")
        butt_num_dot = QPushButton(".")
        butt_op_div = QPushButton("/")
        butt_op_mul = QPushButton("*")
        butt_op_add = QPushButton("+")
        butt_op_sub = QPushButton("-")
        butt_cancel = QPushButton("C")
        butt_memory = QPushButton("M")
        butt_recall = QPushButton("R")
        butt_delete = QPushButton("Del")
        butt_result = QPushButton("=")
        
        butt_cancel.setStyleSheet("background-color: rgba(177, 53, 53, 0.8); color: white; font-weight: 700; font-size: 30px;")
        
        label_result_display = QLabel("0")
        label_result_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        label_result_display.setMaximumHeight(100)
        displaySettings.setDisplayLabel(label_result_display, cancel=True)
        
        ################################################
        # connecting buttons to its managing functions
        butt_num_0.clicked.connect(partial(self.but_number_pressed, butt_num_0.text(), label_result_display))
        butt_num_1.clicked.connect(partial(self.but_number_pressed, butt_num_1.text(), label_result_display))
        butt_num_2.clicked.connect(partial(self.but_number_pressed, butt_num_2.text(), label_result_display))
        butt_num_3.clicked.connect(partial(self.but_number_pressed, butt_num_3.text(), label_result_display))
        butt_num_4.clicked.connect(partial(self.but_number_pressed, butt_num_4.text(), label_result_display))
        butt_num_5.clicked.connect(partial(self.but_number_pressed, butt_num_5.text(), label_result_display))
        butt_num_6.clicked.connect(partial(self.but_number_pressed, butt_num_6.text(), label_result_display))
        butt_num_7.clicked.connect(partial(self.but_number_pressed, butt_num_7.text(), label_result_display))
        butt_num_8.clicked.connect(partial(self.but_number_pressed, butt_num_8.text(), label_result_display))
        butt_num_9.clicked.connect(partial(self.but_number_pressed, butt_num_9.text(), label_result_display))
        
        butt_cancel.clicked.connect(partial(self.but_clear_pressed, label_result_display))
        butt_delete.clicked.connect(partial(self.but_delete_pressed, label_result_display))
        butt_num_dot.clicked.connect(partial(self.but_decimal_pressed, label_result_display))
        butt_memory.clicked.connect(partial(self.but_memory_pressed, label_result_display))
        
        butt_recall.clicked.connect(partial(self.but_recall_pressed, label_result_display))
        
        butt_op_add.clicked.connect(partial(self.operation_addition, label_result_display))
        butt_result.clicked.connect(partial(self.operation_result, label_result_display))
        
        
        
        ###########################
        # adding widgets to layout
        layout_buttons.addWidget(label_result_display, 0, 0, 1, -1)
        
        layout_buttons.addWidget(butt_cancel, 1, 0)
        layout_buttons.addWidget(butt_memory, 1, 1)
        layout_buttons.addWidget(butt_recall, 1, 2)
        layout_buttons.addWidget(butt_op_div, 1, 3)
        
        layout_buttons.addWidget(butt_num_7, 2, 0)
        layout_buttons.addWidget(butt_num_8, 2, 1)
        layout_buttons.addWidget(butt_num_9, 2, 2)
        layout_buttons.addWidget(butt_op_mul, 2, 3)
        
        layout_buttons.addWidget(butt_num_4, 3, 0)
        layout_buttons.addWidget(butt_num_5, 3, 1)
        layout_buttons.addWidget(butt_num_6, 3, 2)
        layout_buttons.addWidget(butt_op_sub, 3, 3)
        
        layout_buttons.addWidget(butt_num_1, 4, 0)
        layout_buttons.addWidget(butt_num_2, 4, 1)
        layout_buttons.addWidget(butt_num_3, 4, 2)
        layout_buttons.addWidget(butt_op_add, 4, 3)
        
        layout_buttons.addWidget(butt_num_0, 5, 0)
        layout_buttons.addWidget(butt_num_dot, 5, 1)
        layout_buttons.addWidget(butt_delete, 5, 2)
        layout_buttons.addWidget(butt_result, 5, 3)
        
    def but_number_pressed(self, button: str, display: QLabel):
        curr_text = display.text()
        
        # if display has "0"
        if(float(curr_text) == 0.0) and curr_text.find(".") == -1:
            display.setText(button)
            return
        
        curr_text += button
        
        display.setText(curr_text)
        # print("[INFO] - curr_text:", curr_text)
        
    def but_clear_pressed(self, display: QLabel):
        displaySettings.setDisplayLabel(display, cancel=True)
        
    def but_memory_pressed(self, display: QLabel):
        self.memory = float(display.text())
        
    def but_recall_pressed(self, display: QLabel):
        # clear display view before showing result of recall
        displaySettings.setDisplayLabel(display)
        
        floored = math.floor(self.memory)
        
        # if there is only integer preserved
        if self.memory - floored == 0:
            display.setText(str(floored))
            return
        
        display.setText(str(self.memory))
        
    def but_delete_pressed(self, display: QLabel):
        text_length = len(display.text())
        
        if(text_length == 1):
            display.setText("0")
            return
        
        display.setText(display.text()[:text_length-1])

    def but_decimal_pressed(self, display: QLabel):
        # check if not already inserted:
        if display.text().find(".") != NOT_DECIMAL:
            return
        
        # otherwise, insert into displaying data
        display.setText(display.text() + ".")
        
    ####################################################
    # MATH
    def operation_addition(self, display: QLabel):
        self.num_saved = float(display.text())
        
        self.but_clear_pressed(display)
        self.curr_op = self.OPERATIONS["addition"]
        
    def operation_result(self, display: QLabel):
        
        num_present = float(display.text())
        
        if self.curr_op == self.OPERATIONS["addition"]:
            display.setText(str(self.num_saved + num_present))
            displaySettings.setDisplayLabel(display, "color: red;")