import matplotlib.pyplot as plt

nombres = ["Valor p", "Alfa (α)"]
valores = [0.007, 0.05]

plt.plot(nombres, valores, marker="o")

plt.title("Comparación de p y α")
plt.ylabel("Valor")
plt.ylim(0, 0.06)
plt.grid()

plt.show()