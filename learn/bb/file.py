try:
    file = open("test.txt", "r")
except Exception as identifier:
    print("Dosya açılamadı:", identifier)

hepsi = file.read()

print(type(file))
print(type(hepsi))
print(len(hepsi))


for v in file:
    print(v, end="")

print()
print(hepsi)
