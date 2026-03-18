import tkinter as tk
from tkinter import messagebox
from utils import calculate_factorial

class FactorialCalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Factorial Calculator")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Input field label
        input_label = tk.Label(self.root, text="Enter a number:", font=("Arial", 12))
        input_label.pack(pady=10)
        
        # Input field
        self.number_entry = tk.Entry(self.root, font=("Arial", 12), width=20, justify="center")
        self.number_entry.pack(pady=5)
        self.number_entry.bind("<Return>", lambda event: self.calculate_button_click())
        
        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate", font=("Arial", 12), 
                                   command=self.calculate_button_click, bg="lightblue")
        calculate_button.pack(pady=10)
        
        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), 
                                   wraplength=280, justify="center")
        self.result_label.pack(pady=10)
    
    def calculate_button_click(self):
        try:
            # Get input value
            input_value = self.number_entry.get().strip()
            
            if not input_value:
                self.result_label.config(text="Please enter a number", fg="red")
                return
            
            # Convert to integer
            number = int(input_value)
            
            # Calculate factorial
            result = calculate_factorial(number)
            
            if isinstance(result, str):  # Error message
                self.result_label.config(text=result, fg="red")
            else:
                self.result_label.config(text=f"Factorial of {number} is: {result}", fg="green")
                
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid integer.", fg="red")
        except Exception as e:
            self.result_label.config(text=f"An error occurred: {str(e)}", fg="red")
    
    def run(self):
        self.root.mainloop()