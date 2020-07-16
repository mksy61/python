liste = list()

print(id(liste))

liste.append("murat")
liste.append(534)
liste.append(True)
liste.append([3, 5])

print(id(liste))
print(liste)

print(liste.count("murat"))

print(len(liste))

print()
for v in liste:
    print(v, " ", type(v))
