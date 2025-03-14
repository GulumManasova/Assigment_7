import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from calculator_logic import Calculator

class CalculatorWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.calculator = Calculator()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Calculator')
        self.setStyleSheet("background-color: #2d2d2d;")  # Dark background

        # Create the QLineEdit for displaying the input/output
        self.input = QLineEdit(self)
        self.input.setReadOnly(True)
        self.input.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input.setStyleSheet("font-size: 32px; height: 60px; color: white; background-color: #333333; padding: 10px;")

        # Create buttons for digits, operators, and the equals button
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        # Create a vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.input)

        # Create a grid layout for buttons
        grid_layout = QGridLayout()

        # Define button positions in the grid layout
        positions = [(i, j) for i in range(4) for j in range(4)]

        # Add buttons to the layout (white color for buttons)
        for position, button_text in zip(positions, buttons):
            button = QPushButton(button_text, self)
            button.setStyleSheet("font-size: 28px; height: 70px; background-color: white; color: black; border-radius: 10px;")
            button.clicked.connect(self.button_click)
            grid_layout.addWidget(button, *position)

        # Color the operation buttons (yellow for +, -, *, /, =, C)
        operation_buttons = ['+', '-', '*', '/', '=', 'C']
        for button_text in operation_buttons:
            for i in range(grid_layout.count()):
                button = grid_layout.itemAt(i).widget()
                if button.text() == button_text:
                    button.setStyleSheet("font-size: 28px; height: 70px; background-color: #FFEB3B; color: black; border-radius: 10px;")

        # Add the grid layout to the vertical layout
        vbox.addLayout(grid_layout)

        # Set the layout for the main window
        self.setLayout(vbox)

    def button_click(self):
        sender = self.sender().text()

        if sender == '=':
            # Calculate and display the result
            result = self.calculator.calculate()
            self.input.setText(str(result))
        elif sender == 'C':
            # Clear the expression and input field
            self.clear_input()
        else:
            # Add the character to the expression and display it
            self.calculator.add_to_expression(sender)
            self.input.setText(self.calculator.get_expression())

    def clear_input(self):
        # Clear the expression and input field
        self.calculator.clear_expression()
        self.input.clear()


def main():
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
