n = int(input())
result = ""
cat_find = False
for i in range(n):
    word = input()
    if ("Кот" in word or "кот" in word) and not cat_find:
        result = "МЯУ"
        cat_find = True
    elif not cat_find:
        result = "НЕТ"
print(result)
