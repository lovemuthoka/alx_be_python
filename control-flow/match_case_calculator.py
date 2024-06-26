# match_case_calculator.py

def main():

        # Prompt the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Prompt the user to choose an operation
        operation = input("Choose the operation (+, -, *, /): ").strip()

        # Perform the calculation using match-case
        match operation:
            case '+':
                result = num1 + num2
                print(f"The result is {result}.")
            case '-':
                result = num1 - num2
                print(f"The result is {result}.")
            case '*':
                result = num1 * num2
                print(f"The result is {result}.")
            case '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}.")
            case _:
                print("Invalid operation. Please choose one of (+, -, *, /).")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

