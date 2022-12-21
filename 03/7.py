attempts = 10
border_1 = 0
border_2 = 1000
border_3 = 0
position = int(border_2 / 2)
while True:
    if attempts <= 0:
        print("У вас не осталось попыток(")
        break
    else:
        print("Осталось попыток : ", attempts)
        print(position)
        sign = input("Введите знак: ")
        if sign == "<":
            border_2 = position
            border_3 = position
        elif sign == ">":
            border_1 = position
            if border_3 != 0:
                border_2 = border_3
        elif sign == "=":
            print("Ваше число: ", position)
            break
        position = (border_1 + border_2) // 2
        attempts -= 1
