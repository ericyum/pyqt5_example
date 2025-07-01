import sys
from PyQt5.QtWidgets import QApplication, QWidget


# QtWidgets이 부모 클래스
# 부모 클래스를 상속 받아서 MyApp이라는 클래스를 생성
class MyApp(QWidget):

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


if __name__ == '__main__':
   app = QApplication(sys.argv)
   # 실제로 창을 띄우고 싶음. 그래서 ex라는 객체를 생성해서 창을 띄움.
   ex = MyApp()
   sys.exit(app.exec_())