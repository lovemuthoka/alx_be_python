def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator 

        print(f"This division is: {result}")

    except ZeroDivisionError:
        print("Error:Division by zero is not allowed .")
        
    except ValueError:
        print("Error:Non-numeric input is not allowed. Please enter numeric values.")

safe_divide(20,16)    
