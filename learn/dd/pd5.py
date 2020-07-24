import pandas

dn = pandas.read_csv("dünyanüfusu.csv")

print(dn.dropna(how="all"))
print("-"*120)
print(dn.dropna(subset=["Doğum oranı"]))
print("-"*120)
print(dn.fillna("X"))
print(dn.info())
