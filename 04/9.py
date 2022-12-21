n = int(input())
c = 1
row = ((n * 2 - 1) // 2) + 1
for i in range(1, n + 1):
    print(" " * row, "*" * c)
    c += 2
    row -= 1