stop = False
while stop == False:
    try:
        laiks = int(input("ievadi laiku(0-23): "))
        if laiks >= 0 and laiks <= 23:
            stop = True
        else:
            print("pameigini velreiz")
    except:
        ("ir kluda!")
if laiks >= 0 and laiks <= 4:
    print("labunakti!")
elif laiks >= 5 and laiks <=11:
    print("labrit!")
elif laiks >= 12 and laiks <= 17:
    print("labdien!")
elif laiks >= 18 and laiks <=23:
    print("labvakar!")
else:
    print("ir kluda!")