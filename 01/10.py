print("Добро пожаловать на квест.")
print("Вы находитесь в темном коридоре.")
print("Вы можете пойти направо, налево ил прямо.Куда вы пойдете? ")
step_1 = input()
if step_1 == "налево":
    print("Под вами проваливается пол.Игра окончена.")
elif step_1 == "прямо":
    print('На вас свалился камень.Игра окончена')
if step_1 == "направо":
    print("Вы вошли в комнату.")
    print("В комнате есть 2 двери:желтая,синяя и белая.")
    print("На стене висит картина,на которой нарисован синий кот.")
    print("Какую дверь вы выберите?")
    step_2 = input()
    if step_2 == "желтую":
        print("Вы проходите в темную комнату.Перед вами огромный заяц,который съедает вас.Игра окончена")
    elif step_1 == "белую":
        print('Комнату затопило.Игра окончена')
    if step_2 == "синию":
        print("Поздравляю,вы прошли дальше.")
        print("Вы находитесь в лифте.")
        print("Перед вами 3 кнопки:1,2 и 3.Какую кнопку вы нажмете?")
        step_3 = input()
        if step_3 == "1":
            print("Лифт внезапно падает.Игра окончена.")
        elif step_1 == '2':
            print('Лифт открывается,вас застреливают.Игра окончена')
        if step_3 == "3":
            print("Вы подниматесь.Лифт открывается и вы выбираетесь наружу.Поздавляю вы прошли игру.")
