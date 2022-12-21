def build_pyramid(cubes):
    pyramid = [max(cubes)]
    n = len(cubes)
    for i in range(n):
        left_elem = cubes[0]
        right_elem = cubes[-1]
        if left_elem > right_elem:
            greed_choice = left_elem
            cubes.pop(0)
        else:
            greed_choice = right_elem
            cubes.pop()
        if greed_choice > pyramid[-1]:
            return None
        else:
            pyramid.append(greed_choice)
    return pyramid[1:]


t = int(input())
for i in range(t):
    cubes = [int(x) for x in input().split()]
    pyramid = build_pyramid(cubes)
    if pyramid is None:
        print("НЕТ")
    else:
        print(*pyramid)
