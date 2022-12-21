n = int(input())
city = set()
for i in range(n):
    city.add(input())
if input() not in city:
    print("OK")
else:
    print("TRY ANOTHER")
