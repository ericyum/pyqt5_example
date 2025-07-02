import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
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
        # QTextEdit 객체 생성 (텍스트를 표시하고 편집할 수 있는 위젯)
        self.textEdit = QTextEdit()
        # QTextEdit을 메인 창의 중앙 위젯으로 설정
        self.setCentralWidget(self.textEdit)
        # 상태바 생성 (메시지는 표시하지 않고, 메뉴바와 함께 사용될 수 있도록 초기화)
        self.statusBar()

        # 'Open' 액션(메뉴 항목) 생성
        # QIcon('open.png')는 아이콘을 설정합니다. (해당 경로에 이미지가 있어야 합니다)
        # 'Open'은 메뉴에 표시될 텍스트입니다.
        # 'self'는 이 액션이 MyApp 창에 속함을 의미합니다.
        openFile = QAction(QIcon('open.png'), 'Open', self)
        # 'Open' 액션에 단축키 설정 (Ctrl+O)
        openFile.setShortcut('Ctrl+O')
        # 'Open' 액션에 마우스를 올렸을 때 상태바에 표시될 툴팁 메시지 설정
        openFile.setStatusTip('Open New File')
        # 'Open' 액션이 트리거(클릭 또는 단축키 사용)되었을 때 showDialog 함수를 연결
        openFile.triggered.connect(self.showDialog)

        # 메뉴바 생성
        # self.menuBar()는 QMainWindow에 기본으로 제공되는 메뉴바 객체를 반환합니다.
        menubar = self.menuBar()
        # macOS에서 메뉴바가 시스템 메뉴바 대신 애플리케이션 창 내부에 표시되도록 설정
        # Windows/Linux에서는 기본적으로 창 내부에 표시됩니다.
        menubar.setNativeMenuBar(False)
        # 메뉴바에 '&File' 메뉴 추가
        # '&File'에서 '&'는 Alt+F를 눌러 메뉴를 활성화할 수 있도록 접근 키를 설정합니다.
        fileMenu = menubar.addMenu('&File')
        # 'File' 메뉴에 openFile 액션 추가
        fileMenu.addAction(openFile)

        # 창의 제목 설정
        self.setWindowTitle('File Dialog')
        # 창의 위치와 크기 설정 (x좌표, y좌표, 너비, 높이)
        self.setGeometry(300, 300, 300, 200)
        # 창 보이기
        self.show()

    # 파일 다이얼로그를 표시하고 선택된 파일을 처리하는 메서드
    def showDialog(self):
        # QFileDialog.getOpenFileName()을 사용하여 파일 열기 다이얼로그를 띄웁니다.
        # 첫 번째 인자: 부모 위젯 (self)
        # 두 번째 인자: 다이얼로그 제목 ('Open file')
        # 세 번째 인자: 초기 디렉토리 ('./'는 현재 디렉토리)
        # 이 함수는 선택된 파일 경로(튜플의 첫 번째 요소)와 파일 필터(튜플의 두 번째 요소)를 반환합니다.
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        # 파일 경로가 유효할 경우 (사용자가 파일을 선택하고 '열기' 버튼을 눌렀을 경우)
        if fname[0]:
            # 선택된 파일을 읽기 모드('r')로 엽니다.
            f = open(fname[0], 'r')

            # 'with' 문을 사용하여 파일을 열면 파일이 자동으로 닫힙니다.
            with f:
                # 파일의 모든 내용을 읽어옵니다.
                data = f.read()
                # 읽어온 내용을 QTextEdit 위젯에 설정하여 표시합니다.
                self.textEdit.setText(data)


# 이 스크립트가 직접 실행될 때만 아래 코드 블록이 실행됩니다.
if __name__ == '__main__':
    # QApplication 객체 생성 (모든 PyQt 애플리케이션은 이 객체를 생성해야 합니다)
    app = QApplication(sys.argv)
    # MyApp 클래스의 인스턴스 생성 (우리가 만든 메인 창 객체)
    ex = MyApp()
    # 애플리케이션을 실행하고 이벤트 루프에 진입합니다.
    # 창이 닫히면 sys.exit()를 통해 프로그램이 종료됩니다.
    sys.exit(app.exec_())