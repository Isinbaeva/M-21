line = result = cat_line = 0
find = False
while True:
    word = input()
    line += 1
    if "Кот" in word or "кот" in word:
        if not find:
            result = line
            find = True
        cat_line += 1
    if word == "СТОП":
        if not find:
            result = -1
        print(cat_line, result)
        break
