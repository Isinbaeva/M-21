a = input()
k = len(a) + 1
temp = "о" * k
while a.find(temp) == -1:
    k -= 1
    temp = "о" * k
print(k)