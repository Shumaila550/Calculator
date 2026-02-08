import tkinter as tk

class MobileCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mobile Calculator")
        self.geometry("320x450")
        self.resizable(False, False)

        # Calculator state
        self.current = "0"
        self.previous = None
        self.operator = None
        self.new_input = True

        self.create_display()
        self.create_buttons()
        self.update_display()

    def create_display(self):
        self.display = tk.Entry(
            self,
            font=("Segoe UI", 24),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        self.display.pack(fill="x", padx=10, pady=10)

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)

    def create_buttons(self):
        layout = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "⌫", "+"],
            ["AC", "="]
        ]

        frame = tk.Frame(self)
        frame.pack()

        for r, row in enumerate(layout):
            for c, btn in enumerate(row):
                tk.Button(
                    frame,
                    text=btn,
                    width=7 if btn in ["AC", "="] else 5,
                    height=2,
                    font=("Segoe UI", 14),
                    command=lambda b=btn: self.press(b)
                ).grid(row=r, column=c, padx=5, pady=5,
                       columnspan=2 if btn in ["AC", "="] else 1)

    def press(self, key):
        if key.isdigit():
            self.input_digit(key)
        elif key == ".":
            self.input_decimal()
        elif key in "+-*/":
            self.set_operator(key)
        elif key == "=":
            self.calculate()
        elif key == "AC":
            self.clear_all()
        elif key == "⌫":
            self.backspace()

        self.update_display()

    def input_digit(self, digit):
        if self.new_input:
            self.current = digit
            self.new_input = False
        else:
            self.current += digit

    def input_decimal(self):
        if "." not in self.current:
            self.current += "."

    def set_operator(self, op):
        if self.operator:
            self.calculate()
        self.previous = float(self.current)
        self.operator = op
        self.new_input = True

    def calculate(self):
        if self.operator is None:
            return

        try:
            current_value = float(self.current)

            if self.operator == "+":
                result = self.previous + current_value
            elif self.operator == "-":
                result = self.previous - current_value
            elif self.operator == "*":
                result = self.previous * current_value
            elif self.operator == "/":
                if current_value == 0:
                    raise ZeroDivisionError
                result = self.previous / current_value

            self.current = str(result).rstrip("0").rstrip(".")
            self.operator = None
            self.new_input = True

        except ZeroDivisionError:
            self.current = "Error"
            self.operator = None
            self.new_input = True

    def clear_all(self):
        self.current = "0"
        self.previous = None
        self.operator = None
        self.new_input = True

    def backspace(self):
        if not self.new_input and len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"


if __name__ == "__main__":
    MobileCalculator().mainloop()
