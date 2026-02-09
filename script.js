import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)

        self.current = ""
        self.operator = None
        self.first_number = None

        self.display = tk.Entry(
            root,
            font=("Segoe UI", 22),
            bd=10,
            relief="flat",
            justify="right"
        )
        self.display.pack(fill="both", padx=10, pady=15, ipady=15)

        self.create_buttons()

    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [
            ("AC", 1, 0), ("⌫", 1, 1), ("%", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(
                frame,
                text=text,
                font=("Segoe UI", 14),
                width=5,
                height=2,
                command=lambda t=text: self.on_press(t)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

        frame.grid_columnconfigure(0, weight=1)

    def on_press(self, key):
        if key.isdigit() or key == ".":
            self.current += key
            self.update_display(self.current)

        elif key in "+-*/":
            if self.current:
                self.first_number = float(self.current)
                self.operator = key
                self.current = ""

        elif key == "=":
            if self.current and self.operator:
                second = float(self.current)
                result = self.calculate(self.first_number, second, self.operator)
                self.update_display(result)
                self.current = str(result)
                self.operator = None

        elif key == "AC":
            self.clear()

        elif key == "⌫":
            self.current = self.current[:-1]
            self.update_display(self.current)

    def calculate(self, a, b, op):
        if op == "+": return a + b
        if op == "-": return a - b
        if op == "*": return a * b
        if op == "/": return "Error" if b == 0 else a / b

    def clear(self):
        self.current = ""
        self.operator = None
        self.first_number = None
        self.update_display("")

    def update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, value)


# Run app
root = tk.Tk()
Calculator(root)
root.mainloop()
