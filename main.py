t = input("выберите действие (+, -, *, /, **, sqrt, %, D)")
y = float(input("Введите первое число: "))
z = float(input("Введите второе число: "))
if t != "D":
    if t == "+":
        c = y + z
        print("Результат: " + str(c))
    elif t == "-":
        c = y - z
        print("Результат: " + str(c))
    elif t == "*":
        c = y * z
        print("Результат: " + str(c))
    elif t == "/":
        c = y / z
        print("Результат: " + str(c))
    elif t == "**":
        c = y ** z
        print("Результат: " + str(c))
    elif t == "sqrt":
        c = y ** (1/z)
        print("Результат: " + str(c))
    elif t == "%":
        c = y % z
        print("Результат: " + str(c))
    else:
        print("Команда не распознана")
else:
    c = float(input("Введите третье число: "))
    f = (y ** 2) - (4 * z * c)
    n = (-y - (f ** (1/2))) / (2 * c)
    k = (-y + (f ** (1 / 2))) / (2 * c)
    print("Результат: " + str(n) + str(k))



