strings = list()
for i in range(int(input())):
    strings.append(input())
for i in range(len(strings)):
    for j in range(i + 1, len(strings)):
        if strings[i] > strings[j]:
            strings[i], strings[j] = strings[j], strings[i]
for elem in strings:
    print(elem)
