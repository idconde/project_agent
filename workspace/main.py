#!/usr/bin/env python3
"""
Entry point for the Factorial Calculator application.
"""

from ui import FactorialCalculatorGUI

def main():
    """
    Main function to start the factorial calculator application.
    """
    app = FactorialCalculatorGUI()
    app.run()

if __name__ == "__main__":
    main()