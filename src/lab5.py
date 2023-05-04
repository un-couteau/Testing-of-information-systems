def task_one() -> list[str]:
    list_of_integers = list()
    user_choice: str = ''

    while user_choice != "0":
        user_choice: str = input("Введите число: ")
        list_of_integers.append(user_choice)

    del list_of_integers[-1]
    list_of_integers.reverse()

    return list_of_integers


def task_two() -> list[int] | int:
    user_int_input: str = input("Введите целое число: ")
    result: list[int] = list()

    while not user_int_input.isdigit():
        user_int_input = input("Ошибка!\nВведите целое число: ")

    for i in range(int(user_int_input)):
        if i > 1000 and i % 3 == 0:
            result.append(i)

    if result:
        # print(result) # включите для проверки чисел, которые имеет 4 знака и кратны 3
        return sum(result)
    return 0


def lab5():
    print(task_one())
    print(task_two())
