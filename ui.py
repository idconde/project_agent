import tkinter as tk
from tkinter import ttk
from utils import calculate_factorial

class FactorialCalculatorApp:
    def __init__(self):
        self.window = tk.Tk()
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        self.window.title("Factorial Calculator")
        self.window.geometry("300x200")
        self.window.resizable(False, False)
        
    def create_widgets(self):
        # Input field
        tk.Label(self.window, text="Enter a number:").pack(pady=10)
        self.input_field = tk.Entry(self.window, width=20)
        self.input_field.pack(pady=5)
        
        # Calculate button
        self.calculate_button = tk.Button(
            self.window, 
            text="Calculate", 
            command=self.calculate_factorial
        )
        self.calculate_button.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(
            self.window, 
            text="Result will appear here", 
            wraplength=250
        )
        self.result_label.pack(pady=10)
        
    def calculate_factorial(self):
        try:
            input_text = self.input_field.get().strip()
            
            if not input_text:
                self.result_label.config(text="Please enter a number")
                return
                
            number = int(input_text)
            result = calculate_factorial(number)
            self.result_label.config(text=f"Factorial of {number} is: {result}")
            
        except ValueError:
            self.result_label.config(text="Please enter a valid integer")
        except Exception as e:
            self.result_label.config(text=str(e))
            
    def run(self):
        self.window.mainloop()