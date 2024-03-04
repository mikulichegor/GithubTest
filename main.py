def menu():

    answer = input('Выберите действие:\n+ - сложение\n- - вычитание\n* - умножение\n'
                   '/ - деление\n** - возведение в степень\n% - остаток от деления\n корень - корень\n'
                   'sin - синус\ncos - косинус\ntg - тангенс')
    if answer == '+':
        pass
    elif answer == '-':
        pass
    elif answer == '*':
        pass
    elif answer == '/':
        pass
    elif answer == '**':
        pass
    elif answer == '%':
        pass
    elif answer == 'корень':
        num=int(input("Ввидите число: "))
        sqrt=num ** 0.5
        print(f'корень из {num} равен {sqrt}')
    elif answer == 'sin':
        pass
    elif answer == 'cos':
        a = int(input('Сторона A:'))
        b = int(input('Сторона B:'))
        c = int(input('Сторона C:'))
        print(float((a**2 + b**2 - c**2)/(2 * a * b)))
    elif answer == 'tg':
        pass

menu()

