import tkinter as tk
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#d2b48c")
        self.entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=5, pady=10, padx=10)

        buttons = [
            ('√', 1, 0), ('x²', 1, 1), ('^', 1, 2), ('(', 1, 3), (')', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('DEL', 2, 3), ('AC', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3), ('/', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3), ('-', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('00', 5, 2), ('=', 5, 3, 1, 2),
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            rowspan = btn[3] if len(btn) > 3 else 1
            colspan = btn[4] if len(btn) > 4 else 1
            self.create_button(text, row, col, rowspan, colspan)

    def create_button(self, text, row, col, rowspan, colspan):
        btn = tk.Button(
            self.root,
            text=text,
            font="Arial 10 bold",
            width=3,
            height=1,
            bg="#000000" if text not in ['=', 'AC', 'DEL'] else "#d87b6d",
            fg="white",
            command=lambda: self.on_click(text)
        )
        btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=3, pady=3)

    def on_click(self, char):
        if char == 'AC':
            self.entry.delete(0, tk.END)
        elif char == 'DEL':
            self.entry.delete(len(self.entry.get()) - 1)
        elif char == '=':
            try:
                result = eval(self.entry.get().replace('√', 'math.sqrt').replace('^', '').replace('x²', '**2'))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)