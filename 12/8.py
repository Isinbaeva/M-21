string = input().lower()
max_count = 0
char = ""
for i in range(len(string)):
    count = string.count(string[i])
    if count > max_count:
        max_count = count
        char = string[i]
print(char)