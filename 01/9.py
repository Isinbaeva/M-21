login = input("Введите желаемый логин: ")
mail = input("Введите резервный адрес электронной почты: ")
if "@" not in login and "@" in mail:
    print('OK')
else:
    if "@" not in mail:
        print('Некорректный адрес')
    if "@" in login:
        print('Некорректный логин')
