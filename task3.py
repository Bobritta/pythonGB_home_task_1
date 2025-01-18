#  Программа загадывает число от 0 до 1000.
#  Необходимо угадать число за 10 попыток.
#  Программа должна подсказывать “больше” или “меньше” после каждой попытки.
#  Для генерации случайного числа используйте код:
#  from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

while True:
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    # print(num)

    attempt_limit = 10
    print("Загадано целое число в промежутке от 0 до 1000")
    while attempt_limit > 0:
        attempt = input(f"У вас осталось {attempt_limit} попыток. Угадайте число:\n")

        try:
            attempt = int(attempt)
        except ValueError:
            print("Пожалуйста, введите одно целое число цифрами.")
            continue

        if attempt == num:
            print(f"Ура! Вы угадали! Это действительно {num}")
            break
        else:
            print("К сожалению, это не то, что я загадал")
            if attempt>num:
                print("Загаданное число меньше")
            else:
                print("Загаданное число больше")

        attempt_limit -= 1

    if attempt_limit == 0:
        print(f"Попытки исчерпаны. Загаданное число было {num}.")

    once_more = input("Хотите сыграть ещё раз? Введите 1 (да, хочу) или 2 (нет, не хочу):\n")
    try:
        once_more = int(once_more)
    except ValueError:
        print("Пожалуйста, введите 1 (да, хочу) или 2 (нет, не хочу):\n")
        continue

    if once_more == 2:
        print("Спасибо за игру!")
        break