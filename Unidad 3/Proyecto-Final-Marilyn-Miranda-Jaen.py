import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
plt.style.use("dark_background")

from tkinter import (
    ttk,
    filedialog,
    messagebox,
    simpledialog
)
# Muestra números con 2 decimales y evitar notación científica
pd.options.display.float_format = '{:.2f}'.format

# variables globales

df = None
registros_nuevos = []


# Función para mostrar texto

def mostrar_texto(texto):

    salida.delete("1.0", tk.END)
    salida.insert(tk.END, texto)

# Función que verifica CSV

def verificar_df():

    if df is None:

        messagebox.showwarning(
            "Advertencia",
            "Primero debe cargar un archivo CSV."
        )

        return False

    return True

# 1. Carga archivo CSV

def cargar_csv():

    global df

    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[
            ("Archivo CSV", "*.csv")
        ]
    )

    if archivo:

        try:

            df = pd.read_csv(archivo)

            texto = (
                "Datos\n\n"
                f"Filas: {df.shape[0]}\n"
                f"Columnas: {df.shape[1]}\n\n"
                "Primeras filas:\n\n"
                f"{df.head().to_string()}"
            )

            mostrar_texto(texto)

            messagebox.showinfo(
                "Correcto",
                "Archivo CSV cargado correctamente."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

# 2. Información de dataset

def informacion_dataset():

    if not verificar_df():
        return

    texto = (
        "******Información de dataset ******\n\n"
        f"Cantidad de filas: {df.shape[0]}\n"
        f"Cantidad de columnas: {df.shape[1]}\n\n"
        "COLUMNAS:\n"
    )

    for columna in df.columns:

        texto += f"- {columna}\n"

    texto += "\nTipos de datos:\n"

    texto += df.dtypes.to_string()

    mostrar_texto(texto)

# 3. Primeras y últimas filas

def primeras_ultimas():

    if not verificar_df():
        return

    texto = (
        "------ Primeras 5 filas------\n\n"
        + df.head().to_string()
        + "\n\n"
        + "----- Últimas 5 filas -----\n\n"
        + df.tail().to_string()
    )

    mostrar_texto(texto)

# 4. Submenú tipo de datos

def ventana_tipos():

    global df

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title(
        "Análisis de Tipos de Datos"
    )

    ventana.geometry(
        "450x500"
    )

    tk.Label(
        ventana,
        text="Tipos de datos",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    # Muestra Tipos

    def mostrar_tipos():

        mostrar_texto(
            "****** Tipos de datos ******\n\n"
            + df.dtypes.to_string()
        )

    # Columnas numericas

    def columnas_numericas():

        columnas = df.select_dtypes(
            include="number"
        ).columns.tolist()

        mostrar_texto(
            "------ Columnas Númericas ------\n\n"
            + "\n".join(columnas)
        )

    # Columnas de texto

    def columnas_texto():

        columnas = df.select_dtypes(
            include=["object", "string"]
        ).columns.tolist()

        mostrar_texto(
            "------Columnas de texto------\n\n"
            + "\n".join(columnas)
        )

    # Cuenta tipos de datos

    def contar_tipos():

        mostrar_texto(
            "------Cantidad por tipo de dato------\n\n"
            + df.dtypes.value_counts().to_string()
        )

    # Convierte a número

    def convertir_numero():

        global df

        columna = simpledialog.askstring(
            "Convertir",
            "Digite la columna:"
        )

        if columna in df.columns:

            df[columna] = pd.to_numeric(
                df[columna],
                errors="coerce"
            )

            messagebox.showinfo(
                "Correcto",
                "Columna convertida a número."
            )

        else:

            messagebox.showerror(
                "Error",
                "La columna no existe."
            )

    # Convierte a texto
    def convertir_texto():

        global df

        columna = simpledialog.askstring(
            "Convertir",
            "Digite la columna:"
        )

        if columna in df.columns:

            df[columna] = df[columna].astype(
                "string"
            )

            messagebox.showinfo(
                "Correcto",
                "Columna convertida a texto."
            )

        else:

            messagebox.showerror(
                "Error",
                "La columna no existe."
            )


    opciones = [

        ("Mostrar tipos de datos", mostrar_tipos),

        ("Columnas numéricas", columnas_numericas),

        ("Columnas de texto", columnas_texto),

        ("Contar tipos de datos", contar_tipos),

        ("Convertir columna a número", convertir_numero),

        ("Convertir columna a texto", convertir_texto)

    ]

    for texto, funcion in opciones:

        tk.Button(
            ventana,
            text=texto,
            width=25,
            command=funcion
        ).pack(pady=4)


    tk.Button(
        ventana,
        text="Cerrar",
        width=25,
        command=ventana.destroy
    ).pack(pady=10)

# 5. Submenu de valores nulos

def ventana_nulos():

    global df

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title(
        "Análisis de Valores Nulos"
    )

    ventana.geometry(
        "300x300"
    )

    tk.Label(
        ventana,
        text="Valores Nulos",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    # Muestra nulos

    def mostrar_nulos():

        nulos = df.isnull().sum()

        mostrar_texto(
            "------ Valores Nulos ------\n\n"
            + nulos.to_string()
            + "\n\nTotal: "
            + str(nulos.sum())
        )

    # Muestra filas con nulos

    def filas_nulas():

        resultado = df[
            df.isnull().any(axis=1)
        ]

        if resultado.empty:

            mostrar_texto(
                "No existen filas con valores nulos."
            )

        else:

            mostrar_texto(
                resultado.to_string()
            )

    # Elimina nulos

    def eliminar_nulos():

        global df

        antes = len(df)

        df = df.dropna()

        despues = len(df)

        messagebox.showinfo(
            "Resultado",
            f"Filas eliminadas: {antes - despues}"
        )

    # Agrega desconocido a celdas vacias

    def rellenar_desconocido():

        global df

        columna = simpledialog.askstring(
            "Desconocido",
            "Digite la columna:"
        )

        if columna in df.columns:

            df[columna] = df[columna].fillna(
                "Desconocido"
            )

            messagebox.showinfo(
                "Correcto",
                "Valores reemplazados."
            )

        else:

            messagebox.showerror(
                "Error",
                "La columna no existe."
            )


    opciones = [

        ("Mostrar nulos", mostrar_nulos),

        ("Filas con nulos", filas_nulas),

        ("Eliminar filas con nulos", eliminar_nulos),

        ("Rellenar con valor desconocido", rellenar_desconocido)
    ]

    for texto, funcion in opciones:

        tk.Button(
            ventana,
            text=texto,
            width=25,
            command=funcion
        ).pack(pady=4)

    tk.Button(
        ventana,
        text="Cerrar",
        width=25,
        command=ventana.destroy
    ).pack(pady=10)

# 6. Submenu duplicados

def ventana_duplicados():

    global df

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title(
        "Datos Duplicados"
    )

    ventana.geometry(
        "350x350"
    )

    tk.Label(
        ventana,
        text="Datos Duplicados",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    def contar():

        cantidad = df.duplicated().sum()

        mostrar_texto(
            "Cantidad de registros duplicados: "
            + str(cantidad)
        )

    def mostrar():

        duplicados = df[
            df.duplicated(keep=False)
        ]

        if duplicados.empty:

            mostrar_texto(
                "No existen registros duplicados."
            )

        else:

            mostrar_texto(
                duplicados.to_string()
            )

    def eliminar():

        global df

        antes = len(df)

        df = df.drop_duplicates()

        eliminados = antes - len(df)

        messagebox.showinfo(
            "Resultado",
            f"Registros eliminados: {eliminados}"
        )


    def por_columna():

        columna = simpledialog.askstring(
            "Duplicados",
            "Digite la columna:"
        )

        if columna in df.columns:

            resultado = df[
                df.duplicated(
                    subset=[columna],
                    keep=False
                )
            ]

            mostrar_texto(
                resultado.to_string()
            )

        else:

            messagebox.showerror(
                "Error",
                "La columna no existe."
            )

    tk.Button(
        ventana,
        text="Contar duplicados",
        width=35,
        command=contar
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Mostrar duplicados",
        width=35,
        command=mostrar
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Eliminar duplicados",
        width=35,
        command=eliminar
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Duplicados por columna",
        width=35,
        command=por_columna
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Cerrar",
        width=35,
        command=ventana.destroy
    ).pack(pady=15)

# 7. Submenu estadisticas

def ventana_estadisticas():

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title(
        "Estadísticas Descriptivas"
    )

    ventana.geometry(
        "460x600"
    )

    tk.Label(
        ventana,
        text="Estadisticas Descriptivas",
        font=("Arial", 15, "bold")
    ).pack(pady=15)


    def pedir_columna():

        columna = simpledialog.askstring(
            "Columna",
            "Digite una columna numérica:"
        )

        numericas = df.select_dtypes(
            include="number"
        ).columns.tolist()

        if columna not in numericas:

            messagebox.showerror(
                "Error",
                "La columna no es numérica."
            )

            return None

        return columna

    def resumen():

        mostrar_texto(
            df.describe().to_string()
        )

    def media():

        columna = pedir_columna()

        if columna:

            mostrar_texto(
                f"Media de {columna}: "
                f"{df[columna].mean():.2f}"
            )

    def mediana():

        columna = pedir_columna()

        if columna:

            mostrar_texto(
                f"Mediana de {columna}: "
                f"{df[columna].median():.2f}"
            )

    def moda():

        columna = simpledialog.askstring(
            "Moda",
            "Digite la columna:"
        )

        if columna in df.columns:

            mostrar_texto(
                "Moda:\n"
                + str(df[columna].mode().tolist())
            )

    def minimo_maximo():

        columna = pedir_columna()

        if columna:

            mostrar_texto(
                f"Mínimo: {df[columna].min()}\n"
                f"Máximo: {df[columna].max()}"
            )

    def rango():

        columna = pedir_columna()

        if columna:

            resultado = (
                df[columna].max()
                - df[columna].min()
            )

            mostrar_texto(
                f"Rango: {resultado:.2f}"
            )

    def varianza():

        columna = pedir_columna()

        if columna:

            mostrar_texto(
                f"Varianza: "
                f"{df[columna].var():.2f}"
            )

    def desviacion():

        columna = pedir_columna()

        if columna:

            mostrar_texto(
                f"Desviación estándar: "
                f"{df[columna].std():.2f}"
            )

    def coeficiente_variacion():

        columna = pedir_columna()

        if columna:

            media_valor = df[columna].mean()

            if media_valor != 0:

                cv = (
                    df[columna].std() / media_valor) * 100

                mostrar_texto(
                    f"Coeficiente de variación: "
                    f"{cv:.2f}%"
                )

    def cuartiles():

        columna = pedir_columna()

        if columna:

            q1 = df[columna].quantile(0.25)
            q2 = df[columna].quantile(0.50)
            q3 = df[columna].quantile(0.75)

            mostrar_texto(
                f"Q1: {q1:.2f}\n"
                f"Q2: {q2:.2f}\n"
                f"Q3: {q3:.2f}"
            )

    def atipicos():

        columna = pedir_columna()

        if columna:

            q1 = df[columna].quantile(0.25)

            q3 = df[columna].quantile(0.75)

            ric = q3 - q1

            inferior = q1 - 1.5 * ric

            superior = q3 + 1.5 * ric

            resultado = df[
                (df[columna] < inferior)
                |
                (df[columna] > superior)
            ]

            texto = (
                f"Q1: {q1:.2f}\n"
                f"Q3: {q3:.2f}\n"
                f"RIC: {ric:.2f}\n"
                f"Límite inferior: {inferior:.2f}\n"
                f"Límite superior: {superior:.2f}\n"
                f"Atípicos: {len(resultado)}\n\n"
                f"{resultado.to_string()}"
            )

            mostrar_texto(texto)

    opciones = [

        ("Resumen estadístico", resumen),

        ("Media", media),

        ("Mediana", mediana),

        ("Moda", moda),

        ("Mínimo y máximo", minimo_maximo),

        ("Rango", rango),

        ("Varianza", varianza),

        ("Desviación estándar", desviacion),

        ("Coeficiente de variación", coeficiente_variacion),

        ("Cuartiles", cuartiles),

        ("Valores atípicos", atipicos)
    ]

    for texto, funcion in opciones:

        tk.Button(
            ventana,
            text=texto,
            width=35,
            command=funcion
        ).pack(pady=3)

    tk.Button(
        ventana,
        text="Cerrar",
        width=35,
        command=ventana.destroy
    ).pack(pady=10)

# 8. Submenu de filtros y columnas

def ventana_filtros():

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title("Filtros y Consultas")
    ventana.geometry("450x550")

    tk.Label(
        ventana,
        text="Filtros y Consultas",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    # 1. Busca un valor

    def buscar():

        columna = simpledialog.askstring(
            "Buscar",
            "Digite la columna:"
        )

        if columna is None:
            return

        if columna not in df.columns:

            messagebox.showerror(
                "Error",
                "La columna no existe."
            )

            return

        valor = simpledialog.askstring(
            "Buscar",
            "Digite el valor:"
        )

        if valor is None:
            return

        resultado = df[
            df[columna]
            .astype(str)
            .str.lower()
            == valor.lower()
        ]

        if resultado.empty:

            mostrar_texto(
                "No se encontraron resultados."
            )

        else:

            mostrar_texto(
                "===== RESULTADO DE BÚSQUEDA =====\n\n"
                + resultado.to_string()
            )

    # 2. Muestra cantidades negativas

    def cantidad_negativa():

        if "cantidad" not in df.columns:

            messagebox.showerror(
                "Error",
                "No existe la columna cantidad."
            )

            return

        resultado = df[
            df["cantidad"] < 0
        ]

        if resultado.empty:

            mostrar_texto(
                "No existen cantidades negativas."
            )

        else:

            mostrar_texto(
                "****** Cantidades Negativas ******\n\n"
                + resultado.to_string()
                + "\n\nCantidad de registros: "
                + str(len(resultado))
            )

    # 3. Filtra por categoria

    def filtrar_categoria():

        if "categoria" not in df.columns:

            messagebox.showerror(
                "Error",
                "No existe la columna categoria."
            )

            return

        valor = simpledialog.askstring(
            "Categoría",
            "Digite la categoría:"
        )

        if valor is None:
            return

        resultado = df[
            df["categoria"]
            .astype(str)
            .str.strip()
            .str.lower()
            == valor.strip().lower()
        ]

        if resultado.empty:

            mostrar_texto(
                "No se encontraron registros "
                "para la categoría: " + valor
            )

        else:

            mostrar_texto(
                "****** Categoria: "
                + valor.upper()
                + " ******\n\n"
                + resultado.to_string()
            )

    # 4. Filtra por region

    def filtrar_region():

        if "region" not in df.columns:

            messagebox.showerror(
                "Error",
                "No existe la columna region."
            )

            return

        valor = simpledialog.askstring(
            "Región",
            "Digite la región:"
        )

        if valor is None:
            return

        resultado = df[
            df["region"]
            .astype(str)
            .str.strip()
            .str.lower()
            == valor.strip().lower()
        ]

        if resultado.empty:

            mostrar_texto(
                "No se encontraron registros "
                "para la región: " + valor
            )

        else:

            mostrar_texto(
                "***** Región: "
                + valor.upper()
                + " *****\n\n"
                + resultado.to_string()
            )

    # 5. Filtra por vendedor

    def filtrar_vendedor():

        if "vendedor" not in df.columns:

            messagebox.showerror(
                "Error",
                "No existe la columna vendedor."
            )

            return

        valor = simpledialog.askstring(
            "Vendedor",
            "Digite el nombre del vendedor:"
        )

        if valor is None:
            return

        resultado = df[
            df["vendedor"]
            .astype(str)
            .str.strip()
            .str.lower()
            == valor.strip().lower()
        ]

        if resultado.empty:

            mostrar_texto(
                "No se encontraron ventas "
                "para el vendedor: " + valor
            )

        else:

            mostrar_texto(
                "******* Vendedor: "
                + valor.upper()
                + " *******\n\n"
                + resultado.to_string()
            )

    # 6. Filtra por metodo de pago

    def filtrar_pago():

        if "metodo_pago" not in df.columns:

            messagebox.showerror(
                "Error",
                "No existe la columna metodo_pago."
            )

            return

        valor = simpledialog.askstring(
            "Método de pago",
            "Digite el método de pago:"
        )

        if valor is None:
            return

        resultado = df[
            df["metodo_pago"]
            .astype(str)
            .str.strip()
            .str.lower()
            == valor.strip().lower()
        ]

        if resultado.empty:

            mostrar_texto(
                "No se encontraron registros "
                "para el método de pago: " + valor
            )

        else:

            mostrar_texto(
                "***** Metodo de pago: "
                + valor.upper()
                + " ******\n\n"
                + resultado.to_string()
            )

    # 7. Muestra clientes frecuentes

    def clientes_frecuentes():

        if "cliente_frecuente" not in df.columns:

            messagebox.showerror(
                "Error",
                "No existe la columna cliente_frecuente."
            )

            return

        resultado = df[
            df["cliente_frecuente"]
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["sí", "si"])
        ]

        if resultado.empty:

            mostrar_texto(
                "No existen clientes frecuentes."
            )

        else:

            mostrar_texto(
                "******* Clientes Frecuentes ******\n\n"
                + resultado.to_string()
                + "\n\nCantidad de registros: "
                + str(len(resultado))
            )

    # 8. Muestra valores unicos

    def valores_unicos():

        columna = simpledialog.askstring(
            "Valores únicos",
            "Digite la columna:"
        )

        if columna is None:
            return

        if columna not in df.columns:

            messagebox.showerror(
                "Error",
                "La columna no existe."
            )

            return

        resultado = df[columna].dropna().unique()

        texto = (
            "****** Valores unicos de  "
            + columna.upper()
            + " ******\n\n"
        )

        for valor in resultado:

            texto += str(valor) + "\n"

        texto += (
            "\nCantidad de valores únicos: "
            + str(len(resultado))
        )

        mostrar_texto(texto)

    # Botones del submenu

    opciones = [

        (
            "1. Buscar un valor",
            buscar
        ),

        (
            "2. Mostrar cantidades negativas",
            cantidad_negativa
        ),

        (
            "3. Filtrar por categoría",
            filtrar_categoria
        ),

        (
            "4. Filtrar por región",
            filtrar_region
        ),

        (
            "5. Filtrar por vendedor",
            filtrar_vendedor
        ),

        (
            "6. Filtrar por método de pago",
            filtrar_pago
        ),

        (
            "7. Mostrar clientes frecuentes",
            clientes_frecuentes
        ),

        (
            "8. Mostrar valores únicos",
            valores_unicos
        )
    ]

    # Crea los botones

    for texto, funcion in opciones:

        tk.Button(
            ventana,
            text=texto,
            width=38,
            command=funcion
        ).pack(pady=5)

    # 9. Cerrar

    tk.Button(
        ventana,
        text="9. Cerrar",
        width=38,
        command=ventana.destroy
    ).pack(pady=15)

# 9. Submenu de agrupaciones

def ventana_agrupaciones():

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title(
        "Agrupaciones"
    )

    ventana.geometry(
        "430x420"
    )

    tk.Label(
        ventana,
        text="AGRUPACIONES",
        font=("Arial", 16, "bold")
    ).pack(pady=15)


    def operacion(tipo):

        grupo = simpledialog.askstring(
            "Agrupar",
            "Columna para agrupar:"
        )

        if grupo not in df.columns:
            return

        if tipo == "conteo":

            resultado = df.groupby(
                grupo
            ).size()

        else:

            columna = simpledialog.askstring(
                "Variable",
                "Columna numérica:"
            )

            numericas = df.select_dtypes(
                include="number"
            ).columns

            if columna not in numericas:
                return

            if tipo == "promedio":

                resultado = df.groupby(
                    grupo
                )[columna].mean()

            elif tipo == "suma":

                resultado = df.groupby(
                    grupo
                )[columna].sum()

            elif tipo == "minimo":

                resultado = df.groupby(
                    grupo
                )[columna].min()

            else:

                resultado = df.groupby(
                    grupo
                )[columna].max()

        mostrar_texto(
            resultado.round(2).to_string()
        )

    tk.Button(
        ventana,
        text="Contar por grupo",
        width=35,
        command=lambda: operacion("conteo")
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Promedio por grupo",
        width=35,
        command=lambda: operacion("promedio")
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Suma por grupo",
        width=35,
        command=lambda: operacion("suma")
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Mínimo por grupo",
        width=35,
        command=lambda: operacion("minimo")
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Máximo por grupo",
        width=35,
        command=lambda: operacion("maximo")
    ).pack(pady=5)

    tk.Button(
        ventana,
        text="Cerrar",
        width=35,
        command=ventana.destroy
    ).pack(pady=15)

# 10. Submenu de graficos

def ventana_graficos():

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title("Representaciones Gráficas")
    ventana.geometry("450x500")

    tk.Label(
        ventana,
        text="GRÁFICOS",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    # 1. Grafico de barras

    def barras():

        columna = simpledialog.askstring(
            "Gráfico de barras",
            "Digite la columna:"
        )

        if columna is None:
            return

        if columna not in df.columns:

            messagebox.showerror(
                "Error",
                "La columna no existe."
            )
            return

        datos = (
            df[columna]
            .value_counts()
            .head(10)
        )

        plt.figure(figsize=(9, 5))

        datos.plot(
            kind="bar",
            color="green",
            edgecolor="black"
        )

        plt.title(
            "Frecuencia de " + columna
        )

        plt.xlabel(columna)
        plt.ylabel("Cantidad")

        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.grid(
            axis="y",
            alpha=0.3
        )

        plt.tight_layout()

        plt.show()

    # 2. Histograma

    def histograma():

        numericas = df.select_dtypes(
            include="number"
        ).columns.tolist()

        columna = simpledialog.askstring(
            "Histograma",
            "Columnas numéricas:\n\n"
            + "\n".join(numericas)
            + "\n\nDigite la columna:"
        )

        if columna is None:
            return

        if columna not in numericas:

            messagebox.showerror(
                "Error",
                "Debe seleccionar una columna numérica."
            )
            return

        datos = df[columna].dropna()

        plt.figure(figsize=(9, 5))

        plt.hist(
            datos,
            bins=15,
            color="lightgreen",
            edgecolor="black"
        )

        plt.title(
            "Distribución de " + columna
        )

        plt.xlabel(columna)
        plt.ylabel("Frecuencia")

        plt.grid(
            axis="y",
            alpha=0.3
        )

        plt.ticklabel_format(
            style="plain",
            axis="x"
        )

        plt.tight_layout()

        plt.show()

    # 3. Grafico de lineas

    def linea():

        numericas = df.select_dtypes(
            include="number"
        ).columns.tolist()

        columna = simpledialog.askstring(
            "Gráfico de líneas",
            "Columnas numéricas:\n\n"
            + "\n".join(numericas)
            + "\n\nDigite la columna:"
        )

        if columna is None:
            return

        if columna not in numericas:

            messagebox.showerror(
                "Error",
                "Debe seleccionar una columna numérica."
            )
            return

        # Si existe la columna fecha,
        # se utiliza para crear una tendencia temporal
        if "fecha" in df.columns:

            datos = df.copy()

            datos["fecha"] = pd.to_datetime(
                datos["fecha"],
                errors="coerce"
            )

            datos = datos.dropna(
                subset=["fecha", columna]
            )

            # Agrupa por fecha
            resultado = (
                datos
                .groupby("fecha")[columna]
                .mean()
                .sort_index()
            )

            plt.figure(figsize=(10, 5))

            plt.plot(
                resultado.index,
                resultado.values,
                marker="o",
                markersize=3,
                color="red"
            )

            plt.title(
                "Promedio de "
                + columna
                + " por fecha"
            )

            plt.xlabel("Fecha")
            plt.ylabel(columna)

            plt.xticks(
                rotation=45
            )

        else:

            # Si no existe fecha,
            # utiliza el número de registro
            datos = df[columna].dropna()

            plt.figure(figsize=(10, 5))

            plt.plot(
                datos.values,
                color="red"
            )

            plt.title(
                "Gráfico de líneas de "
                + columna
            )

            plt.xlabel("Registro")
            plt.ylabel(columna)

        plt.grid(
            alpha=0.3
        )

        plt.ticklabel_format(
            style="plain",
            axis="y"
        )

        plt.tight_layout()

        plt.show()

    # 4. Grafico de dispersion

    def dispersion():

        numericas = df.select_dtypes(
            include="number"
        ).columns.tolist()

        x = simpledialog.askstring(
            "Variable X",
            "Columnas numéricas:\n\n"
            + "\n".join(numericas)
            + "\n\nDigite variable X:"
        )

        if x is None:
            return

        y = simpledialog.askstring(
            "Variable Y",
            "Columnas numéricas:\n\n"
            + "\n".join(numericas)
            + "\n\nDigite variable Y:"
        )

        if y is None:
            return

        if x not in numericas or y not in numericas:

            messagebox.showerror(
                "Error",
                "Las dos variables deben ser numéricas."
            )
            return

        datos = df[
            [x, y]
        ].dropna()

        plt.figure(figsize=(8, 5))

        plt.scatter(
            datos[x],
            datos[y],
            alpha=0.6
        )

        plt.title(
            x + " vs " + y
        )

        plt.xlabel(x)
        plt.ylabel(y)

        plt.grid(
            alpha=0.3
        )

        plt.ticklabel_format(
            style="plain"
        )

        plt.tight_layout()

        plt.show()

    # 5. Boxplot

    def boxplot():

        numericas = df.select_dtypes(
            include="number"
        ).columns.tolist()

        columna = simpledialog.askstring(
            "Boxplot",
            "Columnas numéricas:\n\n"
            + "\n".join(numericas)
            + "\n\nDigite la columna:"
        )

        if columna is None:
            return

        if columna not in numericas:

            messagebox.showerror(
                "Error",
                "Debe seleccionar una columna numérica."
            )
            return

        datos = df[columna].dropna()

        plt.figure(figsize=(7, 5))

        plt.boxplot(
            datos,
            vert=True
        )

        plt.title(
            "Boxplot de " + columna
        )

        plt.ylabel(columna)

        plt.grid(
            axis="y",
            alpha=0.3
        )

        plt.ticklabel_format(
            style="plain",
            axis="y"
        )

        plt.tight_layout()

        plt.show()

    # BOTONES

    opciones = [

        (
            "1. Gráfico de barras",
            barras
        ),

        (
            "2. Histograma",
            histograma
        ),

        (
            "3. Gráfico de líneas",
            linea
        ),

        (
            "4. Gráfico de dispersión",
            dispersion
        ),

        (
            "5. Boxplot",
            boxplot
        )
    ]

    for texto, funcion in opciones:

        tk.Button(
            ventana,
            text=texto,
            width=36,
            command=funcion
        ).pack(pady=6)


    tk.Button(
        ventana,
        text="6. Cerrar",
        width=36,
        command=ventana.destroy
    ).pack(pady=15)

# 11. Analisis adicional

def ventana_adicional():

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title(
        "Análisis Adicional"
    )

    ventana.geometry(
        "300x300"
    )

    tk.Label(
        ventana,
        text="Análisis Adicional",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    def matriz():

        numericas = df.select_dtypes(
            include="number"
        )

        if numericas.shape[1] >= 2:

            mostrar_texto(
                numericas.corr().round(2).to_string()
            )

        else:

            messagebox.showwarning(
                "Advertencia",
                "No hay suficientes variables numéricas."
            )

    def unicos():

        mostrar_texto(
            "Valores únicos por columna\n\n"
            + df.nunique().to_string()
        )

    def resumen():

        texto = (
            "****** Resumen General ******\n\n"
            f"Filas: {df.shape[0]}\n"
            f"Columnas: {df.shape[1]}\n"
            f"Valores nulos: "
            f"{df.isnull().sum().sum()}\n"
            f"Duplicados: "
            f"{df.duplicated().sum()}\n"
        )

        mostrar_texto(texto)

    opciones = [

        ("Matriz de correlaciones", matriz),

        ("Valores únicos", unicos),

        ("Resumen general", resumen)
    ]

    for texto, funcion in opciones:

        tk.Button(
            ventana,
            text=texto,
            width=35,
            command=funcion
        ).pack(pady=5)

    tk.Button(
        ventana,
        text="Cerrar",
        width=35,
        command=ventana.destroy
    ).pack(pady=15)

# 12. Ingreso de datos---readme

def ventana_ingreso():

    global df
    global registros_nuevos

    if not verificar_df():
        return

    ventana = tk.Toplevel(root)

    ventana.title(
        "Ingreso de Datos"
    )

    ventana.geometry(
        "450x450"
    )

    tk.Label(
        ventana,
        text="Ingreso de datos",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    # Nuevo ingreso

    def nuevo_registro():

        nuevo = {}

        for columna in df.columns:

            valor = simpledialog.askstring(
                "Nuevo registro",
                columna + ":"
            )

            nuevo[columna] = valor

        registros_nuevos.append(
            nuevo
        )

        messagebox.showinfo(
            "Correcto",
            "Registro agregado."
        )

    # Muestra nuevos

    def mostrar_nuevos():

        if len(registros_nuevos) == 0:

            mostrar_texto(
                "No existen registros nuevos."
            )

        else:

            nuevos = pd.DataFrame(
                registros_nuevos
            )

            mostrar_texto(
                nuevos.to_string()
            )

    # Funcion guardar

    def guardar():

        global df
        global registros_nuevos

        if len(registros_nuevos) == 0:

            messagebox.showwarning(
                "Advertencia",
                "No hay registros para guardar."
            )

            return

        nuevos = pd.DataFrame(
            registros_nuevos
        )

        df = pd.concat(
            [df, nuevos],
            ignore_index=True
        )

        archivo = filedialog.asksaveasfilename(
            title="Guardar archivo",
            defaultextension=".csv",
            filetypes=[
                ("Archivo CSV", "*.csv")
            ]
        )

        if archivo:

            df.to_csv(
                archivo,
                index=False
            )

            registros_nuevos.clear()

            messagebox.showinfo(
                "Correcto",
                "Datos guardados correctamente."
            )

    # README
    def crear_readme():

        archivo = filedialog.asksaveasfilename(
            title="Guardar README",
            defaultextension=".txt",
            filetypes=[
                ("Archivo de texto", "*.txt")
            ]
        )

        if not archivo:
            return

        try:

            with open(
                archivo,
                "w",
                encoding="utf-8"
            ) as readme:

                readme.write(
                    "PROYECTO FINAL - MANEJO DE DATOS – EDA\n"
                )

                readme.write(
                    "Módulo: Manejo de Datos - EDA\n"
                )

                readme.write(
                    "Estudiante: Marilyn Miranda Jaen\n\n"
                )

                readme.write(
                    "DESCRIPCIÓN\n"
                )

                readme.write(
                    "Programa desarrollado en Python "
                    "para cargar, explorar, analizar "
                    "e interpretar datos de un "
                    "archivo CSV.\n\n"
                )

                readme.write(
                    "ESTRUCTURA DEL DATASET\n"
                )

                readme.write(
                    f"Filas: {df.shape[0]}\n"
                )

                readme.write(
                    f"Columnas: {df.shape[1]}\n\n"
                )

                readme.write(
                    "Columnas y Tipos de datos\n"
                )

                for columna in df.columns:

                    readme.write(
                        f"- {columna}: "
                        f"{df[columna].dtype}\n"
                    )

                readme.write(
                    "\nFunciones del programa\n"
                )

                readme.write(
                    "1. Cargar archivo CSV\n"
                )

                readme.write(
                    "2. Información del dataset\n"
                )

                readme.write(
                    "3. Primeras y últimas filas\n"
                )

                readme.write(
                    "4. Tipos de datos\n"
                )

                readme.write(
                    "5. Valores nulos\n"
                )

                readme.write(
                    "6. Datos duplicados\n"
                )

                readme.write(
                    "7. Estadísticas descriptivas\n"
                )

                readme.write(
                    "8. Filtros\n"
                )

                readme.write(
                    "9. Agrupaciones\n"
                )

                readme.write(
                    "10. Representaciones gráficas\n"
                )

                readme.write(
                    "11. Análisis adicional\n"
                )

                readme.write(
                    "12. Ingreso de datos\n"
                )

                readme.write(
                    "13. Salir\n"
                )

            messagebox.showinfo(
                "Correcto",
                "README creado correctamente."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    tk.Button(
        ventana,
        text="Ingresar nuevo registro",
        width=35,
        command=nuevo_registro
    ).pack(pady=6)

    tk.Button(
        ventana,
        text="Mostrar registros ingresados",
        width=35,
        command=mostrar_nuevos
    ).pack(pady=6)

    tk.Button(
        ventana,
        text="Guardar nuevos datos",
        width=35,
        command=guardar
    ).pack(pady=6)

    tk.Button(
        ventana,
        text="Crear archivo README",
        width=35,
        command=crear_readme
    ).pack(pady=6)

    tk.Button(
        ventana,
        text="Cerrar",
        width=35,
        command=ventana.destroy
    ).pack(pady=15)

# Ventana Principal

root = tk.Tk()

root.title(
    "Proyecto Final - Marilyn Miranda Jaen"
)

root.geometry(
    "1250x720"
)

root.minsize(
    1100,
    650
)

# Titulo principal

titulo = tk.Label(
    root,
    text="Manejo de Datos – EDA",
    font=("Arial", 18, "bold")
)

titulo.pack(
    pady=(15, 10)
)

# Contenedor general

contenedor = tk.Frame(
    root
)

contenedor.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)

# Menu de panel izquierdo

panel_botones = tk.LabelFrame(
    contenedor,
    text=" Menú Principal ",
    font=("Arial", 11, "bold"),
    padx=12,
    pady=10,
    labelanchor="n"
)

panel_botones.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)

# Botones principales

botones = [

    (
        "1. Cargar CSV",
        cargar_csv
    ),

    (
        "2. Información del conjunto de datos",
        informacion_dataset
    ),

    (
        "3. Primeras y últimas filas",
        primeras_ultimas
    ),

    (
        "4. Analizar tipos de datos",
        ventana_tipos
    ),

    (
        "5. Analizar valores nulos",
        ventana_nulos
    ),

    (
        "6. Analizar datos duplicados",
        ventana_duplicados
    ),

    (
        "7. Estadísticas descriptivas",
        ventana_estadisticas
    ),

    (
        "8. Filtrar o consultar datos",
        ventana_filtros
    ),

    (
        "9. Agrupaciones y operaciones",
        ventana_agrupaciones
    ),

    (
        "10. Representaciones gráficas",
        ventana_graficos
    ),

    (
        "11. Análisis adicional",
        ventana_adicional
    ),

    (
        "12. Ingreso de datos / README",
        ventana_ingreso
    )
]

# Crea botones

for texto, funcion in botones:

    tk.Button(
        panel_botones,
        text=texto,
        width=34,
        height=1,
        font=("Arial", 10, "bold"),
        anchor="center",
        command=funcion
    ).pack(
        fill="x",
        pady=3
    )

# Boton salir

tk.Button(
    panel_botones,
    text="13. Salir",
    width=34,
    height=1,
    font=("Arial", 10, "bold"),
    anchor="center",
    command=root.destroy
).pack(
    fill="x",
    pady=(10, 3)
)

# Resultados de panel derecho

panel_resultados = tk.LabelFrame(
    contenedor,
    text=" Resultados del Análisis ",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=10
)

panel_resultados.pack(
    side="right",
    fill="both",
    expand=True
)

# Frame para texto y scroll

frame_texto = tk.Frame(
    panel_resultados
)

frame_texto.pack(
    fill="both",
    expand=True
)

# Barra vertical

scroll_y = tk.Scrollbar(
    frame_texto
)

scroll_y.pack(
    side="right",
    fill="y"
)

# Barra horizontal

scroll_x = tk.Scrollbar(
    frame_texto,
    orient="horizontal"
)

scroll_x.pack(
    side="bottom",
    fill="x"
)

# Área de resultados

salida = tk.Text(
    frame_texto,
    wrap="none",
    font=("Consolas", 10),
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)

salida.pack(
    fill="both",
    expand=True
)

scroll_y.config(
    command=salida.yview
)

scroll_x.config(
    command=salida.xview
)

# Inicia interfaz

root.mainloop()