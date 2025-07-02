from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QTimeEdit, QLabel, QWidget, QHBoxLayout, QMessageBox, QCheckBox
from PyQt5.QtCore import QTime, QTimer, QDateTime, Qt
import datetime

# UI 정의 클래스 (pyuic5가 생성한 부분)
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(QtCore.QRect(0, 0, 988, 709))
        Form.setWindowTitle("Form")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 40, 100, 30)) # 버튼 크기 조정
        self.pushButton.setObjectName("pushButton")

        # 시간 선택 QScrollArea
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(70, 100, 120, 80)) # 위치 조정
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 118, 78))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        # 분 선택 QScrollArea
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(230, 100, 120, 80)) # 위치 조정
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 118, 78))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        # 요일 버튼들
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 310, 75, 23))
        self.pushButton_2.setCheckable(True) # 토글 가능하도록 설정
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 310, 75, 23))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 310, 75, 23))
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 310, 75, 23))
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 310, 75, 23))
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 310, 75, 23))
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(640, 310, 75, 23))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")

        # 알람 목록을 표시할 QScrollArea (scrollArea_3)
        self.scrollArea_3 = QtWidgets.QScrollArea(Form)
        self.scrollArea_3.setGeometry(QtCore.QRect(140, 400, 351, 250)) # 위치 및 크기 조정
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 349, 248))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        # QVBoxLayout을 사용하여 알람들을 세로로 쌓음
        self.alarm_list_layout = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.alarm_list_layout.setAlignment(Qt.AlignTop) # 위쪽 정렬
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Alarm Clock"))
        self.pushButton.setText(_translate("Form", "Add Alarm"))
        self.pushButton_2.setText(_translate("Form", "Monday"))
        self.pushButton_3.setText(_translate("Form", "Tuesday"))
        self.pushButton_4.setText(_translate("Form", "Wednesday"))
        self.pushButton_5.setText(_translate("Form", "Thursday"))
        self.pushButton_6.setText(_translate("Form", "Friday"))
        self.pushButton_7.setText(_translate("Form", "Saturday"))
        self.pushButton_8.setText(_translate("Form", "Sunday"))


