from math import sqrt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox, QSizePolicy
from PyQt5.QtGui import QFont


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_text = ""
        self.interface()

    def interface(self):
        grid = QGridLayout()

        self.input = QLineEdit()
        self.input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.input.setFixedHeight(60)
        self.input.setFont(QFont('Times', 15))
        self.input.setStyleSheet("background-color: white; color: black;")

        input_to_grid = QHBoxLayout()
        input_to_grid.addWidget(self.input)

        grid.addLayout(input_to_grid, 0, 0, 1, 3)

        grid.addWidget(self.input, 0, 0)

        # buttons
        self.add_button(grid, "0", 5, 1)
        self.add_button(grid, "1", 4, 0)
        self.add_button(grid, "2", 4, 1)
        self.add_button(grid, "3", 4, 2)
        self.add_button(grid, "4", 3, 0)
        self.add_button(grid, "5", 3, 1)
        self.add_button(grid, "6", 3, 2)
        self.add_button(grid, "7", 2, 0)
        self.add_button(grid, "8", 2, 1)
        self.add_button(grid, "9", 2, 2)
        self.add_button(grid, "+", 3, 3, "grey")  # add
        self.add_button(grid, "-", 2, 3, "grey")  # subtract
        self.add_button(grid, "/", 4, 3, "grey")  # divide
        self.add_button(grid, "*", 1, 3, "grey")  # multiply
        self.add_button(grid, "=", 5, 3, "grey")  # result
        self.add_button(grid, "\u221A", 1, 2, "grey")  # square root
        self.add_button(grid, "\u215Fx", 1, 0, "grey")  # 1/x
        self.add_button(grid, "x\u00B2", 1, 1, "grey")  # square x
        self.add_button(grid, ".", 5, 2, "grey")  # coma
        self.add_button(grid, "\u00B1", 5, 0, "grey")  # inverse
        self.add_button(grid, "\u2B8C", 0, 3, "grey")  # remove

        # przypisanie utworzonego układu do okna
        self.setLayout(grid)

        self.setGeometry(20, 20, 300, 400)
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color: black; color: white;")
        self.show()

    def add_button(self, grid, label, row, column, background_color="white"):
        button = QPushButton(label, self)
        button.setFixedHeight(60)
        button.setFont(QFont('Times', 15))
        button.setStyleSheet(f"background-color: {background_color}; color: black;")
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(self.fill_line)
        grid.addWidget(button, row, column)

    def fill_line(self):
        sender = self.sender()

        try:
            if sender.text() == "\u2B8C":  # remove
                result = self.current_text[:-1]
                self.current_text = result
                self.input.setText(result)
            elif sender.text() == "=": # result
                try:
                    result = str(eval(self.current_text))
                    self.current_text = result
                    self.input.setText(result)
                except ZeroDivisionError:
                    QMessageBox.critical(self, "Error", "Dividing by zero is not great idea!")
            elif sender.text() == "\u221A":  # square root
                result = str(sqrt(float(self.current_text)))
                self.current_text = result
                self.input.setText(result)
            elif sender.text() == "x\u00B2":  # square x
                result = str(float(self.current_text)**2)
                self.current_text = result
                self.input.setText(result)
            elif sender.text() == "\u00B1":  # inverse
                result = str(float(self.current_text) * -1)
                self.current_text = result
                self.input.setText(result)
            elif sender.text() == "\u215Fx":  # 1/x
                result = str(1/float(self.current_text))
                self.current_text = result
                self.input.setText(result)
            else:
                self.current_text += sender.text()
                self.input.setText(self.current_text)
        except:
            QMessageBox.warning(self, "Error", "Wrong data added!", QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
