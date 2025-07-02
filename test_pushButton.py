import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


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
        # 첫 번째 QPushButton 객체 생성
        # '&Button1'에서 '&'는 Alt+B를 눌러 버튼을 활성화할 수 있도록 접근 키를 설정합니다.
        btn1 = QPushButton('&Button1', self)
        # 버튼을 토글 가능한(checkable) 상태로 설정합니다.
        # 토글 가능한 버튼은 클릭될 때마다 눌린 상태와 눌리지 않은 상태를 전환합니다.
        btn1.setCheckable(True)
        # 버튼의 초기 상태를 토글하여 눌린 상태로 만듭니다.
        btn1.toggle()

        # 두 번째 QPushButton 객체 생성
        # 텍스트를 나중에 setText() 메서드로 설정합니다.
        btn2 = QPushButton(self)
        # 버튼의 텍스트를 'Button2'로 설정하고, '&'를 사용하여 Alt+2로 접근 키를 설정합니다.
        btn2.setText('Button&2')

        # 세 번째 QPushButton 객체 생성
        btn3 = QPushButton('Button3', self)
        # 버튼을 비활성화합니다. 비활성화된 버튼은 클릭할 수 없습니다.
        btn3.setEnabled(False)

        # 수직 박스 레이아웃(QVBoxLayout) 생성
        # 위젯들을 수직으로 정렬하는 데 사용됩니다.
        vbox = QVBoxLayout()
        # 레이아웃에 btn1 추가
        vbox.addWidget(btn1)
        # 레이아웃에 btn2 추가
        vbox.addWidget(btn2)
        # 레이아웃에 btn3 추가
        vbox.addWidget(btn3)

        # 현재 위젯(MyApp)의 레이아웃을 vbox로 설정
        self.setLayout(vbox)
        # 창의 제목 설정
        self.setWindowTitle('QPushButton')
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
    # 창이 닫히면 sys.exit()를 통해 프로그램이 종료됩니다.
    sys.exit(app.exec_())