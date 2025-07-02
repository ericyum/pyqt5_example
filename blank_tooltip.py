import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


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
        # 툴팁의 폰트 설정
        # 'SansSerif' 폰트 패밀리에 크기 10으로 설정합니다.
        QToolTip.setFont(QFont('SansSerif', 10))

        # 메인 창(QWidget)에 툴팁 설정
        # 마우스를 창 위에 올리면 "This is a QWidget widget" 메시지가 나타납니다.
        # HTML 태그를 사용하여 텍스트를 굵게 표시할 수 있습니다.
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 'Button' 텍스트를 가진 QPushButton 객체 생성
        # 'self'는 이 버튼이 MyApp 창의 자식 위젯임을 의미합니다.
        btn = QPushButton('Button', self)
        # 버튼에 툴팁 설정
        # 마우스를 버튼 위에 올리면 "This is a QPushButton widget" 메시지가 나타납니다.
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 버튼의 위치를 (50, 50)으로 이동
        btn.move(50, 50)
        # 버튼의 크기를 내용에 맞게 자동으로 조절 (최적의 크기)
        btn.resize(btn.sizeHint())

        # 창의 제목 설정
        self.setWindowTitle('Tooltips')
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