liste = [1,3,2,4,6,5]

liste.append(-3)

for v in liste:
    print(v,end=" ")

print()
liste.insert(2,55)
for v in liste:
    print(v,end=" ")


print()
liste.sort()
for v in liste:
    print(v,end=" ")

liste.insert(2,55)