masivs = ["A", "B", "c", "D", "E", "F"]
print(masivs)
print(type(masivs))
print(masivs[3])

for x in masivs:
    print(x)

vardnica = {'vards':'arturs', 'izglitiba': 'lol', 'vecums': '22'}

print(vardnica)
print(type(vardnica))
print(vardnica['vards'])

personas = [
   
   {'vards':'arturs', 'izglitiba': 'lol', 'vecums': '22'} ,
   {'vards':'qwerwqw', 'izglitiba': 'lol', 'vecums': '82'}
]

print(type(personas))

for persona in personas:
    print(persona['vards']) 
