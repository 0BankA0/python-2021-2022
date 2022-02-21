import json

data=[]

def arr():
    x=0
    while x<1:
        print(x)
        x-=1
        X.append(x)
        data.update(x)
        with open('x.txt','w')as outfile:
            json.dump(data,outfile)


arr()
print(X)