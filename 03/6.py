password = input("Введите пароль: ")
password_2 = input("Введите пароль еще раз: ")
while len(password) < 8:
    print("Короткий!")
    password = input("Введите пароль: ")
    password_2 = input("Введите пароль еще раз: ")
while "123" in password:
    print("Простой!")
    password = input("Введите пароль: ")
    password_2 = input("Введите пароль еще раз: ")
while password_2 != password:
    print("Различаются!")
    password = input("Введите пароль: ")
    password_2 = input("Введите пароль еще раз: ")
print("ОК")
