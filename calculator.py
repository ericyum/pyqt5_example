from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(QtCore.QRect(0, 0, 998, 753))
        Form.setWindowTitle("Form")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(370, 30, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        # 초기값을 "0"으로 설정
        self.textBrowser.setText("0")

        # C (Clear) Button
        self.C = QtWidgets.QPushButton(Form)
        self.C.setGeometry(QtCore.QRect(250, 270, 75, 23))
        self.C.setObjectName("C")

        # Backspace Button
        self.backspace = QtWidgets.QPushButton(Form)
        self.backspace.setGeometry(QtCore.QRect(400, 270, 75, 23))
        self.backspace.setObjectName("backspace")

        # Percent Button
        self.percent = QtWidgets.QPushButton(Form)
        self.percent.setGeometry(QtCore.QRect(540, 270, 75, 23))
        self.percent.setObjectName("percent")

        # Number Buttons
        self.seven = QtWidgets.QPushButton(Form)
        self.seven.setGeometry(QtCore.QRect(240, 340, 75, 23))
        self.seven.setObjectName("seven")

        self.eight = QtWidgets.QPushButton(Form)
        self.eight.setGeometry(QtCore.QRect(400, 340, 75, 23))
        self.eight.setObjectName("eight")

        self.nine = QtWidgets.QPushButton(Form)
        self.nine.setGeometry(QtCore.QRect(540, 340, 75, 23))
        self.nine.setObjectName("nine")

        self.four = QtWidgets.QPushButton(Form)
        self.four.setGeometry(QtCore.QRect(240, 430, 75, 23))
        self.four.setObjectName("four")

        self.five = QtWidgets.QPushButton(Form)
        self.five.setGeometry(QtCore.QRect(400, 440, 75, 23))
        self.five.setObjectName("five")

        self.six = QtWidgets.QPushButton(Form)
        self.six.setGeometry(QtCore.QRect(530, 440, 75, 23))
        self.six.setObjectName("six")

        self.one = QtWidgets.QPushButton(Form)
        self.one.setGeometry(QtCore.QRect(240, 510, 75, 23))
        self.one.setObjectName("one")

        self.two = QtWidgets.QPushButton(Form)
        self.two.setGeometry(QtCore.QRect(400, 510, 75, 23))
        self.two.setObjectName("two")

        self.three = QtWidgets.QPushButton(Form)
        self.three.setGeometry(QtCore.QRect(530, 510, 75, 23))
        self.three.setObjectName("three")

        self.doublezero = QtWidgets.QPushButton(Form)
        self.doublezero.setGeometry(QtCore.QRect(240, 590, 75, 23))
        self.doublezero.setObjectName("doublezero")

        self.zero = QtWidgets.QPushButton(Form)
        self.zero.setGeometry(QtCore.QRect(400, 590, 75, 23))
        self.zero.setObjectName("zero")

        self.dot = QtWidgets.QPushButton(Form)
        self.dot.setGeometry(QtCore.QRect(530, 590, 75, 23))
        self.dot.setObjectName("dot")

        # Operator Buttons
        self.devide = QtWidgets.QPushButton(Form)
        self.devide.setGeometry(QtCore.QRect(670, 270, 75, 23))
        self.devide.setObjectName("devide")

        self.multiply = QtWidgets.QPushButton(Form)
        self.multiply.setGeometry(QtCore.QRect(680, 350, 75, 23))
        self.multiply.setObjectName("multiply")

        self.minus = QtWidgets.QPushButton(Form)
        self.minus.setGeometry(QtCore.QRect(680, 440, 75, 23))
        self.minus.setObjectName("minus")

        self.plus = QtWidgets.QPushButton(Form)
        self.plus.setGeometry(QtCore.QRect(680, 510, 75, 23))
        self.plus.setObjectName("plus")

        # Equals Button
        self.equal = QtWidgets.QPushButton(Form)
        self.equal.setGeometry(QtCore.QRect(680, 590, 75, 23))
        self.equal.setObjectName("equal")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.C.setText(_translate("Form", "C"))
        self.backspace.setText(_translate("Form", "<-"))
        self.percent.setText(_translate("Form", "%"))
        self.seven.setText(_translate("Form", "7"))
        self.eight.setText(_translate("Form", "8"))
        self.nine.setText(_translate("Form", "9"))
        self.four.setText(_translate("Form", "4"))
        self.five.setText(_translate("Form", "5"))
        self.six.setText(_translate("Form", "6"))
        self.devide.setText(_translate("Form", "/"))
        self.multiply.setText(_translate("Form", "*"))
        self.minus.setText(_translate("Form", "-"))
        self.one.setText(_translate("Form", "1"))
        self.two.setText(_translate("Form", "2"))
        self.three.setText(_translate("Form", "3"))
        self.plus.setText(_translate("Form", "+"))
        self.doublezero.setText(_translate("Form", "00"))
        self.zero.setText(_translate("Form", "0"))
        self.dot.setText(_translate("Form", "."))
        self.equal.setText(_translate("Form", "="))


# 실제 계산기 로직과 버튼 이벤트를 처리하는 클래스
class CalculatorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 이전에 계산된 결과가 있는지 여부를 나타내는 플래그
        self.new_calculation_needed = True

        # 숫자 버튼들을 리스트로 묶어 이벤트 연결
        self.number_buttons = [
            self.ui.zero, self.ui.one, self.ui.two, self.ui.three, self.ui.four,
            self.ui.five, self.ui.six, self.ui.seven, self.ui.eight, self.ui.nine,
            self.ui.doublezero, self.ui.dot
        ]
        for button in self.number_buttons:
            button.clicked.connect(self.number_button_clicked)

        # 연산자 버튼들을 리스트로 묶어 이벤트 연결
        self.operator_buttons = [
            self.ui.plus, self.ui.minus, self.ui.multiply, self.ui.devide
        ]
        for button in self.operator_buttons:
            button.clicked.connect(self.operator_button_clicked)

        # 특수 기능 버튼 연결
        self.ui.C.clicked.connect(self.clear_button_clicked)
        self.ui.backspace.clicked.connect(self.backspace_button_clicked)
        self.ui.percent.clicked.connect(self.percent_button_clicked)
        self.ui.equal.clicked.connect(self.equal_button_clicked)

    # --- 계산기 기능 함수 정의 시작 ---
    def number_button_clicked(self):
        # self.sender()는 QtWidgets.QWidget를 상속받은 클래스에서 사용 가능합니다.
        button_text = self.sender().text()
        current_display = self.ui.textBrowser.toPlainText()

        # 이전에 =을 눌러 계산 결과가 나왔거나, display가 "0"인 상태에서 새 숫자를 입력할 때
        if self.new_calculation_needed or current_display == "0":
            # "0"을 누르면 아무것도 하지 않음 (초기 "0" 유지)
            if button_text == "0":
                self.ui.textBrowser.setText("0")
            # "."을 누르면 "0."으로 시작
            elif button_text == ".":
                self.ui.textBrowser.setText("0.")
            else:
                # 그 외 숫자는 그대로 입력 (00 포함)
                self.ui.textBrowser.setText(button_text)
            self.new_calculation_needed = False
        else:
            # 현재 디스플레이가 이미 소수점을 포함하고 있을 때 또 다른 소수점 입력 방지
            if button_text == "." and "." in current_display:
                pass
            else:
                self.ui.textBrowser.setText(current_display + button_text)
        
        # 현재 표시된 내용을 기반으로 current_expression을 업데이트 (CalculatorApp에는 필요 없음)
        # self.current_expression = self.ui.textBrowser.toPlainText()


    def operator_button_clicked(self):
        operator = self.sender().text()
        current_display = self.ui.textBrowser.toPlainText()

        # 연산자 버튼을 누를 때마다 new_calculation_needed를 False로 설정하여
        # 숫자를 입력하는 흐름으로 전환 (새로운 피연산자 입력 대기)
        self.new_calculation_needed = False

        # 현재 입력이 오류 상태이면 연산자 입력 방지
        if current_display in ["Error", "Error: Divide by zero", "Error: Invalid expression"]:
            return

        # 현재 textBrowser의 마지막 문자가 이미 연산자인 경우 연산자 교체
        if current_display and current_display[-1] in "+-*/.": # .도 연산자처럼 처리하여 중복 방지
            # 마지막 연산자를 제거하고 새 연산자를 추가
            self.ui.textBrowser.setText(current_display[:-1] + operator)
        else:
            # 숫자가 입력된 상태에서 연산자 추가
            self.ui.textBrowser.setText(current_display + operator)


    def clear_button_clicked(self):
        self.ui.textBrowser.setText("0") # 초기값을 0으로 설정
        self.new_calculation_needed = True # 초기화 후에는 새로운 계산이 필요

    def backspace_button_clicked(self):
        current_display = self.ui.textBrowser.toPlainText()
        if current_display == "Error" or current_display == "0":
            return # 오류 상태이거나 0이면 지우지 않음

        new_text = current_display[:-1] # 마지막 문자 제거
        if not new_text or (len(new_text) == 1 and new_text[0] == '-'): # 전부 지워졌거나 마이너스만 남았으면 "0"으로 설정
            self.ui.textBrowser.setText("0")
            self.new_calculation_needed = True
        else:
            self.ui.textBrowser.setText(new_text)


    def percent_button_clicked(self):
        try:
            expression = self.ui.textBrowser.toPlainText()
            # 마지막 숫자를 추출하여 퍼센트 계산 (간단한 구현)
            # 복잡한 수식 중간의 %는 처리하지 않음
            if not expression or expression in ["Error", "Error: Divide by zero", "Error: Invalid expression"]:
                return

            # 수식에서 숫자가 아닌 문자를 기준으로 분리
            import re
            numbers = re.findall(r"(\d+\.?\d*)", expression)
            operators = re.findall(r"[\+\-\*/]", expression)

            if not numbers:
                self.ui.textBrowser.setText("Error")
                self.new_calculation_needed = True
                return

            last_num_str = numbers[-1]
            current_value = float(last_num_str)
            result = current_value / 100

            # 수식의 마지막 부분을 결과로 교체
            # eval에 사용할 수 있는 형태로 다시 조합
            new_expression = expression[:expression.rfind(last_num_str)] + str(result)

            self.ui.textBrowser.setText(new_expression)
            self.new_calculation_needed = True # 퍼센트 계산 후에는 새 계산 시작처럼 동작
        except ValueError:
            self.ui.textBrowser.setText("Error")
            self.new_calculation_needed = True
        except Exception as e:
            self.ui.textBrowser.setText("Error")
            self.new_calculation_needed = True


    def equal_button_clicked(self):
        expression = self.ui.textBrowser.toPlainText()
        # textBrowser가 비어있거나, Error 상태이거나, 연산자로 끝나면 계산하지 않음
        if not expression or expression in ["Error", "Error: Divide by zero", "Error: Invalid expression"] or expression[-1] in "+-*/.":
            return

        try:
            # 곱셈/나눗셈 기호 변경 (UI에는 * / 이지만 eval은 Python 연산자를 사용)
            # 실제 UI에선 * / 기호로 보여주므로 변경할 필요 없음.
            # 하지만 eval 함수가 인식하는 기호는 Python 문법에 따라야 함.
            # 사용자 입력에 따라 x나 ÷ 가 들어올 수 있으므로 eval 전에 변환.
            # 현재 UI는 그냥 * / 이므로 이 부분은 필요 없을 수 있으나, 안전을 위해 유지
            expression_to_evaluate = expression.replace('x', '*').replace('÷', '/')
            result = eval(expression_to_evaluate)

            # 정수 결과일 경우 소수점 없이 표시
            if result == int(result):
                result = int(result)
            elif abs(result - round(result, 10)) < 1e-9: # 부동 소수점 오차 처리 (0.3 - 0.2 = 0.0999...)
                result = round(result, 10) # 적절한 정밀도로 반올림

            self.ui.textBrowser.setText(str(result))
            self.new_calculation_needed = True # 계산 완료 후 새로운 숫자 입력 시 초기화 위함
        except ZeroDivisionError:
            self.ui.textBrowser.setText("Error: Divide by zero")
            self.new_calculation_needed = True
        except (SyntaxError, NameError):
            self.ui.textBrowser.setText("Error: Invalid expression")
            self.new_calculation_needed = True
        except Exception as e:
            self.ui.textBrowser.setText("Error")
            self.new_calculation_needed = True
    # --- 계산기 기능 함수 정의 끝 ---


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # CalculatorApp 인스턴스를 생성하여 메인 윈도우로 사용합니다.
    main_window = CalculatorApp()
    main_window.show()
    sys.exit(app.exec_())