def menu():

    answer = input('Выберите действие:\n+ - сложение\n- - вычитание\n* - умножение\n'
                   '/ - деление\n** - возведение в степень\n% - остаток от деления\n корень - корень\n'
                   'sin - синус\ncos - косинус\ntg - тангенс:')
    if answer == '+':
        pass
    elif answer == '-':
        pass
    elif answer == '*':
        pass
    elif answer == '/':
        delenie()
    elif answer == '**':
        pass
    elif answer == '%':
        pass
    elif answer == 'корень':
        pass
    elif answer == 'sin':
        pass
    elif answer == 'cos':
        pass
    elif answer == 'tg':
        pass

def delenie():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    result = num_1/num_2
    print(f'Ответ: {result}')


menu()

