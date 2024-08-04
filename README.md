
# Text-Based Calculator

Welcome to the text-based calculator, a simple and interactive Python program that performs basic arithmetic operations.

## Features

- Addition, Subtraction, Multiplication, and Division.
- User-friendly prompts to input numbers and select operators.
- Continuous calculations with the option to reuse the previous result.
- Robust input validation to handle invalid entries gracefully.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/0x2V369/calculator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd text-based-calculator
   ```

3. Run the calculator program:

   ```bash
   python calculator.py
   ```

## Usage

1. Follow the on-screen prompts to enter the first number.
2. Select an operator from the provided options (`+`, `-`, `*`, `/`).
3. Enter the second number.
4. View the result of the calculation.
5. Choose whether to continue calculating with the result or start a new calculation.

## Code Overview

Here's a brief overview of the main functions in the `calculator.py` script:

- `calculate(num1, num2, operator)`: Performs the calculation based on the provided operator.
- `number_input(prompt)`: Prompts the user for a numeric input and validates it.
- `pick_an_operator()`: Prompts the user to select a valid operator.
- `main()`: Main function that runs the calculator loop.

## Example

```bash
Welcome to the text-based calculator
Please enter a number:
10
Please provide an operator (+, -, *, /):
+
Please enter a number:
5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to exit.
```

## Author

Created by [0x2V369](https://github.com/0x2V369).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
