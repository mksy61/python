import pandas

ulkeler = pandas.read_csv("pd_ulkeler.csv", squeeze=True)
nufus = pandas.read_csv("pd_ulkenufus.csv", squeeze=True)

print(len(ulkeler))
print(len(nufus))

print(sorted(ulkeler))

x = dict(zip(ulkeler, nufus))

print(ulkeler[4])
print(ulkeler[3:5])

print(nufus.count())


def d(x):
    if x < 40:
        return "Az"
    elif x >= 40 and x < 100:
        return "Orta"
    else:
        return "Yüksek"


print(nufus.apply(d))
print(nufus.apply(lambda z: z*2))
