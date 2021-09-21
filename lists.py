#mainigais saraksts, jeb list

#[]

list=['word', 12 , 222]
print(list)

#elementu skaits mainigaja

print("elementu skaits", len(list))

#indeks metode

print(list[1])
print(list[0:])



#elementu mainja
list[0] = "word2"
print(list)


#elementu pievienišana
print(list + ['hey'])
list = list + ['what']
print(list)


list.append('word3')
print(list)

#pop-elementa noņemšana
list.pop(2)
print(list)