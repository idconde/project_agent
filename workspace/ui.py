#!/usr/bin/env python3
"""
GUI logic for the Factorial Calculator application.
"""

import tkinter as tk
from tkinter import ttk
from utils import calculate_factorial

class FactorialCalculatorGUI:
    """
    GUI class for the factorial calculator application.
    """
    
    def __init__(self):
        """
        Initialize the GUI components and window.
        """
        self.root = tk.Tk()
        self.root.title("Factorial Calculator")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        
        self.setup_components()
    
    def setup_components(self):
        """
        Set up all GUI components and their layout.
        """
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input label
        input_label = ttk.Label(main_frame, text="Enter a number:")
        input_label.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)
        
        # Input field
        self.number_entry = ttk.Entry(main_frame, width=20, font=('Arial', 12))
        self.number_entry.grid(row=1, column=0, pady=(0, 20), sticky=(tk.W, tk.E))
        
        # Calculate button
        self.calculate_button = ttk.Button(main_frame, text="Calculate", command=self.calculate_factorial)
        self.calculate_button.grid(row=2, column=0, pady=(0, 20))
        
        # Result label
        self.result_label = ttk.Label(main_frame, text="Result will appear here", font=('Arial', 10), wraplength=350)
        self.result_label.grid(row=3, column=0, pady=(0, 10), sticky=(tk.W, tk.E))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Bind Enter key to calculate button
        self.root.bind('<Return>', lambda event: self.calculate_factorial())
    
    def calculate_factorial(self):
        """
        Handle the calculate button click event.
        """
        try:
            # Get input from entry field
            input_text = self.number_entry.get().strip()
            
            if not input_text:
                self.result_label.config(text="Error: Please enter a number")
                return
            
            # Convert to integer
            number = int(input_text)
            
            # Calculate factorial
            result = calculate_factorial(number)
            
            # Display result
            self.result_label.config(text=f"Factorial of {number} is: {result}")
            
        except ValueError:
            self.result_label.config(text="Error: Please enter a valid integer")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
    
    def run(self):
        """
        Start the GUI application main loop.
        """
        self.root.mainloop()