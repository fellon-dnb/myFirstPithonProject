import subprocess

class JCalculator:
    def __init__(self):
        self.result = 0

    def calculate(self, number1, number2, operation):

        try:
            # Подготавливаем входные данные
            input_data = f"{number1}\n{number2}\n{operation}\n"
            # Вызываем Java-программу
            process = subprocess.run(
                ["java", "JavaCalculator"],
                input=input_data,
                text=True,
                capture_output=True,
                cwd="D:\\WorkSpace\\myFirstPithonProject"
            )


            if process.returncode != 0:
                error_message = process.stderr.strip()
                if "ArithmeticException" in error_message:
                    raise ZeroDivisionError("ошибка, на ноль не делим")
                elif "IllegalArgumentException" in error_message:
                    raise ValueError("неправильная операция")
                raise ValueError(error_message)


            self.result = float(process.stdout.strip())
            return self.result
        except ValueError as e:
            raise ValueError(str(e))
        except subprocess.CalledProcessError as e:
            raise ValueError("Ошибка выполнения Java-программы")

if __name__ == "__main__":
    calc = JCalculator()
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