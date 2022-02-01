file = open("meginajums.txt","r",encoding="utf-8")

file.write("Skola viss labaka")

saturs=["Sodien laba diena"]

file.writelines(saturs)

file.close()

with open("meginajums.txt","r",encoding="utf-8") as file:

    print(file.read())
    print(file.readline())

    file.seek(0)

    print(file.readline())

with open("meginajums.txt","a",encoding="utf-8") as file:
    file.write("Skola ir slikti")

with open("meginajums.txt","w",encoding="utf-8") as file:
    file.write("Labdien")