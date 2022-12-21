n1 = set()
n2 = set()
while True:
    n = input()
    if n == "":
        break
    else:
        n1.add(int(n))
while True:
    n = input()
    if n == "":
        break
    else:
        n2.add(int(n))
if n1 & n2:
    print(n1 & n2)
else:
    print("EMPTY")
