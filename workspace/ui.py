import tkinter as tk
from tkinter import ttk
from utils import calculate_factorial

class FactorialApp:
    """GUI application for calculating factorials."""
    
    def __init__(self):
        """Initialize the GUI components."""
        self.root = tk.Tk()
        self.root.title("Factorial Calculator")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.setup_widgets()
    
    def setup_widgets(self):
        """Create and arrange all GUI widgets."""
        # Input label
        input_label = tk.Label(self.root, text="Enter a number:")
        input_label.pack(pady=10)
        
        # Input field
        self.entry = tk.Entry(self.root, width=20, justify='center')
        self.entry.pack(pady=5)
        
        # Calculate button
        self.calculate_button = tk.Button(
            self.root, 
            text="Calculate", 
            command=self.handle_calculate,
            width=15
        )
        self.calculate_button.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(
            self.root, 
            text="", 
            wraplength=280,
            justify='center'
        )
        self.result_label.pack(pady=10)
        
        # Bind Enter key to calculate button
        self.root.bind('<Return>', lambda event: self.handle_calculate())
    
    def handle_calculate(self):
        """Handle the calculate button click event."""
        try:
            # Get input value
            input_text = self.entry.get().strip()
            
            # Check if input is empty
            if not input_text:
                self.result_label.config(text="Please enter a number")
                return
            
            # Convert to integer
            try:
                number = int(input_text)
            except ValueError:
                self.result_label.config(text="Please enter a valid integer")
                return
            
            # Check for negative numbers
            if number < 0:
                self.result_label.config(text="Please enter a non-negative integer")
                return
            
            # Calculate factorial
            result = calculate_factorial(number)
            self.result_label.config(text=f"Factorial of {number} is: {result}")
            
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
    
    def run(self):
        """Start the GUI application."""
        self.root.mainloop()