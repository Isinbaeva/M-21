def find_farthest_orbit(list_of_orbits):
    for i in list_of_orbits:
        if i[0] == i[1]:
            list_of_orbits.remove(i)
        else:
            continue
    length_of_orbits = list(map(lambda a: a[0] * a[1] * 3.14, list_of_orbits))
    return list_of_orbits[length_of_orbits.index(max(length_of_orbits))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
