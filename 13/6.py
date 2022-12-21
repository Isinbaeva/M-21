n1 = input().split()
lst1 = []
lst2 = []
for i in range(len(n1)):
    if n1[i] not in lst1:
        lst2.append("1")
        lst1.append(n1[i])
    else:
        lst2.append(str(lst1.count(n1[i]) + 1))
        lst1.append(n1[i])
print(" ".join(lst2))