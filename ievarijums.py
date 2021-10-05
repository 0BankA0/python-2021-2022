cukurskg = float( input('cik kilogramu cukura:'))
cukurscena = float( input('cik maksa kilograms cukura:'))
kaneliskg = float( input('cik kilogramu kaneļa:'))
kaneliscena = float( input('cik maksa kilograms kaneļa:'))
abolikg = float( input('cik kilogramu abolu:'))
abolicena = float( input('cik maksa kilograms abolu:'))
udenikg = float( input('cik litru udens:'))
udenicena = float( input('cik maksa litrs udens:'))


c = cukurskg * cukurscena
f = kaneliskg * kaneliscena
g = abolikg * abolicena
h = udenikg * udenicena

iznakums = c + f + g + h

print(str(iznakums))