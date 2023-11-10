# Calculator README

This is a simple calculator application built using PyQt5 in Python. The calculator provides basic arithmetic operations and a clear function.

## Features

- Addition, subtraction, multiplication, and division operations.
- Error handling for invalid mathematical expressions.
- Clear button to reset the input.

## Dependencies

- Python 3
- PyQt5

## How to Use

1. Ensure you have Python 3 installed on your system.
2. Install PyQt5 by running the following command in your terminal:

   ```bash
   pip install PyQt5
   ```

3. Run the calculator application:

   ```bash
   python calculator.py
   ```

4. The calculator window will appear, allowing you to perform basic arithmetic operations.

## Calculator Layout

The calculator UI consists of a main window with a display for input and output, and a grid of buttons for numerical and operational input.

- The display at the top shows the current input and the result of the calculation.
- The grid of buttons provides options for digits 0-9, basic arithmetic operations (+, -, *, /), clear (C), and equals (=).

## Usage

1. **Numeric Input**: Click on the digit buttons to input numbers.

2. **Arithmetic Operations**: Use the corresponding buttons (+, -, *, /) to perform basic arithmetic operations.

3. **Equals (=) Button**: Press the equals button to calculate the result of the expression.

4. **Clear (C) Button**: Clears the current input.

## Example Usage

1. Input a mathematical expression, e.g., `2 + 3`.
2. Press the equals button (=) to get the result.
3. Use the clear button (C) to reset the input for a new calculation.

## Notes

- The calculator uses the `eval` function to evaluate mathematical expressions. Ensure that the input is a valid expression to avoid errors.

- In case of an error during evaluation, the display will show "Error."

## License

This calculator application is provided under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.