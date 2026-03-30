import tkinter as tk
import math

root = tk.Tk()
root.title("Basic Python Calculator")
root.configure(bg="lightblue")
root.resizable(False, False)

display_var = tk.StringVar()

def click(item):
    current = display_var.get()
    display_var.set(current + str(item))

def clear():
    display_var.set("")

def calculate():
    expression = display_var.get()
    try:
        # Replace ^ with ** so Python understands the power operation
        expression = display_var.get().replace('^', '**')
        result = str(eval(expression))
        display_var.set(result)    
    except Exception:
        display_var.set("Error")

def square_root():
    try:
        number = float(display_var.get())
        if number < 0:
            display_var.set("Error")
        else:
            display_var.set(str(math.sqrt(number)))
    except Exception:
        display_var.set("Error")

def percentage():
    try:
        number = float(display_var.get())
        display_var.set(str(number / 100))
    except Exception:
        display_var.set("Error")

# --- Display Entry ---
# This is the "screen" of the calculator
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24), bg="#e8e8e8", fg="black", bd=10, justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

# --- Button Layout ---
# A list of tuples containing (Text, Row, Column)
buttons = [
    ('C', 1, 0), ('√', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('^', 5, 2), ('=', 5, 3)
]

# Create and place buttons using a loop
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, font=('Arial', 18), bg="#4caf50", fg="white", command=calculate, height=2, width=5)
    elif text == 'C':
        btn = tk.Button(root, text=text, font=('Arial', 18), bg="#f44336", fg="white", command=clear, height=2, width=5)
    elif text == '√':
        btn = tk.Button(root, text=text, font=('Arial', 18), bg="#2196f3", fg="white", command=square_root, height=2, width=5)
    elif text == '%':
        btn = tk.Button(root, text=text, font=('Arial', 18), bg="#2196f3", fg="white", command=percentage, height=2, width=5)
    else:
        # lambda is used here to pass the specific text of the button to the click function
        btn = tk.Button(root, text=text, font=('Arial', 18), bg="#ffffff", fg="black", command=lambda t=text: click(t), height=2, width=5)
    
    # Place the button in the grid
    btn.grid(row=row, column=col, padx=5, pady=5)

# --- Run the Application ---
root.mainloop()        