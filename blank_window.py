## Ex 3-1. 창 띄우기.
import sys
from PyQt5.QtWidgets import QApplication, QWidget


# QtWidgets이 부모 클래스
# 부모 클래스를 상속 받아서 MyApp이라는 클래스를 생성
class MyApp(QWidget):

    # 초기화를 해야하는 변수들의 경우 __init__ 메서드 안에 넣어서 초기화한다.
    # 예를 들어서 계산기를 켰는데 숫자나 부호가 적혀있으면 어색하다. 그래서 빈칸이 나오도록 '초기화'를 하는 것이 좋다. 그럴 때 해당 입력칸 부분을 '빈칸'으로 초기화한다.
    def __init__(self):
        # super는 부모 클래스를 가리킨다.
        super().__init__()
        self.initUI()

    def initUI(self):
        # 창의 이름을 설정
        self.setWindowTitle('My First Application')
        # 창을 띄우는 위치
        self.move(300, 300)
        # 창의 크기
        self.resize(400, 200)

        # 창 띄우기
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