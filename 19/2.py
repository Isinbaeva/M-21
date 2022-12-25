def simple_map(transformation, values):
    result = [transformation(elem) for elem in values]
    return result


values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))

