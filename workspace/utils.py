#!/usr/bin/env python3
"""
Utility functions for the Factorial Calculator application.
"""

def calculate_factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Handle special cases
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial iteratively
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result