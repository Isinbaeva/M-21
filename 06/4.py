result = set()
eng = int(input())
ger = int(input())
for i in range(eng + ger):
    surname = input()
    if surname in result:
        result.discard(surname)
    else:
        result.add(surname)
if len(result):
    print(len(result))
else:
    print("NO")
