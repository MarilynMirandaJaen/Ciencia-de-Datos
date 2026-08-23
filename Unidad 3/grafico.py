import matplotlib.pyplot as plt

datos = [38, 42, 44, 45, 47, 48, 49, 50, 52, 53, 55, 58, 60, 310]

limite_inferior = 27.5
limite_superior = 71.5

plt.figure(figsize=(10, 5))

# Gráfico de barras
plt.bar(range(1, len(datos) + 1), datos)

# Límites
plt.axhline(limite_inferior, color="green",
            linestyle="--", label="Límite inferior = 27.5")

plt.axhline(limite_superior, color="red",
            linestyle="--", label="Límite superior = 71.5")

plt.title("Detección de valores atípicos")
plt.xlabel("Posición del dato")
plt.ylabel("Valor")

plt.xticks(range(1, len(datos) + 1))
plt.legend()

plt.show()