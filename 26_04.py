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
    finally:
        print("Es te vienmer busu")
askint()