def task_one(integer: int) -> str | int:
    if integer > 0:
        return '+'
    if integer < 0:
        return '-'
    return 0


def task_two():
    pass


def lab4():
    print(task_one(int(input("Введите целое число: "))))
    task_two()
