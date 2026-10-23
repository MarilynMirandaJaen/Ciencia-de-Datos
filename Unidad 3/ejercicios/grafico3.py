import matplotlib.pyplot as plt

trimestres = ["Q1", "Q2", "Q3", "Q4"]

anio1 = [2.1, 2.4, 2.6, 3.2]
anio2 = [2.3, 2.6, 2.8, 3.5]
anio3 = [2.6, 2.9, 3.1, 3.9]

plt.figure(figsize=(10, 6))

# Color de fondo
plt.gca().set_facecolor("lightblue")

# Líneas con diferentes colores
plt.plot(trimestres, anio1,
         marker="o",
         color="purple",
         linewidth=2,
         label="Año 1")

plt.plot(trimestres, anio2,
         marker="o",
         color="orange",
         linewidth=2,
         label="Año 2")

plt.plot(trimestres, anio3,
         marker="o",
         color="green",
         linewidth=2,
         label="Año 3")

plt.title("Valores por trimestre Marilyn Miranda Jaen")
plt.xlabel("Trimestre")
plt.ylabel("Valor")

plt.legend()
plt.grid(alpha=0.3)

plt.show()