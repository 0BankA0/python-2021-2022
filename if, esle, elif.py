'''
Artūrs Murāns

04.10.21
''' 

main = "one"


if main == "one":
    print ("a")
elif main == "Two":
    print("what")

else:
    print('123')

one = input('izvelies + vai - : ')
print(one)

a = float (input('pieraksti pirmo skaiti: '))
b = float (input('pieraksti ontro skaitli: '))

if one == ('+'):
    c = a + b
    print('rezultats ' + str(c))

elif one == ('-'):
    c = a - b
    print('rezultats ' + str(c))

else:
    print('nepareiza funkcija')

input()

