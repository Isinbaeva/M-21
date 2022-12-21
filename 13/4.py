d = dict()
for _ in range(int(input())):
    x, y = map(int, input().split())
    key = x // 10, y // 10
    d[key] = d.get(key, 0) + 1
print(max(d.values()))