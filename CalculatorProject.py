# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:17:13 2023

@author: jil12
"""

import tkinter as tk
from math import sqrt
#ttk to be able to use the combobox
import tkinter.ttk

# main class
class CalculatorProject:
    # Constructor (__init__) method for CalculatorProject class
    def __init__(self):
        # Create the main window
        self.main_window = tk.Tk()
        # Sets the width and height of the calculator window
        self.main_window.geometry("380x600")
        # Sets the title of the calculator window
        self.main_window.title('Calculator')
        
        #Make it so the window cannot be resized 
        self.main_window.resizable(height=False, width=False)
        
        #Change color of background 
        self.main_window.configure(background = 'white')
        # Creates an entry widget for display
        self.display = tk.Entry(self.main_window, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        #Second entry widget for conversion results 
        self.display1 = tk.Entry(self.main_window, width=14)
        self.display1.grid(row=11, column=0, sticky='W')
        
        # Variable to store the current expression
        self.current_expression = ""

        # List to store calculation history
        self.history = []
        # ---------------------------------------------------------------------
        # Button click event for numeric buttons
        def button_click(number):
            self.current_expression += str(number)
            # Update the display with the updated current expression
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_expression)

        # Clear event
        def button_clear():
            # Reset the current expression to an empty string
            self.current_expression = ""
            # Clear the display by deleting its content
            self.display.delete(0, tk.END)

        # Operator events (including square root)
        def button_operator(operator):
            # Check if the operator is the square root symbol
            if operator == "√":
                # If it is, call the button_root function to handle square root operations
                self.button_root()
            # Otherwise: 
            else:
                # If the operator is not the square root symbol:
                # Append the operator to the current expression
                self.current_expression += operator
                # Update the display with the updated current expression
                self.display.delete(0, tk.END)
                self.display.insert(0, self.current_expression)

        # Square Root event
        def button_root():
            # Get the current text from the display entry widget
            current_text = self.display.get()

            # Check if the current text is just the square root symbol
            if current_text == "√":
                # If so, update the display to show only the square root symbol
                self.display.delete(0, tk.END)
                self.display.insert(0, "√")
            # Otherwise: 
            else:
                # Try Block
                try:
                    # Convert the current text to a float for calculation
                    first_number = float(current_text)
                    # Calculate the square root using the sqrt function
                    result = sqrt(first_number)
                    # Update the display with the result
                    self.display.delete(0, tk.END)
                    self.display.insert(0, result)
                    # Update the current expression with the result
                    self.current_expression = str(result)
                    # Add the calculation to the history
                    self.history.append(f"{current_text} = {result}")
                # Except Block
                except ValueError:
                    # Handle the case where the input is not a valid number
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
                    self.current_expression = ""
        
        
        # Button Conversion event
        def button_conversion():
            # If statement for when the from currency is set to USD 
            if from_combo.get() == 'USD':
                #If  statesment for when from is USD and to is USD
                if to_combo.get() == 'USD':
                    #This will create a variable and will get it from the display field with .get()
                    conversion_results = self.display1.get()
                #If  statement for when from is USD and to is EU    
                elif to_combo.get() == 'EU':
                    conversion_results = float(self.display1.get()) * 0.92
                #If  statement for when from is USD and to is YEN    
                elif to_combo.get() == 'YEN':
                    conversion_results = float(self.display1.get()) * 146
            # IF statement for when from field is set to EU 
            elif from_combo.get() == 'EU':
                #If statment if from is set to EU and to is set to EU 
                    if to_combo.get() == 'EU':
                        conversion_results = self.display1.get()
                    #If statment if from is set to EU and to is set to USD    
                    elif to_combo.get() == 'USD':
                        conversion_results = float(self.display1.get()) * 1.09
                    #If statment if from is set to EU and to is set to YEN    
                    elif to_combo.get() == 'YEN':
                        conversion_results = float(self.display1.get()) * 159
            #Else statement is for the last condition which is if from field is set to YEN            
            else:
                #If from is set to yen and to field is set to yen 
                if to_combo.get() == 'YEN':
                    conversion_results = self.display1.get()
                #If from is set to yen and to field is set to USD    
                elif to_combo.get() == 'USD':
                    conversion_results = float(self.display1.get()) * 0.0068
                #If from is set to yen and to field is set to EU
                elif to_combo.get() == 'EU':
                    conversion_results = float(self.display1.get()) * 0.0063
            # This will format the results into a formatted string  
            outcome_results = f'{self.display1.get()} {from_combo.get()} = {conversion_results} {to_combo.get()}'
            # This will set the results label to the conversion_results
            result_label.config(text=outcome_results)
            #This statment will add conversion to the history window 
            self.history.append(f"{from_combo.get()} {self.display1.get()} = {to_combo.get()} {conversion_results}")
        
        # Button Equal event
        def button_equal():
            # Try block
            try:
                # Retrieve the current expression from the instance variable
                expression = self.current_expression
                # Evaluate the expression using the eval function
                result = eval(expression)
                # Clear the current display
                self.display.delete(0, tk.END)
                # Update the display with the result of the evaluation
                self.display.insert(0, result)
                # Update the current expression to store the result as a string
                self.current_expression = str(result)
                # Add the calculation to the history
                self.history.append(f"{expression} = {result}")
            # Except Block
            except Exception as e:
                # Update the display with the updated current expression
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.current_expression = ""
        # ---------------------------------------------------------------------        
        # Show history in a separate window
        def show_history():
            # Create a new window
            # Use Toplevel widget class to create an additional window for the history (pop up screen)
            history_window = tk.Toplevel(self.main_window)
            history_window.title("Calculation History")

            # Display history in a label
            history_label = tk.Label(history_window, text="\n".join(self.history), padx=40, pady=40)
            history_label.pack()
        # ---------------------------------------------------------------------
        # Define buttons on click (0-9)
        button_1 = tk.Button(self.main_window, text="1", bg='lime green', padx=40, pady=20, command=lambda: button_click(1))
        button_2 = tk.Button(self.main_window, text="2", bg='lime green', padx=40, pady=20, command=lambda: button_click(2))
        button_3 = tk.Button(self.main_window, text="3", bg='lime green', padx=40, pady=20, command=lambda: button_click(3))
        button_4 = tk.Button(self.main_window, text="4", bg='lime green', padx=40, pady=20, command=lambda: button_click(4))
        button_5 = tk.Button(self.main_window, text="5", bg='lime green', padx=40, pady=20, command=lambda: button_click(5))
        button_6 = tk.Button(self.main_window, text="6", bg='lime green', padx=40, pady=20, command=lambda: button_click(6))
        button_7 = tk.Button(self.main_window, text="7", bg='lime green', padx=40, pady=20, command=lambda: button_click(7))
        button_8 = tk.Button(self.main_window, text="8", bg='lime green', padx=40, pady=20, command=lambda: button_click(8))
        button_9 = tk.Button(self.main_window, text="9", bg='lime green', padx=40, pady=20, command=lambda: button_click(9))
        button_0 = tk.Button(self.main_window, text="0", bg='lime green', padx=88, pady=20, command=lambda: button_click(0))
        # ---------------------------------------------------------------------
        # Button Padding for +, - , *, / 
        button_add = tk.Button(self.main_window, text="+", bg='lime green', padx=39, pady=20, command=lambda: button_operator("+"))
        button_subtract = tk.Button(self.main_window, text="-", bg='lime green', padx=40, pady=20, command=lambda: button_operator("-"))
        button_multiply = tk.Button(self.main_window, text="*", bg='lime green', padx=40, pady=20, command=lambda: button_operator("*"))
        button_divide = tk.Button(self.main_window, text="/", bg='lime green', padx=40, pady=20, command=lambda: button_operator("/"))
        button_root = tk.Button(self.main_window, text="√", bg='lime green', padx=40, pady=20, command=button_root)
        # Button Padding for Clear and =
        button_clear = tk.Button(self.main_window, text="Clear", bg='lime green', padx=77, pady=20, command=button_clear)
        equal_button = tk.Button(self.main_window, text="=", bg='lime green', padx=39, pady=20, command=button_equal)
        button_history = tk.Button(self.main_window, text="History", bg='lime green', padx=26, pady=20, command=show_history)
        # ---------------------------------------------------------------------
        # Label for Currency 
        currency_label = tk.Label(self.main_window, text='Currency Converter', pady=10, padx=60, font=('Poppins 20 bold'), bg='green4')
        # Label for "FROM"
        from_currency_label = tk.Label(self.main_window, text='FROM:', font=('Poppins 10 bold'), bg='white')
        # Label for "TO:"
        to_currency_label = tk.Label(self.main_window, text='TO:', font=('Poppins 10 bold'), bg='white')
        
        # Combobox for "FROM" field in the currency conversion field 
        from_combo = tkinter.ttk.Combobox(self.main_window, width=10, font=('Poppins 10 bold'), values=('USD','EU','YEN'))
        from_combo.grid(row=9, column=0, sticky= 'W')
        # Combobox for "TO" field in the currency conversion field 
        to_combo = tkinter.ttk.Combobox(self.main_window, width=10, font=('Poppins 10 bold'), values=('USD','EU','YEN'))
        to_combo.grid(row=9, column=2, sticky= 'W')
        
        # "AMOUNT" label to signal where to enter conversion ammount 
        ammount_currency_label = tk.Label(self.main_window, text='AMOUNT:', font=('Poppins 10 bold'), bg='white')
        # Empty LABEL that through button_conversion() will be filled with conversion results.
        result_label = tk.Label(self.main_window, text='', font=('Poppins 10 bold'))
        result_label.grid(row=13, column=0, sticky='W', pady=5, columnspan=4)
        outcome_results = f'{self.display1.get()} {from_combo.current(0)} =  {to_combo.current(0)}'
        
        
        # Conversion Button: click to run the button_conversion() function
        convert_button = tk.Button(self.main_window, text="CONVERT", bg='dodger blue', fg='white', font=('Poppins 10 bold'), command=button_conversion)
        convert_button.grid(row=12, column=0, sticky='W', pady=5)
        
        

        # ---------------------------------------------------------------------
        # Place buttons on the screen
        # first row buttons
        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)
        button_divide.grid(row=1, column=3)
        # second row buttons
        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)
        button_multiply.grid(row=2, column=3)
        # third row buttons
        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)
        button_subtract.grid(row=3, column=3)
        # fourth row buttons
        button_0.grid(row=4, column=0, columnspan=2)
        button_add.grid(row=4, column=3)
        # fifth row button CLEAR
        button_clear.grid(row=5, column=0, columnspan=2)
        equal_button.grid(row=5, column=3)
        button_history.grid(row=5, column=2)
        # Square Root button
        button_root.grid(row=4, column=2)
        # Currency conversion buttons 
        currency_label.grid(row=7, column=0, columnspan=4)
        from_currency_label.grid(row=8, column=0,  sticky= 'W')
        to_currency_label.grid(row=8, column=2, sticky= 'W')
        
        # Grid statement for ammount label
        ammount_currency_label.grid(row=10, column=0,  sticky= 'W')
        # ---------------------------------------------------------------------
        # main window loop
        self.main_window.mainloop()

# Run the calculator
if __name__ == '__main__':
    project = CalculatorProject()
