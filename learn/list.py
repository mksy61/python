liste=[5, "Murat", True, 1.23]


for v in liste:
    print(str(type(v))+" ", end="")
    print(v)

liste+=["Deneme"]

print(liste)
print(liste[1])
print(liste[-1])