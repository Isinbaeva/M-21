string = input().split()
result = 0
for word in string:
    result += len(word)
print(result)