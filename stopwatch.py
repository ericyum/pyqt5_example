from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(QtCore.QRect(0, 0, 504, 518))
        Form.setWindowTitle("Form")

        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(170, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")

        self.Start = QtWidgets.QPushButton(Form)
        self.Start.setGeometry(QtCore.QRect(100, 100, 75, 23))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.Start.setFont(font)
        self.Start.setObjectName("Start")

        self.Stop = QtWidgets.QPushButton(Form)
        self.Stop.setGeometry(QtCore.QRect(290, 100, 75, 23))
        self.Stop.setObjectName("Stop")

        self.Reset = QtWidgets.QPushButton(Form)
        self.Reset.setGeometry(QtCore.QRect(200, 100, 75, 23))
        self.Reset.setObjectName("Reset")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # --- 여기에 버튼 기능 연결 및 타이머 로직 추가 ---
        self.timer = QtCore.QTimer(Form)
        self.timer.timeout.connect(self.update_timer)
        self.elapsed_time_ms = 0
        self.is_running = False

        # 초기 버튼 상태 설정
        self.Stop.setEnabled(False)   # Stop 버튼은 처음에는 비활성화
        self.Reset.setEnabled(True)  # Reset 버튼은 처음에는 활성화

        self.Start.clicked.connect(self.start_button_clicked)
        self.Stop.clicked.connect(self.stop_button_clicked)
        self.Reset.clicked.connect(self.reset_button_clicked)
        # --- 추가된 코드 끝 ---

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "00:00.0"))
        self.Start.setText(_translate("Form", "Start"))
        self.Stop.setText(_translate("Form", "Stop"))
        self.Reset.setText(_translate("Form", "Reset"))

    def start_button_clicked(self):
        print("Start 버튼이 클릭되었습니다!")
        if not self.is_running:
            self.timer.start(10)
            self.is_running = True
            # Start 버튼을 누르면 Stop 활성화, Reset 비활성화
            self.Start.setEnabled(False)
            self.Stop.setEnabled(True)
            self.Reset.setEnabled(False)

    def stop_button_clicked(self):
        print("Stop 버튼이 클릭되었습니다!")
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            # Stop 버튼을 누르면 Stop 비활성화, Reset 활성화
            self.Start.setEnabled(True) # Start 버튼 다시 활성화
            self.Stop.setEnabled(False)
            self.Reset.setEnabled(True)

    def reset_button_clicked(self):
        print("Reset 버튼이 클릭되었습니다!")
        if self.is_running:
            self.timer.stop()
            self.is_running = False # Reset 시에도 타이머 상태를 '정지'로 변경
        self.elapsed_time_ms = 0
        self.label1.setText("00:00.0")
        # Reset 버튼을 누르면 Stop 비활성화, Reset 활성화 (초기 상태와 동일)
        self.Start.setEnabled(True) # Start 버튼 활성화
        self.Stop.setEnabled(False)
        self.Reset.setEnabled(True)

    def update_timer(self):
        self.elapsed_time_ms += 10

        minutes = (self.elapsed_time_ms // 1000) // 60
        seconds = (self.elapsed_time_ms // 1000) % 60
        tenths_of_second = (self.elapsed_time_ms % 1000) // 100

        self.label1.setText(f"{minutes:02d}:{seconds:02d}.{tenths_of_second}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())