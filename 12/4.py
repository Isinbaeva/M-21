list1 = input().split()
list2 = input().split()
print(sum([int(list1[i]) ** 2 for i in range(int(list2[0]), int(list2[1]) + 1)]))