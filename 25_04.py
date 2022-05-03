a = int(input("ievadi a:"))
b = int(input("ievadi b:"))

for i in range(a, b + 1):
    print(i)


# Lietotājs ievada veselu pozitīvu skaitli. Izdrukā visus skaitļus sākot no ievadītā līdz 0 (neieskaitot)!
sk = int(input("Ievadi skaitli:"))
while sk > 0:
    print(sk)
    sk -= 1

# Lietotājs ievada vairākus skaitļus vienā rindā, atdalot tos ar atstarpi. Izvadi tos skaitļus, kuri ir vienādi un atrodas blakus!
 
saraksts = [int(sk) for sk in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]
 
for i in range(len(saraksts)):
    if saraksts[i] == saraksts[i + 1]:
        print(saraksts[i], saraksts[i + 1])

# Lietotājs ievada vairākus skaitļus, atdalot tos ar atstarpi. Izvadi lielākā ievadītā skaitļa vērtību un indeksu sarakstā!
 
skaitli = [int(skaitli) for skaitli in input("Ievadi skaitlus, atdalot tos ar atstarpi:").split()]