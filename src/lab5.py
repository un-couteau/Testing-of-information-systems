def task_one() -> list[str]:
    list_of_integers = list()
    user_choise: str = ''

    while user_choise != "0":
        user_choise: str = input("Введите число: ")
        list_of_integers.append(user_choise)

    del list_of_integers[-1]
    list_of_integers.reverse()

    return list_of_integers


def task_two():
    ...


def lab5():
    print(task_one())
