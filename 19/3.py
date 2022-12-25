nums = [22,27,36,41,52,54,45,85,90]
print(sum((map(lambda x: x ** 2, (filter(lambda x: x % 9 == 0, nums))))))