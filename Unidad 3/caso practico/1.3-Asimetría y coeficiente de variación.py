import matplotlib.pyplot as plt

productos = ["Producto A", "Producto B"]
cv = [15, 30]

plt.figure(figsize=(8, 5))

plt.bar(productos, cv, color=["steelblue", "orange"])

plt.title("Coeficiente de variación de las ventas")
plt.xlabel("Producto")
plt.ylabel("Coeficiente de variación (%)")

# Mostrar porcentaje sobre cada barra
for i, valor in enumerate(cv):
    plt.text(i, valor + 0.5, f"{valor}%", ha="center")

plt.ylim(0, 35)

plt.show()