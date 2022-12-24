def from_string_to_list(string, container):
    for number in map(int, string.split()):
        container.append(value)
    return container


value = [77, 'abc']
from_string_to_list("", value)
print(*value)