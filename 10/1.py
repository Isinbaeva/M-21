n = list()
result = False
for i in range(int(input("Введите количество чисел: "))):
    n.append(int(input()))
a = int(input())
for i in range(len(n)):
    for j in range(len(n) - i):
        if (n[i] * n[j]) == a:
            result = True
if result:
    print("Да")
else:
    print("Нет")
