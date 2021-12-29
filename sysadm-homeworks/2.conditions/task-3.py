#Приложение определения знака зодиака

user_date = int(input("Введите число дня рождения : "))
user_month = input("Введите месяц рождения : ")

if ((user_date > 20 and user_date < 32 and user_month == 'март') or (user_date > 0 and user_date < 21 and user_month == 'апрель')):
    print("Ваш знак зодиака Овен")
elif (user_date > 20 and user_date < 30 and user_month == "апрель") or (user_date > 0 and user_date < 22 and user_month == "май"):
    print("Ваш знак зодиака Телец")
elif (user_date > 21 and user_date < 31 and user_month == "май") or (user_date > 0 and user_date < 22 and user_month == "июнь"):
    print("Ваш знак зодиака Близнецы")
elif (user_date > 21 and user_date < 30 and user_month == "июнь") or (user_date > 0 and user_date < 23 and user_month == "июль"):
    print("Ваш знак зодиака Рак")
elif (user_date > 22 and user_date < 31 and user_month == "июль") or (user_date > 0 and user_date < 22 and user_month == "август"):
    print("Ваш знак зодиака Лев")
elif (user_date > 21 and user_date < 31 and user_month == "август") or (user_date > 0 and user_date < 24 and user_month == "сентябрь"):
    print("Ваш знак зодиака Дева")
elif (user_date > 23 and user_date < 31 and user_month == "август") or (user_date > 0 and user_date < 24 and user_month == "октябрь"):
    print("Ваш знак зодиака Дева")
# и тд.