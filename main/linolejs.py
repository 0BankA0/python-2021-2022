def linoleja_cena(cena, linoleja_platums, teplas_garums, teplas_platums):
    
    '''
    a = teplas_garums * teplas_platums
    iznakums = a * cena
    return iznakums
    '''

    if teplas_platums / linoleja_platums !=0:
        trukst= teplas_platums%linoleja_platums
        if trukst<linoleja_platums:
            papildus= round(linoleja_platums * teplas_garums)
            iznakums = (round(teplas_garums*teplas_platums)+ papildus)*cena
        elif trukst > linoleja_platums:
            lin_gap= round(trukst/linoleja_platums)
            papildus = lin_gap * linoleja_platums * teplas_garums
            iznakums = (round(teplas_garums*teplas_platums)+ papildus)*cena
    else:
        iznakums = (round(teplas_garums*teplas_platums)*cena)
    return iznakums


print(linoleja_cena(6,2,5,5))