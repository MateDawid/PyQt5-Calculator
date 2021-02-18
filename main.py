from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interface()

    def interface(self):
        grid = QGridLayout()

        self.input = QLineEdit()
        self.input.setFixedHeight(60)
        self.input.setFont(QFont('Times', 15))
        self.input.setStyleSheet("background-color: white;")

        input_to_grid = QHBoxLayout()
        input_to_grid.addWidget(self.input)

        grid.addLayout(input_to_grid, 0, 0, 1, 4)

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
        self.add_button(grid, "+", 3, 3, "grey")
        self.add_button(grid, "-", 2, 3, "grey")
        self.add_button(grid, "/", 4, 3, "grey")
        self.add_button(grid, "*", 1, 3, "grey")
        self.add_button(grid, "=", 5, 3, "grey")
        self.add_button(grid, "\u221A", 1, 2, "grey")
        self.add_button(grid, "\u215Fx", 1, 0, "grey")
        self.add_button(grid, "x\u00B2", 1, 1, "grey")
        self.add_button(grid, ",", 5, 2, "grey")
        self.add_button(grid, "\u00B1", 5, 0, "grey")

        # przypisanie utworzonego układu do okna
        self.setLayout(grid)

        self.setGeometry(20, 20, 300, 400)
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color: black;")
        self.show()

    def add_button(self, grid, label, row, column, background_color="white"):
        button = QPushButton(label, self)
        button.setFixedHeight(60)
        button.setFont(QFont('Times', 15))
        button.setStyleSheet(f"background-color: {background_color};")
        grid.addWidget(button, row, column)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
