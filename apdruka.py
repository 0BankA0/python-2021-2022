


def pasuti_teikreklu(skaits, apdruka, piegade):
    cena = {'TEKSTS': 5, 'ZIME':7, 'FOTO':20} 
    
    apreikins = cena[apdruka] * skaits

    while piegade:
        if apreikins < 50:
            return apreikins + 15
        elif apreikins >=50:
            return apreikins
        elif apreikins > 100:
            atlaide = apreikins * 0.05
            return apreikins - atlaide
    else:
        if apreikins > 100:
            atlaide= apreikins * 0.05
            return apreikins - atlaide
        else:
            return apreikins


print(pasuti_teikreklu(5, 'TEKSTS', True))