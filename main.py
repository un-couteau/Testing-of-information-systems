from src.lab1 import *


def main():
    number_one()
    print(number_two(input("Введите название фильма: "), input("Введите название кинотеатра: "), input("Введите время: ")))
    print(number_three(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
                       int(input("Введите третье число: "))))
    print(number_four())
    print(number_five(float(input("Введите ценник товара: ")), int(input("Введите кол-во товара: "))))


if __name__ == '__main__':
    main()
