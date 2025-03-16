import tkinter as tk
from tkinter import messagebox
import pyperclip 
from jcalculator import JCalculator

class GUICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Мой Калькулятор с Java")
        self.root.geometry("350x600")
        self.root.configure(bg="#e8ecef")
        try:
            self.root.iconbitmap("D:\\WorkSpace\\myFirstPithonProject\\calculator_icon.ico")
        except tk.TclError:
            print("Не удалось загрузить иконку.")

        self.calc = JCalculator()
        self.history = []

        input_frame = tk.Frame(self.root, bg="#e8ecef", bd=2, relief="groove")
        input_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(input_frame, text="Первое число:", font=('Arial', 12, 'bold'), bg="#e8ecef", fg="#2c3e50").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry1 = tk.Entry(input_frame, width=15, font=('Arial', 12), bd=2, relief="sunken")
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Второе число:", font=('Arial', 12, 'bold'), bg="#e8ecef", fg="#2c3e50").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry2 = tk.Entry(input_frame, width=15, font=('Arial', 12), bd=2, relief="sunken")
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Операция:", font=('Arial', 12, 'bold'), bg="#e8ecef", fg="#2c3e50").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.operation_var = tk.StringVar(value="+")
        operations = ["+", "-", "*", "/", "**"]
        operation_menu = tk.OptionMenu(input_frame, self.operation_var, *operations)
        operation_menu.config(font=('Arial', 12), bg="#ffffff", fg="#2c3e50", bd=2, relief="sunken")
        operation_menu.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        button_frame = tk.Frame(self.root, bg="#e8ecef")
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="=", width=10, height=2, font=('Arial', 12, 'bold'),
                  command=self.calculate, bg="#28a745", fg="white", bd=2, relief="raised").pack(side="left", padx=5)

        tk.Button(button_frame, text="Очистить", width=10, height=2, font=('Arial', 12, 'bold'),
                  command=self.clear, bg="#dc3545", fg="white", bd=2, relief="raised").pack(side="left", padx=5)

        self.result_label = tk.Label(self.root, text="Результат: ", font=('Arial', 12, 'bold'), bg="#e8ecef", fg="#2c3e50")
        self.result_label.pack(pady=5)

        history_frame = tk.Frame(self.root, bg="#e8ecef", bd=2, relief="groove")
        history_frame.pack(pady=10, padx=10, fill="x")

        tk.Label(history_frame, text="История:", font=('Arial', 12, 'bold'), bg="#e8ecef", fg="#2c3e50").pack(anchor="w", padx=5)
        self.history_listbox = tk.Listbox(history_frame, width=30, height=3, font=('Arial', 10), bg="#ffffff", fg="#2c3e50", bd=2, relief="sunken")
        self.history_listbox.pack(pady=5, padx=5, fill="x")
        self.history_listbox.bind("<Double-1>", self.copy_to_clipboard)

        digit_frame = tk.Frame(self.root, bg="#e8ecef")
        digit_frame.pack(pady=10)

        row = 0
        col = 0
        for i in range(1, 10):
            tk.Button(digit_frame, text=str(i), width=5, height=2, font=('Arial', 12, 'bold'),
                      command=lambda x=i: self.button_click(x), bg="#007bff", fg="white", bd=2, relief="raised").grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 2:
                col = 0
                row += 1

        tk.Button(digit_frame, text="0", width=5, height=2, font=('Arial', 12, 'bold'),
                  command=lambda: self.button_click(0), bg="#007bff", fg="white", bd=2, relief="raised").grid(row=row, column=1, padx=2, pady=2)

    def button_click(self, number):
        active_entry = self.root.focus_get()
        if active_entry == self.entry1:
            self.entry1.insert(tk.END, str(number))
        elif active_entry == self.entry2:
            self.entry2.insert(tk.END, str(number))

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
            history_entry = f"{number1} {operation} {number2} = {result}"
            self.history.append(history_entry)
            self.history_listbox.insert(tk.END, history_entry)
        except (ValueError, ZeroDivisionError) as e:
            messagebox.showerror("Ошибка", str(e))
            self.clear()

    def copy_to_clipboard(self, event):

        selection = self.history_listbox.curselection()
        if selection:
            index = selection[0]
            text = self.history_listbox.get(index)
            pyperclip.copy(text)
            messagebox.showinfo("скопирывано ", "Скопировано в буфер обмена!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUICalculator(root)
    root.mainloop()