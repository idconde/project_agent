def calculate_factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number to calculate factorial for
    
    Returns:
        int or str: The factorial result or error message
    """
    
    # Input validation
    if not isinstance(n, int):
        return "Input must be an integer"
    
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result