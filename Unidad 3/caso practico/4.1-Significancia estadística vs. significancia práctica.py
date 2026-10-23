import matplotlib.pyplot as plt

nombres = ["Valor p", "Alfa (α)"]
valores = [0.001, 0.05]

plt.figure(figsize=(6, 5))

plt.bar(nombres, valores, color=["purple", "orange"])

plt.title("Significancia estadística")
plt.ylabel("Valor")

# Mostrar valores
for i, valor in enumerate(valores):
    plt.text(i, valor + 0.002, str(valor), ha="center")

plt.ylim(0, 0.06)

plt.show()