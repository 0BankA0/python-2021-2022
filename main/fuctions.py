'''
Artūrs Murāns

04,10,21
'''
def what():
  print("es te")

what()

def what2(location):
  print('kur tu esi',"\n",location)

what2("te")

def what3(a,b):
    print('kas', a, b)

what3("te", "tur")

def what4(abc, acd):
    return abc + acd

an = "123"
af = "absdaw"

print(what4(an, af))


s = int(input('ievadi skaitli: '))

def counting(one,two,three):
    for one in range(one,two,three):
        print(one)

if s == 1:
    counting(one=s,two=s+10,three=1)
else:
    counting(one=s,two=s+11,three=1)
