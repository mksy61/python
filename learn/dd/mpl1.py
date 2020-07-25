import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline

x = ["1.Türkiye", "2.Kenya", "3.Mısır", "4.Japonya", "5.Rusya"]
y = [84, 40, 70, 140, 120]
z = [45, 18, 28, 10, 55]


plt.title("Tablo")
plt.xlabel("Ülkeler")
plt.ylabel("Nüfus")
plt.subplot(1, 2, 1)
plt.plot(x, y, "r*-")
plt.subplot(1, 2, 2)
plt.plot(x, z, "b--")

# plt.show()

f = plt.figure(figsize=(8, 6))
axes1 = f.add_axes([0.1, 0.1, 0.9, 0.9])
axes2 = f.add_axes([0.2, 0.5, 0.4, 0.4])
axes1.plot(x, y)
axes1.set_title("Tablo..")
axes2.plot(x, z)

fig, axes3 = plt.subplots(1, 2, figsize=(8, 6))
axes3[0].plot(x, y, color="red", linewidth=4)
axes3[1].plot(x, z, color="green", linestyle="-.",
              marker="o", markerfacecolor="black")

fig2 = plt.figure(figsize=(8, 6))
axes4 = fig2.add_axes([0, 0, 1, 1])
axes4.plot(x, y, "r", label="AA")
axes4.plot(x, z, "y", label="BB")
axes4.legend()

plt.scatter(x, y)

plt.show()
fig.savefig("mp1.png")
