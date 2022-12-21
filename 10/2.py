surnames = list()
for i in range(int(input("Введите количество школьников: "))):
    surnames.append(input())
for elem in surnames:
    print(elem)
print()
for elem in surnames:
    if int(elem[-1]) > 3:
        print(elem)
