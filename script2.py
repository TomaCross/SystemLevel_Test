smart = 0
streangh = 0
freedom = 0
choice = int(input('Выберите что прокачать 1-Ум 2-Сила 3-Воля\n'))
if choice == 1:
    smart += 1
    print('Ваш интелект теперь первого уровня!')
elif choice == 2:
    streangh += 1
    print('Ваша сила теперь первого уровня!')
elif choice == 3:
    freedom += 1
    print('Ваша воля теперь первого уровня!')
else:
    print('Вы не выбрали ничего')