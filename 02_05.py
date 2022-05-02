import sys

saraksts = ['a', 0, 2]

for i in saraksts:
    try:
        print("skaitlis ir:", i)
        a = 1/int(i)
        break
    except:
        print("Ķluda", sys.exc_info()[1])
print(a)