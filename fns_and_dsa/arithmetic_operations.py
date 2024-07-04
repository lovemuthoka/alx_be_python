def perform_operation(num1: float, num2: float, operation: str) -> float:
    """
    Perform an arithmetic operation on two numbers based on the operation parameter.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Can be 'add', 'ubtract', 'ultiply', or 'divide'.

    Returns:
        float: The result of the arithmetic operation. If division by zero, returns 'Error: Division by zero'.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'ubtract':
        return num1 - num2
    elif operation == 'ultiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Error: Division by zero'
        else:
            return num1 / num2
    else:
        raise ValueError("Invalid operation. Must be 'add', 'ubtract', 'ultiply', or 'divide'.")
