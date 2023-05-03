from src.lab1 import *
from src.lab2 import *
from src.lab3 import *
from src.lab4 import *
from src.lab5 import *
from src.lab6 import *


def main():
    lab_input = input("Какую Лабораторную работу хотите запустить?\n")
    match lab_input:
        case "1":
            lab1()
        case "2":
            lab2()
        case "3":
            lab3()
        case "4":
            lab4()
        case "5":
            lab5()
        case "6":
            lab6()
        case _:
            print("Нет данной работы")


if __name__ == '__main__':
    main()
