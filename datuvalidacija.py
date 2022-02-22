while True:
        tell = input("Ievadi savu telefona numuru: ")
        if len(tell) <8:
            continue
        else:
             break



while True:
    vecums = input("Ievadi savu vecumu: ")
    if vecums.isdigit() == True:
        break
    else:
        continue



while True:
    vards = input("Ievadi savu vardu: ")
    if vards.strip() == "":
        print("ievadi vardu atkartoti: ")
        continue
    else:
        break

