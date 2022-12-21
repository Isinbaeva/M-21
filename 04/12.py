n = int(input())
sum = 0
for i in range(n):
    if i % 2:
        sum += int(input())
    else:
        sum -= int(input())
print(abs(sum))
