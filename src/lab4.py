from math import pi, pow, sqrt, log
def task_one(integer: int) -> str | int:
    if integer > 0:
        return '+'
    if integer < 0:
        return '-'
    return 0


def task_two(x: float, a: float = 1.65) -> float:
    if x < 1.4:
        return round(pi * pow(x, 2) - 7 / pow(x, 2), 2)
    if x == 1.4:
        return round(a * pow(x, 3) + 7 * sqrt(x), 2)
    return round(log(x) + 7 * sqrt(abs(x + a)), 2)


def lab4():
    print(task_one(int(input("Введите целое число: "))))
    print(task_two(float(input("Введите число: "))))
