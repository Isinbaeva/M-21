Pi = 3.14159


def circle_length(radius):
    length = radius * 2 * Pi
    return length


def circle_area(radius):
    area = Pi * (radius ** 2)
    return area


def main():
    radius = float(input('Введите радиус окружности: '))
    print('Длина =', circle_length(radius), 'Площадь =', circle_area(radius))


main()