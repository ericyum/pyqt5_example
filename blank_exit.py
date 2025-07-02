import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


# QWidget을 상속받아 MyApp 클래스 생성
class MyApp(QWidget):

    # 클래스 초기화 메서드
    def __init__(self):
        # 부모 클래스의 초기화 메서드 호출
        super().__init__()
        # UI 초기화 메서드 호출
        self.initUI()

    # 사용자 인터페이스 초기화 메서드
    def initUI(self):
        # 'Quit' 텍스트를 가진 QPushButton 객체 생성
        # 'self'는 이 버튼이 MyApp 창의 자식 위젯임을 의미합니다.
        btn = QPushButton('Quit', self)
        # 버튼의 위치를 (50, 50)으로 이동
        btn.move(50, 50)
        # 버튼의 크기를 내용에 맞게 자동으로 조절 (최적의 크기)
        btn.resize(btn.sizeHint())
        # 버튼이 클릭되었을 때 실행될 함수를 연결 (시그널-슬롯 연결)
        # QCoreApplication.instance().quit는 현재 실행 중인 애플리케이션을 종료하는 함수입니다.
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 창의 제목 설정
        self.setWindowTitle('Quit Button')
        # 창의 위치와 크기 설정 (x좌표, y좌표, 너비, 높이)
        self.setGeometry(300, 300, 300, 200)
        # 창 보이기
        self.show()


# 이 스크립트가 직접 실행될 때만 아래 코드 블록이 실행됩니다.
if __name__ == '__main__':
    # QApplication 객체 생성 (모든 PyQt 애플리케이션은 이 객체를 생성해야 합니다)
    app = QApplication(sys.argv)
    # MyApp 클래스의 인스턴스 생성 (우리가 만든 창 객체)
    ex = MyApp()
    # 애플리케이션을 실행하고 이벤트 루프에 진입합니다.
    # 창이 닫히거나 quit 시그널이 발생하면 sys.exit()를 통해 프로그램이 종료됩니다.
    sys.exit(app.exec_())