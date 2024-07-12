def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Non-numeric input. Please enter valid numbers."

    try:
        if denominator == 0:
            return "Error: Division by zero is not allowed."
        else:
            return numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

    import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv)!= 3:
        print("Usage: python main.py <numerator> <denominator>")
        return

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)

    print(result)

if __name__ == "__main__":
    main()
