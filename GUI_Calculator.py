import tkinter as tk
from tkinter import messagebox
from jcalculator import JCalculator


class GUICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Мой Калькулятор")
        self.root.geometry("300x400")
        self.calc = JCalculator()

        tk.Label(self.root, text="Первое число:", font=('Arial', 12)).grid(row=0, column=0, padx=5, pady=5)
        self.entry1 = tk.Entry(self.root, width=15, font=('Arial', 12))
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Второе число:", font=('Arial', 12)).grid(row=1, column=0, padx=5, pady=5)
        self.entry2 = tk.Entry(self.root, width=15, font=('Arial', 12))
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Операция:", font=('Arial', 12)).grid(row=2, column=0, padx=5, pady=5)
        self.operation_var = tk.StringVar(value="+")
        operations = ["+", "-", "*", "/", "**"]
        operation_menu = tk.OptionMenu(self.root, self.operation_var, *operations)
        operation_menu.grid(row=2, column=1, padx=5, pady=5)

        # Кнопка расчёта
        tk.Button(self.root, text="=", width=10, height=2, font=('Arial', 12),
                  command=self.calculate).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        tk.Button(self.root, text="Очистить", width=10, height=2, font=('Arial', 12),
                  command=self.clear).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(self.root, text="Результат: ", font=('Arial', 12))
        self.result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def clear(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result_label.config(text="Результат: ")

    def calculate(self):
        try:
            number1 = self.entry1.get()
            number2 = self.entry2.get()
            operation = self.operation_var.get()
            result = self.calc.calculate(number1, number2, operation)
            self.result_label.config(text=f"Результат: {result}")
        except (ValueError, ZeroDivisionError) as e:
            messagebox.showerror("Ошибка", str(e))
            self.clear()


if __name__ == "__main__":
    root = tk.Tk()
    app = GUICalculator(root)
    root.mainloop() 
