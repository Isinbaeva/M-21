max_len = int(input())
n = int(input())
headers = []
for i in range(n):
    header = input()
    if len(header) > max_len:
        headers.append(header[:max_len - 3] + "...")
    else:
        headers.append(header)
print(headers)
