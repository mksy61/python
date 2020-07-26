import pandas as pd

a = {"Bir": 1, "İki": 2, "Üç": 3, "Dört": 4, "Beş": 5}
b = {"Bir": 10, "İki": 20, "Üç": 30, "Dört": 40, "Altı": 60}

x = pd.Series(a)
y = pd.Series(b)

z = pd.DataFrame({"A": x, "B": y})
v = pd.DataFrame([a, b])
z["V"] = z["A"]/2
u = z[z["B"] > 10]
# print(z.T)
# print(z)
# print(type(x))
# print(type(u))
print()
print(v)

v.fillna("*", inplace=True)
print()
print(v)

# print(x[0:3])
print("-"*4)
print(v.iloc[0:1])
