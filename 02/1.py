city1, city2 = input("Введите город в июле: "), input("Введите город в августе: ")
if ((city1 == 'Тула') and (city2 != 'Пенза') and (city2 != 'Тула')) or\
        ((city1 != 'Тула') and (city1 != 'Пенза') and (city2 == 'Пенза')):
    print('ДА')
else:
    print('НЕТ')
