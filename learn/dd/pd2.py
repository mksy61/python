import pandas

yillar = [2015, 2016, 2017, 2018]
gelirler = [500, 600, 700, 800]

x = pandas.Series(data=gelirler, index=yillar)
print(x)

print(x.sum())
print(x.max())
print(x.mean())
print(x.median())
print(x.var())
print(x.std())
print(x.describe())
