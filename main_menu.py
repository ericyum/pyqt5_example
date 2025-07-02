import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


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
        # 'Exit' 액션(메뉴 항목) 생성
        # QIcon('icon/exit.png')는 아이콘을 설정합니다. (해당 경로에 이미지가 있어야 합니다)
        # 'Exit'는 메뉴에 표시될 텍스트입니다.
        # 'self'는 이 액션이 MyApp 창에 속함을 의미합니다.
        exitAction = QAction(QIcon('icon/exit.png'), 'Exit', self)
        # 'Exit' 액션에 단축키 설정 (Ctrl+Q)
        exitAction.setShortcut('Ctrl+Q')
        # 'Exit' 액션에 마우스를 올렸을 때 상태바에 표시될 툴팁 메시지 설정
        exitAction.setStatusTip('Exit application')
        # 'Exit' 액션이 트리거(클릭 또는 단축키 사용)되었을 때 qApp.quit 함수를 연결
        # qApp은 QApplication 인스턴스를 참조하며, quit() 메서드는 애플리케이션을 종료합니다.
        exitAction.triggered.connect(qApp.quit)

        # 상태바 생성 (메시지는 표시하지 않고, 메뉴바와 함께 사용될 수 있도록 초기화)
        self.statusBar()

        # 메뉴바 생성
        # self.menuBar()는 QMainWindow에 기본으로 제공되는 메뉴바 객체를 반환합니다.
        menubar = self.menuBar()
        # macOS에서 메뉴바가 시스템 메뉴바 대신 애플리케이션 창 내부에 표시되도록 설정
        # Windows/Linux에서는 기본적으로 창 내부에 표시됩니다.
        menubar.setNativeMenuBar(False)
        # 메뉴바에 'File' 메뉴 추가
        # '&File'에서 '&'는 Alt+F를 눌러 메뉴를 활성화할 수 있도록 접근 키를 설정합니다.
        filemenu = menubar.addMenu('&File')
        # 'File' 메뉴에 exitAction 추가
        filemenu.addAction(exitAction)

        # 창의 제목 설정
        self.setWindowTitle('Menubar')
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