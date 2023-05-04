from random import randint
from math import prod

works_counter = 1


def red_print_decorator(func):
    def wrapper(*args, **kwargs):
        global works_counter
        works_counter
        print(f"\033[31m{works_counter} Задание\033[0m")
        func()
        works_counter += 1
        return func

    return wrapper


# @red_print_decorator
def number_one() -> None:
    print("Привет, Python\nПриятно познакомится")


# @red_print_decorator
def number_two(film: str, cinema: str, time: str) -> str:
    return f"Билет на {film} в {cinema} на {time} забронирован"


# @red_print_decorator
def number_three(*args: int) -> str:
    args = list(args)
    return f"Сумма: {sum(args)}\n" \
           f"Произведение: {prod(args)}\n" \
           f"Среднее арифметическое: {sum(args) / len(args)}"


# @red_print_decorator
def number_four() -> str:
    random: str = str(randint(100, 1000))

    return f"{', '.join(random)}"


# @red_print_decorator
def number_five(money: float, amount: int) -> str:
    return f"К оплате {money * amount} рублей"


def lab1():
    number_one()
    print(number_two(input("Введите название фильма: "), input("Введите название кинотеатра: "),
                     input("Введите время: ")))
    print(number_three(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
                       int(input("Введите третье число: "))))
    print(number_four())
    print(number_five(float(input("Введите ценник товара: ")), int(input("Введите кол-во товара: "))))
