import matplotlib.pyplot as plt

x = list(range(1000))
y = [n ** 2 for n in x]

plt.scatter(x, y, s=10, c=y, cmap=plt.cm.Blues)

plt.show()
