class Calculator:
    def __init__(self):
        self.result = 0

    def calculate(self, number1, number2, operation):
        """Метод для выполнения вычислений."""
        try:
            number1 = float(number1)
            number2 = float(number2)

            if operation == "+":
                self.result = number1 + number2
            elif operation == "-":
                self.result = number1 - number2
            elif operation == "*":
                self.result = number1 * number2
            elif operation == "/":
                if number2 != 0:
                    self.result = number1 / number2
                else:
                    raise ZeroDivisionError("ошибка, на ноль не делим")
            elif operation == "**":
                self.result = number1 ** number2
            else:
                raise ValueError("неправильная операция")
            return self.result
        except ValueError as e:
            if "неправильная операция" in str(e):
                raise
            raise ValueError("введи корректные числа")

#
if __name__ == "__main__":
    calc = Calculator()
    while True:
        number1 = input("введи первый намбер: ")
        number2 = input("введи второй намбер: ")
        operation = input("выбери операцию(+, -, *, /, **): ")
        try:
            result = calc.calculate(number1, number2, operation)
            print("результат:", result)
        except (ValueError, ZeroDivisionError) as e:
            print(e)
        again = input("Хочешь продолжить? (да/нет): ")
        if again.lower() == "нет":
            break