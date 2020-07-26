import pandas as pd

x = pd.Series([1, 3, 5, 7, 9])
# print(pd.__version__)

# print()
# print(x)

mp = {"Bir": 1, "İki": 2, "Üç": 3, "Dört": 4}

y = pd.Series(mp)

print(y.values)
print(y.index)
print(y[2])
print(y["İki"])
print()
print(y)
