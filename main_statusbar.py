import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


# QMainWindow를 상속받아 MyApp 클래스 생성
# QMainWindow는 메뉴바, 툴바, 상태바 등을 가질 수 있는 메인 윈도우 클래스입니다.
class MyApp(QMainWindow):

    # 클래스 초기화 메서드
    def __init__(self):
        # 부모 클래스(QMainWindow)의 초기화 메서드 호출
        super().__init__()
        # UI 초기화 메서드 호출
        self.initUI()

    # 사용자 인터페이스 초기화 메서드
    def initUI(self):
        # 상태바 생성 및 메시지 표시
        # self.statusBar()는 QMainWindow에 기본으로 제공되는 상태바 객체를 반환합니다.
        # showMessage() 메서드를 사용하여 상태바에 'Ready'라는 메시지를 표시합니다.
        self.statusBar().showMessage('Ready')

        # 창의 제목 설정
        self.setWindowTitle('Statusbar')
        # 창의 위치와 크기 설정 (x좌표, y좌표, 너비, 높이)
        self.setGeometry(300, 300, 300, 200)
        # 창 보이기
        self.show()


# 이 스크립트가 직접 실행될 때만 아래 코드 블록이 실행됩니다.
if __name__ == '__main__':
    # QApplication 객체 생성 (모든 PyQt 애플리케이션은 이 객체를 생성해야 합니다)
    app = QApplication(sys.argv)
    # MyApp 클래스의 인스턴스 생성 (우리가 만든 메인 창 객체)
    ex = MyApp()
    # 애플리케이션을 실행하고 이벤트 루프에 진입합니다.
    # 창이 닫히면 sys.exit()를 통해 프로그램이 종료됩니다.
    sys.exit(app.exec_())