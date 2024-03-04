def menu():
    answer = input('Выберите действие:\n+ - сложение\n- - вычитание')
    if answer == '-':
        print(minus())


def minus():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    return num_1 - num_2
menu()