import matplotlib.pyplot as plt

casos = ["A", "B", "C"]
valor_p = [0.032, 0.184, 0.049]
alfa = [0.05, 0.05, 0.01]

plt.plot(casos, valor_p, marker="o", label="Valor p")
plt.plot(casos, alfa, marker="o", label="α (alfa)")

plt.title("Valor p vs. nivel de significancia")
plt.xlabel("Caso")
plt.ylabel("Valor")

plt.legend()
plt.grid()

plt.show()