# 실제 알람 앱 로직을 처리하는 클래스
class AlarmApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setup_time_selectors() # 시간/분 선택기 설정
        self.setup_day_buttons()    # 요일 버튼 설정

        self.ui.pushButton.clicked.connect(self.add_alarm) # 'Add Alarm' 버튼 연결

        self.alarms = [] # 설정된 알람을 저장할 리스트
        self.check_alarm_timer = QTimer(self) # 1초마다 알람을 확인할 타이머
        self.check_alarm_timer.timeout.connect(self.check_for_alarms)
        self.check_alarm_timer.start(1000) # 1초 (1000ms)마다 체크

    def setup_time_selectors(self):
        # 시간 선택기 (QTimeEdit)
        self.time_edit = QTimeEdit(self)
        self.time_edit.setDisplayFormat("HH") # 시간만 표시
        self.time_edit.setTime(QTime.currentTime().addSecs(3600)) # 현재 시간에서 1시간 뒤로 초기 설정 (예시)
        
        # QScrollArea 내부에 QTimeEdit을 추가하기 위한 레이아웃
        hour_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
        hour_layout.addWidget(self.time_edit)
        hour_layout.setAlignment(Qt.AlignCenter) # 가운데 정렬

        # 분 선택기 (QTimeEdit)
        self.minute_edit = QTimeEdit(self)
        self.minute_edit.setDisplayFormat("mm") # 분만 표시
        self.minute_edit.setTime(QTime.currentTime().addSecs(600)) # 현재 시간에서 10분 뒤로 초기 설정 (예시)

        # QScrollArea_2 내부에 QTimeEdit을 추가하기 위한 레이아웃
        minute_layout = QVBoxLayout(self.ui.scrollAreaWidgetContents_2)
        minute_layout.addWidget(self.minute_edit)
        minute_layout.setAlignment(Qt.AlignCenter) # 가운데 정렬
    
    def setup_day_buttons(self):
        self.day_buttons = {
            "Monday": self.ui.pushButton_2,
            "Tuesday": self.ui.pushButton_3,
            "Wednesday": self.ui.pushButton_4,
            "Thursday": self.ui.pushButton_5,
            "Friday": self.ui.pushButton_6,
            "Saturday": self.ui.pushButton_7,
            "Sunday": self.ui.pushButton_8,
        }
        
        # 모든 요일 버튼의 텍스트를 QDayOfWeek 값에 맞게 재설정 (내부적으로)
        # Qt.Monday = 1, Qt.Tuesday = 2, ..., Qt.Sunday = 7
        self.day_map = {
            "Monday": Qt.Monday,
            "Tuesday": Qt.Tuesday,
            "Wednesday": Qt.Wednesday,
            "Thursday": Qt.Thursday,
            "Friday": Qt.Friday,
            "Saturday": Qt.Saturday,
            "Sunday": Qt.Sunday,
        }

        for day_name, button in self.day_buttons.items():
            button.clicked.connect(lambda checked, b=button: self.toggle_day_button(b))
            # 버튼 텍스트 설정 (필요한 경우)
            button.setText(day_name)
            # 기본적으로 아무 요일도 선택되지 않도록 초기화 (Optional)
            button.setChecked(False)

    def toggle_day_button(self, button):
        # 버튼의 토글 상태에 따라 스타일 변경 (선택됨/선택 안 됨 시각화)
        if button.isChecked():
            button.setStyleSheet("background-color: lightblue;")
        else:
            button.setStyleSheet("") # 기본 스타일로 복원

    def add_alarm(self):
        alarm_time = self.time_edit.time() # QTime 객체
        selected_days = []
        for day_name, button in self.day_buttons.items():
            if button.isChecked():
                selected_days.append(day_name)
        
        if not selected_days:
            QMessageBox.warning(self, "알람 설정 오류", "하나 이상의 요일을 선택해주세요.")
            return

        alarm_str = f"{alarm_time.toString('HH:mm')} {' '.join(selected_days)}"
        self.alarms.append({
            "time": alarm_time,
            "days": selected_days,
            "widget": None, # 나중에 알람 위젯을 참조하기 위함
            "enabled": True # 알람 활성화/비활성화 상태
        })

        self.display_alarm(self.alarms[-1]) # 추가된 알람을 UI에 표시
        QMessageBox.information(self, "알람 추가", f"알람이 추가되었습니다: {alarm_str}")

        # 알람 추가 후 요일 버튼 선택 해제 및 스타일 초기화
        for day_name, button in self.day_buttons.items():
            button.setChecked(False)
            button.setStyleSheet("")
        
        # 시간 선택기도 현재 시간으로 초기화 (선택적)
        self.time_edit.setTime(QTime.currentTime())
        self.minute_edit.setTime(QTime.currentTime())


    def display_alarm(self, alarm_data):
        alarm_widget = QWidget()
        alarm_layout = QHBoxLayout(alarm_widget)
        alarm_layout.setAlignment(Qt.AlignLeft) # 왼쪽 정렬

        alarm_text = f"{alarm_data['time'].toString('HH:mm')} ({' '.join(alarm_data['days'])})"
        
        label = QLabel(alarm_text)
        alarm_layout.addWidget(label)

        # 활성화/비활성화 체크박스
        enable_checkbox = QCheckBox("Enabled")
        enable_checkbox.setChecked(alarm_data['enabled'])
        enable_checkbox.stateChanged.connect(lambda state, ad=alarm_data: self.toggle_alarm_enabled(ad, state))
        alarm_layout.addWidget(enable_checkbox)

        # 삭제 버튼
        delete_button = QtWidgets.QPushButton("Delete")
        delete_button.clicked.connect(lambda: self.delete_alarm(alarm_data, alarm_widget))
        alarm_layout.addWidget(delete_button)

        # 알람 위젯을 저장하여 나중에 참조할 수 있도록 함
        alarm_data["widget"] = alarm_widget
        self.ui.alarm_list_layout.addWidget(alarm_widget)

    def toggle_alarm_enabled(self, alarm_data, state):
        alarm_data['enabled'] = (state == Qt.Checked)
        print(f"알람 {alarm_data['time'].toString('HH:mm')} 활성화 상태: {alarm_data['enabled']}")

    def delete_alarm(self, alarm_data, alarm_widget):
        # UI에서 위젯 제거
        self.ui.alarm_list_layout.removeWidget(alarm_widget)
        alarm_widget.deleteLater() # 위젯 파괴

        # 알람 리스트에서 제거
        if alarm_data in self.alarms:
            self.alarms.remove(alarm_data)
        QMessageBox.information(self, "알람 삭제", f"알람이 삭제되었습니다: {alarm_data['time'].toString('HH:mm')}")

    def check_for_alarms(self):
        current_time = QDateTime.currentDateTime()
        current_hour = current_time.time().hour()
        current_minute = current_time.time().minute()
        current_day_of_week = current_time.date().dayOfWeek() # Qt.Monday=1, ..., Qt.Sunday=7

        day_map_reverse = {v: k for k, v in self.day_map.items()} # 숫자 요일을 이름으로 변환

        for alarm in list(self.alarms): # 알람 리스트를 순회하며 수정될 수 있으므로 copy
            if not alarm['enabled']:
                continue # 비활성화된 알람은 건너뛴다

            alarm_hour = alarm['time'].hour()
            alarm_minute = alarm['time'].minute()
            
            # 현재 요일이 알람에 설정된 요일 중 하나인지 확인
            is_today_alarm_day = False
            for day_name in alarm['days']:
                if self.day_map[day_name] == current_day_of_week:
                    is_today_alarm_day = True
                    break
            
            if is_today_alarm_day and \
               alarm_hour == current_hour and \
               alarm_minute == current_minute:
                # 알람 시간 도달!
                alarm_msg = f"알람 울림: {alarm['time'].toString('HH:mm')} ({day_map_reverse[current_day_of_week]})"
                QMessageBox.information(self, "알람!", alarm_msg)
                
                # 울린 알람은 삭제 또는 비활성화 (여기서는 한 번 울리고 비활성화)
                alarm['enabled'] = False
                # 해당 위젯의 체크박스 상태 업데이트
                if alarm['widget']:
                    checkbox = alarm['widget'].findChild(QCheckBox)
                    if checkbox:
                        checkbox.setChecked(False) # 비활성화 상태로 UI 업데이트


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = AlarmApp()
    main_window.show()
    sys.exit(app.exec_())