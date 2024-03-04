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
        pass
    elif answer == 'sin':

        a = int(input('напишите первый катет'))

        c = int(input('напишите гипотенузу'))

        sinA = a/c
        print(f'sin = {sinA}')

    elif answer == 'cos':
        pass
    elif answer == 'tg':
        pass
`
menu()

