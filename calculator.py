import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit
)


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(200, 200, 400, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setStyleSheet("font-size: 24px;")
        self.result_display.setReadOnly(True)
        self.layout.addWidget(self.result_display)

        button_layout = self.create_button_layout()
        self.layout.addLayout(button_layout)

        self.central_widget.setLayout(self.layout)

    def create_button_layout(self):
        button_layout = QVBoxLayout()

        rows = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", "C", "=", "+")
        ]

        for row in rows:
            h_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.button_click)
                button.setStyleSheet("font-size: 18px;")
                h_layout.addWidget(button)
            button_layout.addLayout(h_layout)

        return button_layout

    def button_click(self):
        button = self.sender().text()
        if button == "=":
            try:
                result = str(eval(self.result_display.text()))
                self.result_display.setText(result)
            except Exception:
                self.result_display.setText("Error")
        elif button == "C":
            self.result_display.clear()
        else:
            current_text = self.result_display.text()
            new_text = current_text + button
            self.result_display.setText(new_text)


def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
