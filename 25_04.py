a = int(input("ievadi a:"))
b = int(input("ievadi b:"))

for i in range(a, b + 1):
    print(i)


# Lietotājs ievada veselu pozitīvu skaitli. Izdrukā visus skaitļus sākot no ievadītā līdz 0 (neieskaitot)!
sk = int(input("Ievadi skaitli:"))
while sk > 0:
    print(sk)
    sk -= 1