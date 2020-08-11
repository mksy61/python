import pandas

d = {"NAME": ["ali", "veli", "kenan", "hilal", "ayse", "evren"],
     "AGE": [15, 16, 17, 33, 45, 66],
     "MAAS": [100, 150, 240, 350, 110, 220]}

print(d)

df = pandas.DataFrame(d)
# print(df)

# print(df.head(3))
# print(df.columns)
# print("")
# print(df.info())
# print("")
print(df.describe())
# print("")
# print(df["AGE"])
# print(df.AGE)

# df["Yeni"] = ["a", "b", "c", "d", "e", "f"]
print(df)
# print("")
# print(df.loc[0:1, :])
# print("")
df1 = (df["MAAS"] > df["MAAS"].mean()) & (df["AGE"] < df["AGE"].mean())

print(df[df1])

df["DURUM"] = ["Genç" if v < df["AGE"].mean() else "Yaşlı" for v in df["AGE"]]

print(df)
