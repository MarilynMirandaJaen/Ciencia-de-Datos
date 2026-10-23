import matplotlib.pyplot as plt

datos = [18, 22, 25, 27, 29, 30, 31, 33, 35, 36, 38, 40, 42, 45, 98]

pedidos = range(1, len(datos) + 1)

plt.figure(figsize=(10, 5))

plt.scatter(pedidos, datos)

# Línea del límite superior
plt.axhline(y=59.5, linestyle="--", label="Límite superior = 59.5")

plt.title("Monto de los pedidos de LMB")
plt.xlabel("Número de pedido")
plt.ylabel("Monto (miles de colones)")
plt.xticks(pedidos)

plt.legend()
plt.grid(True)

plt.show()