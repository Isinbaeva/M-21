all_set = set()
result = set()
df_set = set()
m = int(input())
n = int(input())
k = int(input())
for i in range(m + n + k):
    word = input()
    if word in result:
        result.discard(word)
    if word in all_set:
        result.add(word)
        all_set.discard(word)
    else:
        all_set.add(word)
print(len(result))