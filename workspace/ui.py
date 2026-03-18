import tkinter as tk
from tkinter import ttk
from utils import calculate_factorial

class FactorialApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Factorial Calculator")
        self.root.geometry("300x200")
        
        self.input_field = None
        self.result_label = None
        
        self.setup_gui()
    
    def setup_gui(self):
        # Input field
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Enter a number:").pack()
        self.input_field = tk.Entry(input_frame, width=20)
        self.input_field.pack(pady=5)
        
        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_factorial)
        calculate_button.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(self.root, text="Result will appear here", wraplength=250)
        self.result_label.pack(pady=10)
    
    def calculate_factorial(self):
        try:
            input_value = self.input_field.get().strip()
            
            if not input_value:
                self.result_label.config(text="Please enter a number")
                return
            
            number = int(input_value)
            
            if number < 0:
                self.result_label.config(text="Error: Factorial is not defined for negative numbers")
                return
            
            result = calculate_factorial(number)
            self.result_label.config(text=f"Factorial of {number} is: {result}")
            
        except ValueError:
            self.result_label.config(text="Error: Please enter a valid integer")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
    
    def run(self):
        self.root.mainloop()