
file = open("pirmais.txt", "r", encoding="utf-8")
print(file.read())
file.close()


with open("pirmais.txt", "r", encoding="utf-8") as file:
    print(file.read())
    file.close()


file = open("pirmais.txt", "r", encoding="utf-8")
print(file.readline())
file.close()


file = open("pirmais.txt", "r", encoding="utf-8")
print(file.read(15))
file.close()

file = open("Meginajums.txt", "r", encoding="utf-8")
file.write("sveiki")