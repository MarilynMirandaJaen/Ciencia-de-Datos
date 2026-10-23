import matplotlib.pyplot as plt

canales = ["Tienda física", "Tienda en línea"]
medias = [32500, 38900]
desviacion = [8200, 9100]

plt.figure(figsize=(8, 5))

plt.bar(
    canales,
    medias,
    yerr=desviacion,
    capsize=7,
    color=["teal", "gold"]
)

plt.title("Monto promedio de compra por canal")
plt.xlabel("Canal")
plt.ylabel("Monto (₡)")

# Mostrar el promedio sobre cada barra
for i, valor in enumerate(medias):
    plt.text(i, valor + 1000, f"₡{valor:,}", ha="center")

plt.show()