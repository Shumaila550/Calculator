import tkinter as tk

# Create main window
app = tk.Tk()
app.title("Professional Calculator")
app.geometry("320x420")
app.resizable(False, False)

expression = ""

# Functions
def press(key):
    global expression
    expression += str(key)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def calculate():
    global expression
    try:
        result = eval(expression)
        display_var.set(f"{expression} = {result}")
        expression = str(result)
    except:
        display_var.set("Error")
        expression = ""

# Display
display_var = tk.StringVar()
display = tk.Entry(
    app,
    textvariable=display_var,
    font=("Arial", 18),
    bd=10,
    relief="sunken",
    justify="right"
)
display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Buttons frame
frame = tk.Frame(app)
frame.pack()

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(
            frame, text=text, width=5, height=2,
            font=("Arial", 14),
            command=calculate
        )
    else:
        btn = tk.Button(
            frame, text=text, width=5, height=2,
            font=("Arial", 14),
            command=lambda t=text: press(t)
        )
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(
    app, text="CLEAR", font=("Arial", 14),
    command=clear, bg="#ff6666"
)
clear_btn.pack(fill="x", padx=10, pady=10)

app.mainloop()
