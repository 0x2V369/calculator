# Simple text based calculator program

def calculate(num1, num2, operator):
    """
    :param num1: first number
    :param num2: second number
    :param operator: mathematical operator
    :return: returns the calculation of 2 numbers based on the operator
    """

    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else "error: Division by zero"
    }

    return operations.get(operator, "Invalid operator provided")


def number_input(prompt="Please enter a number:\n"):
    """
    :param prompt: prompt message to display to the user
    :return: returns user input for first number in calculation
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please provide a number.")


def pick_an_operator():
    """
    :return: returns user choice for the operator
    """
    while True:
        operator = str(input("Please provide an operator (+, -, *, /): \n"))
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid operator. Please provide a valid operator.\n")


def main():
    print("Welcome to the text-based calculator")
    continue_calculating = True

    while continue_calculating:
        first_num = number_input()
        operator = pick_an_operator()
        second_num = number_input()

        result = calculate(first_num, second_num, operator)
        print(f"{first_num} {operator} {second_num} = {result}")

        while continue_calculating:
            continue_calculating = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.\n"))
            if continue_calculating in ['y', 'yes', 'yeah', 'yea']:
                first_num = result
                operator = pick_an_operator()
                second_num = number_input()
                result = calculate(first_num, second_num, operator)
                print(f"{first_num} {operator} {second_num} = {result}")
            else:
                continue_calculating = False
                break


if __name__ == "__main__":
    main()
