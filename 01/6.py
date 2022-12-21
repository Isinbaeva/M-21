question1 = input("Любите ли вы котиков? ")
question2 = input("Умеете ли вы программировать? ")
if question1 == "да" and question2 == "да":
    print("Вы обладаете незаурядным умом!")
elif question1 == "нет" and question2 == "нет":
    print("Это очень грустно")
elif question1 == "да" and question2 == "нет":
    print("Вам стоит попробовать научиться.")
elif question1 == "нет" and question2 == "да":
    print("Печально.")
else:
    print("Что-то пошло не так! Пройдите тест заново.")

