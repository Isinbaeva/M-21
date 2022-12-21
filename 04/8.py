import time
n = int(input())
for i in range(n, -1, -1):
    print("Осталось секунд: ", i)
    if i == 0:
        print("Запуск!")
    time.sleep(1)
