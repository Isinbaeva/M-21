n = int(input())
for i in range(n):
    word = input()
    if "кот" in word.lower():
        print(i + 1, word.lower().find("кот") + 1)