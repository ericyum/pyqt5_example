import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor


# QWidget을 상속받아 MyApp 클래스 생성
class MyApp(QWidget):

    # 클래스 초기화 메서드
    def __init__(self):
        # 부모 클래스(QWidget)의 초기화 메서드 호출
        super().__init__()
        # UI 초기화 메서드 호출
        self.initUI()

    # 사용자 인터페이스 초기화 메서드
    def initUI(self):
        # 초기 색상을 검정색으로 설정 (RGB: 0, 0, 0)
        col = QColor(0, 0, 0)

        # 'Dialog' 텍스트를 가진 QPushButton 객체 생성
        # 'self'는 이 버튼이 MyApp 창의 자식 위젯임을 의미합니다.
        self.btn = QPushButton('Dialog', self)
        # 버튼의 위치를 (30, 30)으로 이동
        self.btn.move(30, 30)
        # 버튼이 클릭되었을 때 showDialog 메서드를 연결
        self.btn.clicked.connect(self.showDialog)

        # QFrame 객체 생성 (색상을 표시할 사각형 프레임)
        self.frm = QFrame(self)
        # 프레임의 배경색을 초기 색상(col)으로 설정
        # QWidget 스타일시트를 사용하여 배경색을 지정합니다.
        # col.name()은 QColor 객체의 색상 이름을 반환합니다 (예: "#000000").
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        # 프레임의 위치와 크기 설정 (x좌표, y좌표, 너비, 높이)
        self.frm.setGeometry(130, 35, 100, 100)

        # 창의 제목 설정
        self.setWindowTitle('Color Dialog')
        # 창의 위치와 크기 설정 (x좌표, y좌표, 너비, 높이)
        self.setGeometry(300, 300, 250, 180)
        # 창 보이기
        self.show()

    # 색상 다이얼로그를 표시하고 사용자 선택을 처리하는 메서드
    def showDialog(self):
        # QColorDialog.getColor()를 사용하여 색상 선택 다이얼로그를 띄웁니다.
        # 이 함수는 사용자가 선택한 QColor 객체를 반환합니다.
        # 사용자가 '취소'를 누르면 유효하지 않은(invalid) QColor 객체를 반환합니다.
        col = QColorDialog.getColor()

        # 사용자가 유효한 색상을 선택했을 경우 (즉, '확인' 버튼을 눌렀을 경우)
        if col.isValid():
            # 프레임의 배경색을 선택된 색상(col)으로 변경합니다.
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())


# 이 스크립트가 직접 실행될 때만 아래 코드 블록이 실행됩니다.
if __name__ == '__main__':
    # QApplication 객체 생성 (모든 PyQt 애플리케이션은 이 객체를 생성해야 합니다)
    app = QApplication(sys.argv)
    # MyApp 클래스의 인스턴스 생성 (우리가 만든 창 객체)
    ex = MyApp()
    # 애플리케이션을 실행하고 이벤트 루프에 진입합니다.
    # 창이 닫히면 sys.exit()를 통해 프로그램이 종료됩니다.
    sys.exit(app.exec_())