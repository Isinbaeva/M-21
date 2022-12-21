string = input().split()
res = ""
for word in string:
    res += "-".join(list(word)) + " "
print(res.upper())
