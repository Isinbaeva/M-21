num = int(input())
line = str(input())
for i in line:
    if not i.isalpha():
        print(i, end='')
        continue
    if ord(i) + num > 1071 and ord(i) <= 1071 or ord(i) + num > 1103 and ord(i) <= 1103:
        i = chr(ord(i) - 32)
    i = chr(ord(i) + num)
    print(i, end='')