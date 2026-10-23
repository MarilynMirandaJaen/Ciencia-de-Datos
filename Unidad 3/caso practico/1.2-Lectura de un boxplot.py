import matplotlib.pyplot as plt

nombres = ["Mínimo", "Q1", "Mediana", "Q3", "Máximo", "Atípico"]
valores = [1, 2, 3, 4, 6, 14]

plt.figure(figsize=(9, 5))

plt.bar(nombres, valores, color="green")

plt.title("Resumen del tiempo de entrega")
plt.ylabel("Días")
plt.xlabel("Medidas estadísticas")

# Mostrar valores encima de las barras
for i, valor in enumerate(valores):
    plt.text(i, valor + 0.2, str(valor), ha="center")

plt.show()