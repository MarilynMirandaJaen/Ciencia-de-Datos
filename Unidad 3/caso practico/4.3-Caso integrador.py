import matplotlib.pyplot as plt

equipos = ["Equipo A", "Equipo B"]
tiempos = [4.2, 3.1]

plt.figure(figsize=(7, 5))

plt.bar(equipos, tiempos, color=["green", "purple"])

plt.title("Tiempo promedio de resolución de quejas")
plt.xlabel("Equipo de soporte")
plt.ylabel("Tiempo promedio (días)")

for i, valor in enumerate(tiempos):
    plt.text(i, valor + 0.1, f"{valor} días", ha="center")

plt.ylim(0, 5)

plt.show()