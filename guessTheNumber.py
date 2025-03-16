import random
def load_best_score():
    try:
        with open("best_score.txt") as file:
            return int(file.read())
    except (FileNotFoundError, ValueError):
        return float("inf")
def save_best_score(score):
    with open("best_score.txt", "w") as file:
        file.write(str(score))
best_score = load_best_score()
while True:  
    secretNumber = random.randint(1, 100)
    attempts = 0
    if best_score != float("inf"):
        print(f"Лучший результат: {best_score} попыток")
    print("если не ссышь угадай число!")
    print()

    while True:
        try:
            guess = int(input("Угадай число от 1 до 100: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("число вне диапазона")
                continue
            if guess == secretNumber:
                print("Ты угадал! тебе понадобилось", attempts, "попыток")
                if attempts < best_score:
                    best_score = attempts
                    save_best_score(best_score)
                    print("Поздравляю! Новый рекорд!")
                    break
            elif guess < secretNumber:
                print("загаданное число больше")
            else:
                print("загаданное число меньше")
        except ValueError:
            print("введи целое число")
        print()


    while True:
        playAgain = input("сыграем еще? (да/нет): ").lower().strip()
        if playAgain in ["да", "нет"]:
            break
        print("Пожалуйста, введи 'да' или 'нет'!")

    if playAgain == "нет":
        print("давай пока")
        break

    print()