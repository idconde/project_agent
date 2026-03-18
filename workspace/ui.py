import tkinter as tk
from tkinter import messagebox
from utils import calculate_factorial

class FactorialApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Factorial Calculator")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Input label
        input_label = tk.Label(self.root, text="Enter a number:")
        input_label.pack(pady=10)
        
        # Input field
        self.entry = tk.Entry(self.root, width=20)
        self.entry.pack(pady=5)
        
        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_factorial)
        calculate_button.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(self.root, text="Result will appear here", wraplength=250)
        self.result_label.pack(pady=10)
    
    def calculate_factorial(self):
        try:
            input_text = self.entry.get().strip()
            
            if not input_text:
                self.result_label.config(text="Error: Please enter a number")
                return
            
            number = int(input_text)
            result = calculate_factorial(number)
            self.result_label.config(text=f"Factorial of {number} is: {result}")
            
        except ValueError:
            self.result_label.config(text="Error: Please enter a valid integer")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
    
    def run(self):
        self.root.mainloop()