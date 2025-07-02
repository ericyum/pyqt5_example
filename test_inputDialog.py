import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog)


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
        # 'Dialog' 텍스트를 가진 QPushButton 객체 생성
        # 'self'는 이 버튼이 MyApp 창의 자식 위젯임을 의미합니다.
        self.btn = QPushButton('Dialog', self)
        # 버튼의 위치를 (30, 30)으로 이동
        self.btn.move(30, 30)
        # 버튼이 클릭되었을 때 showDialog 메서드를 연결
        self.btn.clicked.connect(self.showDialog)

        # QLineEdit 객체 생성 (텍스트 입력 필드)
        self.le = QLineEdit(self)
        # QLineEdit의 위치를 (120, 35)로 이동
        self.le.move(120, 35)

        # 창의 제목 설정
        self.setWindowTitle('Input dialog')
        # 창의 위치와 크기 설정 (x좌표, y좌표, 너비, 높이)
        self.setGeometry(300, 300, 300, 200)
        # 창 보이기
        self.show()

    # 다이얼로그를 표시하고 사용자 입력을 처리하는 메서드
    def showDialog(self):
        # QInputDialog.getText()를 사용하여 텍스트 입력 다이얼로그를 띄웁니다.
        # 첫 번째 인자: 부모 위젯 (self)
        # 두 번째 인자: 다이얼로그 제목 ('Input Dialog')
        # 세 번째 인자: 사용자에게 표시될 메시지 ('Enter your name:')
        # 이 함수는 입력된 텍스트와 '확인' 버튼이 눌렸는지 여부를 반환합니다.
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        # 사용자가 '확인' 버튼을 눌렀을 경우
        if ok:
            # 입력된 텍스트를 QLineEdit에 설정합니다.
            # getText()는 QString을 반환하므로 str()로 변환하여 사용합니다.
            self.le.setText(str(text))


# 이 스크립트가 직접 실행될 때만 아래 코드 블록이 실행됩니다.
if __name__ == '__main__':
    # QApplication 객체 생성 (모든 PyQt 애플리케이션은 이 객체를 생성해야 합니다)
    app = QApplication(sys.argv)
    # MyApp 클래스의 인스턴스 생성 (우리가 만든 창 객체)
    ex = MyApp()
    # 애플리케이션을 실행하고 이벤트 루프에 진입합니다.
    # 창이 닫히면 sys.exit()를 통해 프로그램이 종료됩니다.
    sys.exit(app.exec_())