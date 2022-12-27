import math
import datetime as dt

birth = list(map(int, input('Введите дату рождения в формате ДД.ММ.ГГГГ: ').split(".")))
birth = dt.date(birth[2], birth[1], birth[0])
now = list(map(int, input('Введите дату расчета биоритма ДД.ММ.ГГГГ: ').split(".")))
now = dt.date(now[2], now[1], now[0])

fiz = round(math.sin((2 * math.pi * (now - birth).days) / 23) * 100, 2)
emo = round(math.sin((2 * math.pi * (now - birth).days) / 28) * 100, 2)
int = round(math.sin((2 * math.pi * (now - birth).days) / 33) * 100, 2)
print(fiz)
print(emo)
print(int)