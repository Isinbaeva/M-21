n = int(input())
string = ""
for i in range(1, n + 1):
    if n != 1:
        if n % i == 0:
            string += str(i) + " "
print(string)
if len(string) > 5:
    print("НЕТ")
elif len(string) <= 5 or n == 1:
    print("ПРОСТОЕ")
