import tkinter as tk

# Function to update expression in the text entry box
def click(button_text):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button_text)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to show expressions
entry = tk.Entry(root, width=25, font=('Arial', 18), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == '=':
            btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=calculate)
        else:
            btn = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: click(t))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text='C', width=21, height=2, font=('Arial', 18), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Start the GUI loop
root.mainloop()
