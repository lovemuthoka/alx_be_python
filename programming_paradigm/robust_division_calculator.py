def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator 

        print(f"The result of division is {result}")

    except ZeroDivisionError:
        print("Error:Cannot divide by zero.")
        
    except ValueError:
        print(" Please enter numeric values.")

safe_divide(20,16)    
