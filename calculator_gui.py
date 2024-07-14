import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import messagebox

# The rest of your code...

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

def on_button_click(char):
    current_text = display.get()
    new_text = current_text + str(char)
    display.set(new_text)

def on_clear():
    display.set("")

def on_equals():
    expression = display.get()
    result = evaluate_expression(expression)
    display.set(result)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar to hold the display text
display = tk.StringVar()

# Create the display entry
entry = tk.Entry(root, textvariable=display, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                       command=lambda t=text: on_button_click(t) if t != '=' else on_equals())
    button.grid(row=row, column=col)

# Add clear button
clear_button = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 18), command=on_clear)
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Start the main event loop
root.mainloop()
