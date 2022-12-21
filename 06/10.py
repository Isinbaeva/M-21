m = int(input())
dishes = set()
day_dishes = set()
for i in range(m):
    dish = input()
    dishes.add(dish)
result = dishes
n = int(input())
for i in range(n):
    number_dishes = int(input())
    for j in range(number_dishes):
        day_dish = input()
        day_dishes.add(day_dish)
    dishes -= day_dishes
print(dishes)
