def task_one():
    a, b = list(map(float, input("Введите два числа через пробел: ").split()))
    try:
        print(a / b)
    except:
        print("Первое число не делится на второе")


def task_two(m: int, n: int) -> dict:
    result = {"m": m, "n": n}

    if m != n:
        if m > n:
            result["n"] = m
            return result
        result["m"] = n
        return result

    result["m"] = 0
    result["n"] = 0
    return result


def lab3():
    task_one()
    print(task_two(int(input("Введите число m: ")), int(input("Введите число n: "))))
