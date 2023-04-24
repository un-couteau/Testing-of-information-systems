from random import randint
from math import prod


def red_print(string: str) -> str:
    print(f"\033[31m{string}\033[0m")


def number_one() -> None:
    red_print("Первое задание")
    print("Привет, Python\nПриятно познакомится")


def number_two(film: str, cinema: str, time: str) -> str:
    red_print("Второе задание")
    return f"Билет на {film} в {cinema} на {time} забронирован"


def number_three(*args: int) -> str:
    args = list(args)
    red_print("Третье задание")
    return f"Сумма: {sum(args)}\n" \
           f"Произведение: {prod(args)}\n" \
           f"Среднее арифметическое: {sum(args) / len(args)}"


def number_four():
    red_print("Четвертое задание")
    random: str = str(randint(100, 1000))

    return f"{', '.join(random)}"


def number_five(money: float, amount: int) -> str:
    red_print("Пятое задание")
    return f"К оплате {money * amount} рублей"
