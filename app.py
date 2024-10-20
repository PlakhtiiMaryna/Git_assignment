a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))
c = input("Введіть операцію, яку ви хочети зробити над числами ('+', '-', '/'): ")

def calculator (a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '/':
        if b == 0:
            return 'Неможлива операція: ділення на 0'
        else:
            return a/b
    else:
        print('Введена неправильна оперція')

res = calculator(a, b, c)

print (f'Отриманий результат: {res}')
    
        


