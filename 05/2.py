n = int(input())
for i in range(n):
    word = input()
    if "Кот" in word or "кот" in word:
        print("МЯУ")
        break
else:
    print("НЕТ")