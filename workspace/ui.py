import tkinter as tk
from tkinter import ttk
from utils import calculate_factorial

class FactorialApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Factorial Calculator")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input label
        input_label = ttk.Label(main_frame, text="Enter a number:")
        input_label.pack(pady=(0, 5))
        
        # Input field
        self.input_field = ttk.Entry(main_frame, width=20, justify="center")
        self.input_field.pack(pady=(0, 10))
        self.input_field.bind("<Return>", lambda event: self.calculate_clicked())
        
        # Calculate button
        self.calculate_button = ttk.Button(main_frame, text="Calculate", command=self.calculate_clicked)
        self.calculate_button.pack(pady=(0, 15))
        
        # Result label
        self.result_label = ttk.Label(main_frame, text="", wraplength=250, justify="center")
        self.result_label.pack()
        
        # Focus on input field
        self.input_field.focus()
    
    def calculate_clicked(self):
        try:
            input_value = self.input_field.get().strip()
            
            if not input_value:
                self.result_label.config(text="Please enter a number")
                return
            
            # Convert to integer
            number = int(input_value)
            
            # Calculate factorial
            result = calculate_factorial(number)
            
            if isinstance(result, str):  # Error message
                self.result_label.config(text=result)
            else:
                self.result_label.config(text=f"Factorial of {number} is: {result}")
                
        except ValueError:
            self.result_label.config(text="Please enter a valid integer")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
    
    def run(self):
        self.root.mainloop()