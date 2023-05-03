import math


def task_one(k: int) -> None:
    for i in range(k + 1):
        print(f"Корень числа {i} равен {round(math.sqrt(i), 1)}, а куб равен {math.pow(i, 3)}")
    return

def task_two():
    ...


def lab6():
    task_one(int(input("Введите целое число: ")))