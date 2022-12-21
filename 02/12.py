text = input("Введите сообщение: ")
ruble = len(text) * 40 // 100
cop = len(text) * 40 % 100
print(str(ruble) + " р. " + str(cop) + " коп.")
