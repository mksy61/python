import pandas

ulkeler = pandas.read_csv("pd_4.csv")

print(ulkeler.shape)
print(ulkeler.index)
print(ulkeler.axes)
# print(ulkeler.info())
ulkeler["Sıralama"] = "***"
# print(ulkeler["Ülkeler"])

print(ulkeler)

print(ulkeler["Kıta"].value)