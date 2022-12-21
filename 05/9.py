n = int(input())
result = ""
cat_find = False
for i in range(n):
    word = input()
    if ("Кот" in word or "кот" in word) and not cat_find:
        result = "МЯУ"
        cat_find = True
    elif ("Пёс" in word or "пёс" in word) and cat_find:
        cat_find = False
    elif not cat_find:
        result = "НЕТ"
print(result)
