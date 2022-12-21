a = int(input("Введите рост Бори: "))
b = int(input("Введите рост Вова: "))
c = int(input("Введите рост Дима: "))
if a > b and a > c:
    print(a)
    if b > c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b > a and b > c:
    print(b)
    if a > c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
elif c > b and c > a:
    print(c)
    if b > a:
        print(b)
        print(a)
    else:
        print(a)
        print(b)