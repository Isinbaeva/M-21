eng = set()
ger = set()
result = set()
n = int(input())
m = int(input())
for i in range(n):
    eng.add(input())
for i in range(m):
    ger.add(input())
result = eng ^ ger
if len(result):
    print(len(result))
else:
    print("NO")
