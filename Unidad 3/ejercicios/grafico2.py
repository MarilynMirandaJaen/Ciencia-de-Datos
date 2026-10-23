import pandas as pd
import matplotlib.pyplot as plt

datos = {
    "Mes": [
        "Enero", "Febrero", "Marzo", "Abril",
        "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ],

    "Año 1": [
        800, 850, 900, 950, 1000, 1050,
        1100, 1150, 1200, 1300, 1600, 2000
    ],

    "Año 2": [
        1000, 1050, 1100, 1150, 1200, 1250,
        1300, 1350, 1400, 1550, 2000, 2600
    ]
}

df = pd.DataFrame(datos)

plt.figure(figsize=(12, 6))

plt.plot(
    df["Mes"],
    df["Año 1"],
    marker="o",
    label="Año 1"
)

plt.plot(
    df["Mes"],
    df["Año 2"],
    marker="o",
    label="Año 2"
)

plt.title("Serie temporal: Año 1 vs Año 2")
plt.xlabel("Mes")
plt.ylabel("Valor")

plt.xticks(rotation=45)
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()