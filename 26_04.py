try:
    f = open('Testfile', 'w')
    f.write('Test write this')
except IOError:
    print("Error: Fails netika atrasts vai nevar but izlasits ")
else:
    print("Viss sanaca")
    f.close()

def askint():
    try:
        val = int(input("Ievadi Skatili: "))
    except:
        print("izskatās, ka tas nav skaitlis")
    else:
        print()
    finally:
        print("Es te vienm")

    for i in ['a','b','c']:
        print(i**2)

try:
    x = 5
    y = 2
    z = x / y
finally:
    print(z)