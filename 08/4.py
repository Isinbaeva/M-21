alphabet = "ABCDEFGHI"
n = int(input("Введите размер доски: "))
temp_number = n
for i in range(n):
    for j in range(n):
        print(alphabet[j] + str(temp_number), end="\t")
        j += 1
    print()
    temp_number -= 1