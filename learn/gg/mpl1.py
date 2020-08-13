import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("iris.csv")

except Exception as identifier:
    print("Hata:", identifier)
    exit()

# df.drop(["Id"], axis=1, inplace=True)

setosa = df[df["Species"] == "Iris-setosa"]
virginica = df[df["Species"] == "Iris-virginica"]
versicolor = df[df["Species"] == "Iris-versicolor"]
print("\n")

# setosa.plot()
# virginica.plot()
# versicolor.plot()

plt.plot(setosa.Id, setosa["PetalWidthCm"], color="red", label="setosa")
plt.plot(virginica.Id, virginica["PetalWidthCm"],
         color="green", label="virginica")
plt.plot(versicolor.Id, versicolor["PetalWidthCm"],
         color="blue", label="versicolor")
plt.xlabel("Id")
plt.ylabel("PetalWidthCm")
plt.legend()
plt.show()
