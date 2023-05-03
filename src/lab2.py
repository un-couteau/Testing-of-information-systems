from math import cos, pow, sqrt

# def task_one(name: str = None, college: str = None, college_group: str = None, language: str = None):
#     output_options: [str] = ["– Как Вас зовут?", "– Добрый день, ", "– Укажите названия техникума.",
#                              "– Укажите номер вашей группы.",
#                              ["– Вы обучаетесь в образовательной организации, ", "в группе " ],
#                              "– Какой язык программирования вы начинаете изучать?",
#                              ]
def task_one():
    name: str = input("– Как Вас зовут?\n")
    print(f"– Добрый день, {name}")
    college: str = input("– Укажите названия техникума.\n")
    print(college)
    college_group: str = input("– Укажите номер вашей группы.\n")
    print(f"{college_group}\n"
          f"– Вы обучаетесь в образовательной организации {college}"
          f" в группе {college_group}")
    language: str = input("– Какой язык программирования вы начинаете изучать?\n")
    print(f"{language}\n"
          f"– {name}, желаем Вам успешного обучения программированию на"
          f" языке {language}")


def task_two(a: float = 1.5, b: float = 15.5, x: float = -2.9) -> float:
    if input("Хотите изменить начальные значение?\nЕсли нет, то нажмите пробел\n"):
        a, b, x = list(map(float, input("Введите значения для a, b, x через пробел:\n").split()))
    return cos(pow(x, 3)) - x / sqrt(pow(a, 2) + pow(b, 2))


def lab2() -> None:
    task_one()
    print(task_two())
