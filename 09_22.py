# Dota programma, kuras uzdevums ir aprēķināt riņķa laukumu
# Testēšana: 3 ----> 28.26
#r = float(input("Ieraksti riņķa rādiusu: "))
#pi = 3.14
#laukums = pi * r**2
#print(f"Riņķa laukums ir {laukums}")

# Dota programma, kuras uzdevums ir izvadīt lietotāja ievadīto vārdu un
#uzvārdu apgrieztā secībā (starp vārdu un uzvārdu ir jābūt atstarpei)
# Testēšana: Anna Bērziņa -----> Bērziņa Anna
#vards = input("Ievadi vārdu: ")
#uzvards = input("Ievadi uzvārdu: ")
#print(f"{uzvards} {vards}")

#Dota programma, kuras uzdevums ir - lietotāja ievadītos skaitļus (kas
#atdalīti ar komatiem), izdrukāt kā sarakstu(list) un kortežu(tuples)
#Testēšana: 1,2,3,4,5,6 -----> Saraksts: ['1','2','3','4','5','6']
# -----> Kortežs: ('1','2','3','4','5','6')
#vertibas = input("Ievadi skaitļus, atdalot tos ar komatiem: ")
#saraksts = vertibas.split(" ")
#kortezs = tuple(saraksts)
#print('Saraksts : ',saraksts)
#print('Kortežs : ',kortezs)

#Dota programma, kuras uzdevums ir izvadīt pirmo un pēdējo krāsu no dotā
#saraksta
#Testēšana: ------> Sarkans, melns
#krasu_saraksts = ["Sarkans","Zaļš","Balts", "Melns"]
#print( "%s %s"%(krasu_saraksts[0], krasu_saraksts[3]))

#Dota programma, kuras uzdevums ir veikt sekojošo matemātisko darbību ar
#ievades skaitli (n): n+nn+nnn
#Testēšana: 5 ----> 615
#a = int(input("Ievadi veselu skaitli: "))
#n1 = int( "%s" % a )
#n2 = int( "%s%s" % (a,a) )
#n3 = int( "%s%s%s" % (a,a,a) )
#print (n1+n2+n3)

#Dota programma, kuras uzdevums ir izvadīt lietotāja ievadītā mēneša kalendāru
#Testēšana: 2015 ---------> May 2015
# 4 ---------> Mo Tu We Th Fr Sa Su
# 1 2 3
# 4 5 6 7 8 9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
#import calendar
#y = int(input("Ievadi gadu : "))
#m = (input("Ievadi mēnesi : "))
    #print(calendar.month(m, y))

#Dota programma, kuras uzdevums ir salīdzināt doto ciparu (n) ar 17, ja n ir
#lielāks par 17, tad nepieciešams atgriezt šo skaitļu starpību dubultā, bet, ja
#n ir mazāks vai vienāds ar 17, nepieciešams atgriezt šo skaitļu starpību
#Testēšana: starpiba(22) -----> 10
# starpiba(14) -----> 3
#def starpiba():
#    n = int(input("ievadi skaitli: "))
#    
#    if n <= 17:
#        return 
#    else:
#        return (n - 17) * 2
#starpiba()

#Dota programma, kuras uzdevums ir atgriezt doto skaitļu (x,y,z) summu, bet,
#ja skaitļi x,y un z ir vienādi, jāatgriež šo skaitļu summa reizināta ar 3
#Testēšana: summa(1,2,3) -----> 6
# summa(3,3,3) -----> 27
#def summa(x, y, z):
#    sum = x + y + z
#    return sum

# Dota programma, kuras uzdevums ir noteikt, vai ievadītais skaitlis ir pāra
#vai nepāra
# Testēšana: 5 -----> Nepāra skaitlis.
# 6 -----> Pāra skaitlis.
#num = int(input("Ievadi veselu skaitli: "))
#if (num % 2) == 0:
#    print("Pāra skaitlis.")
#else:
#    print("Nepāra skaitlis.")

# Dota programma, kuras uzdevums ir saskaitīt 4 dotajā sarakstā
# Testēšana: list_count_4([1, 4, 6, 7, 4]) -----> 2
# list_count_4([1, 4, 6, 4, 7, 4]) ------> 3
def list_count_4(nums):
    count = 1
    for num in nums:
        if num == 4:
            count -= 1
    return count