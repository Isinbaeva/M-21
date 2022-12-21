n = int(input())
strings = []
for i in range(n):
    string = input()
    if string[:2] == "%%":
        strings.append(string[2:])
    elif string[:4] == "####":
        continue
    else:
        strings.append(string)
for elem in strings:
    print(elem)