def task_one() -> list[str]:
    list_of_integers = list()
    user_choise: str = ''

    while user_choise != "0":
        user_choise: str = input("Введите число: ")
        list_of_integers.append(user_choise)

    del list_of_integers[-1]
    list_of_integers.reverse()

    return list_of_integers


def task_two() -> list[int] | int:
    user_int_input: str = input("Введите минимум 4-значное число: ")
    result: list[int] = list()

    while len(user_int_input) < 4:
        user_int_input = input("Ошибка!\nВведите минимум 4-значное число: ")

    for i in range(int(user_int_input)):
        if len(str(i)) == 4:
            if i % 3 == 0:
                result.append(i)

    if result:
        print(result)
        return sum(result)
    return 0

def lab5():
    print(task_one())
    print(task_two())