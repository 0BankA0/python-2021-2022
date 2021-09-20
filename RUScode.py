from colorama import init
from colorama import Fore, Back, Style

init()

print ( Fore.BLACK )
print ( Back.GREEN )

what = input('Что будем делать (+ , - , * , /): ')

a = float( input('Ведите первое число:'))
b = float( input('Ведите второе число:'))

if what == ('+'):
    c = a + b
    print('результат:' + str(c))

elif what == ('-'):
    c = a + b
    print('результат:' + str(c))

if what == ('*'):
    c = a * b
    print('результат:' + str(c))
elif what == ('/'):
    c = a / b
    print('результат:' + str(c))

input('Нажми любуию клавишу чтобы закрыть програму!')