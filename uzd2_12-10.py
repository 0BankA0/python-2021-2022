def vards(a):
    a = a.lower().split()
    if a[0][0] == a[1][0]:
        return True
    else:
        return False

print(vards('One Two'))
print(vards('Top Two'))