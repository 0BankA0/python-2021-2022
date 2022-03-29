def atgriezt_skaitli(a,b):
    if b % 2 == 0:
        print(min(a,b))
        if a % 2 ==0:
            print(min(a,b))
    else:
        print(max(a,b))

atgriezt_skaitli(2,4)