smart = 0
streangh = 0
freedom = 0
while True:
    choice = (input('Выберите что прокачать 1-Ум 2-Сила 3-Воля\n'))
    try:
        value = int(choice)
    except ValueError:
        print('Пожалуйста введите цифру!')
        continue
    if choice == 1:
        smart += 1
        print('Ваш интелект теперь первого уровня!')
        break
    elif choice == 2:
        streangh += 1
        print('Ваша сила теперь первого уровня!')
        break
    elif choice == 3:
        freedom += 1
        print('Ваша воля теперь первого уровня!')
        break
    else:
        print('Вы не выбрали ничего')