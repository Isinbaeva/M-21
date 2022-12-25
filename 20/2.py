def fun():
    return '5' in [input()[-1] for _ in range(int(input()))]


n = int(input())
print(('НЕТ', 'ДА')[sum([fun() for _ in range(n)]) == n])