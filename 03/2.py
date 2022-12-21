password = input("Введите пароль: ")
password_2 = input("Введите пароль еще раз: ")
if len(password) < 8:
    print("Короткий!")
elif password_2 != password:
    print("Различаются.")
else:
    print("ОК")