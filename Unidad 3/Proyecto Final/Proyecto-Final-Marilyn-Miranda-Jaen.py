import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

plt.style.use("dark_background")
pd.options.display.float_format = "{:.2f}".format

# *** variables globales / global variables ***
datos = None
nuevos_registros = []

# *** muestra texto en el panel de resultados / displays text in the results panel ***
# *** muestra el contenido en el área de resultados / displays the content in the results area ***
def mostrar_texto(contenido):
    area_resultados.delete("1.0", tk.END)
    area_resultados.insert(tk.END, contenido)

# *** verifica que exista un dataframe cargado / checks that a dataframe is loaded ***
# *** verifica que los datos hayan sido cargados / checks that the data has been loaded ***
def verificar_df():
    if datos is None:
        messagebox.showwarning(
            "Advertencia",
            "Primero debe cargar un archivo CSV."
        )
        return False
    return True

# *** crea una ventana secundaria / creates a secondary window ***
# *** crea una ventana secundaria reutilizable / creates a reusable secondary window ***
def crear_ventana(encabezado, dimension="450x500"):
    ventana_actual = tk.Toplevel(ventana_principal)
    ventana_actual.title(encabezado)
    ventana_actual.geometry(dimension)

    tk.Label(
        ventana_actual,
        text=encabezado,
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    return ventana_actual

# *** crea botones de forma reutilizable / creates reusable buttons ***
# *** crea los botones de cada submenú / creates the buttons for each submenu ***
def crear_botones(ventana_actual, lista_opciones, ancho_boton=35):
    for contenido, accion in lista_opciones:
        tk.Button(
            ventana_actual,
            text=contenido,
            width=ancho_boton,
            command=accion
        ).pack(pady=5)

# *** solicita una columna existente / asks for an existing column ***
# *** solicita y valida una columna del conjunto de datos / asks for and validates a dataset column ***
def pedir_columna(encabezado="Columna"):
    if datos is None:
        return None

    campo = simpledialog.askstring(
        encabezado,
        "Columnas disponibles:\n\n"
        + "\n".join(datos.columns)
        + "\n\nDigite la columna:"
    )

    if campo is None:
        return None

    if campo not in datos.columns:
        messagebox.showerror(
            "Error",
            "La columna no existe."
        )
        return None

    return campo

# *** solicita una columna numerica / asks for a numeric column ***
# *** solicita y valida una columna numérica / asks for and validates a numeric column ***
def pedir_columna_numerica(encabezado="Columna numérica"):
    campos_numericos = datos.select_dtypes(
        include="number"
    ).columns.tolist()

    campo = simpledialog.askstring(
        encabezado,
        "Columnas numéricas:\n\n"
        + "\n".join(campos_numericos)
        + "\n\nDigite la columna:"
    )

    if campo is None:
        return None

    if campo not in campos_numericos:
        messagebox.showerror(
            "Error",
            "Debe seleccionar una columna numérica."
        )
        return None

    return campo

# *** carga un archivo csv / loads a csv file ***
# *** selecciona y carga el archivo csv / selects and loads the csv file ***
def cargar_csv():
    global datos

    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("Archivo CSV", "*.csv")]
    )

    if not ruta_archivo:
        return

    try:
        datos = pd.read_csv(ruta_archivo)

        contenido = (
            "Datos\n\n"
            f"Filas: {datos.shape[0]}\n"
            f"Columnas: {datos.shape[1]}\n\n"
            "Primeras filas:\n\n"
            f"{datos.head().to_string()}"
        )

        mostrar_texto(contenido)

        messagebox.showinfo(
            "Correcto",
            "Archivo CSV cargado correctamente."
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )

# *** muestra informacion general del dataset / displays general dataset information ***
# *** muestra filas columnas y tipos de datos / displays rows columns and data types ***
def informacion_dataset():
    if not verificar_df():
        return

    contenido = (
        "****** información de dataset ******\n\n"
        f"cantidad de filas: {datos.shape[0]}\n"
        f"cantidad de columnas: {datos.shape[1]}\n\n"
        "columnas:\n"
        + "\n".join(f"- {col}" for col in datos.columns)
        + "\n\ntipos de datos:\n"
        + datos.dtypes.to_string()
    )

    mostrar_texto(contenido)

# *** muestra primeras y ultimas filas / displays first and last rows ***
# *** muestra una vista inicial y final de los datos / displays an initial and final view of the data ***
def primeras_ultimas():
    if not verificar_df():
        return
    mostrar_texto(
        "------ primeras 5 filas ------\n\n"
        + datos.head().to_string()
        + "\n\n------ últimas 5 filas ------\n\n"
        + datos.tail().to_string()
    )

# *** submenú de tipos de datos / data types submenu ***
# *** abre las opciones para analizar tipos de datos / opens the options to analyze data types ***
def ventana_tipos():
    global datos

    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Tipos de datos",
        "430x430"
    )

    # *** muestra el tipo de dato de cada columna / displays the data type of each column ***
    def mostrar_tipos():
        mostrar_texto(
            "****** tipos de datos ******\n\n"
            + datos.dtypes.to_string()
        )

    # *** muestra únicamente las columnas numéricas / displays only the numeric columns ***
    def columnas_numericas():
        lista_columnas = datos.select_dtypes(
            include="number"
        ).columns.tolist()

        mostrar_texto(
            "------ columnas numéricas ------\n\n"
            + "\n".join(lista_columnas)
        )

    # *** muestra únicamente las columnas de texto / displays only the text columns ***
    def columnas_texto():
        lista_columnas = datos.select_dtypes(
            include=["object", "string"]
        ).columns.tolist()

        mostrar_texto(
            "------ columnas de texto ------\n\n"
            + "\n".join(lista_columnas)
        )

    # *** cuenta cuántas columnas existen por tipo de dato / counts how many columns exist by data type ***
    def contar_tipos():
        mostrar_texto(
            "------ cantidad por tipo de dato ------\n\n"
            + datos.dtypes.value_counts().to_string()
        )

    # *** convierte una columna seleccionada a tipo numérico / converts a selected column to numeric type ***
    def convertir_numero():
        global datos

        campo = pedir_columna("Convertir a número")
        if campo:
            datos[campo] = pd.to_numeric(
                datos[campo],
                errors="coerce"
            )
            messagebox.showinfo(
                "Correcto",
                "Columna convertida a número."
            )

    # *** convierte una columna seleccionada a tipo texto / converts a selected column to text type ***
    def convertir_texto():
        global datos

        campo = pedir_columna("Convertir a texto")
        if campo:
            datos[campo] = datos[campo].astype("string")
            messagebox.showinfo(
                "Correcto",
                "Columna convertida a texto."
            )
    lista_opciones = [
        ("Mostrar tipos de datos", mostrar_tipos),
        ("Columnas numéricas", columnas_numericas),
        ("Columnas de texto", columnas_texto),
        ("Contar tipos de datos", contar_tipos),
        ("Convertir columna a número", convertir_numero),
        ("Convertir columna a texto", convertir_texto),
        ("Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones, 28)

# *** submenú de valores nulos / null values submenu ***
# *** abre las opciones para analizar valores nulos / opens the options to analyze null values ***
def ventana_nulos():
    global datos

    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Valores nulos",
        "350x360"
    )

    # *** cuenta los valores nulos por columna / counts null values by column ***
    def mostrar_nulos():
        datos_nulos = datos.isnull().sum()

        mostrar_texto(
            "------ valores nulos ------\n\n"
            + datos_nulos.to_string()
            + "\n\ntotal: "
            + str(datos_nulos.sum())
        )

    # *** muestra las filas que contienen valores nulos / displays rows that contain null values ***
    def filas_nulas():
        resultado_datos = datos[
            datos.isnull().any(axis=1)
        ]

        mostrar_texto(
            "No existen filas con valores nulos."
            if resultado_datos.empty
            else resultado_datos.to_string()
        )

    # *** elimina las filas que contienen valores nulos / removes rows that contain null values ***
    def eliminar_nulos():
        global datos

        cantidad_antes = len(datos)
        datos = datos.dropna()

        messagebox.showinfo(
            "Resultado",
            f"Filas eliminadas: {cantidad_antes - len(datos)}"
        )

    # *** reemplaza valores nulos con desconocido / replaces null values with unknown ***
    def rellenar_desconocido():
        global datos

        campo = pedir_columna("Desconocido")
        if campo:
            datos[campo] = datos[campo].fillna(
                "Desconocido"
            )

            messagebox.showinfo(
                "Correcto",
                "Valores reemplazados."
            )

    lista_opciones = [
        ("Mostrar nulos", mostrar_nulos),
        ("Filas con nulos", filas_nulas),
        ("Eliminar filas con nulos", eliminar_nulos),
        ("Rellenar con valor desconocido", rellenar_desconocido),
        ("Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones, 30)

# *** submenú de duplicados / duplicates submenu ***
# *** abre las opciones para analizar datos duplicados / opens the options to analyze duplicate data ***
def ventana_duplicados():
    global datos

    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Datos duplicados",
        "390x390"
    )

    # *** cuenta los registros duplicados / counts duplicate records ***
    def contar():
        mostrar_texto(
            "Cantidad de registros duplicados: "
            + str(datos.duplicated().sum())
        )

    # *** muestra los registros duplicados / displays duplicate records ***
    def mostrar():
        datos_duplicados = datos[
            datos.duplicated(keep=False)
        ]

        mostrar_texto(
            "No existen registros duplicados."
            if datos_duplicados.empty
            else datos_duplicados.to_string()
        )

    # *** elimina los registros duplicados / removes duplicate records ***
    def eliminar():
        global datos

        cantidad_antes = len(datos)
        datos = datos.drop_duplicates()

        messagebox.showinfo(
            "Resultado",
            f"Registros eliminados: {cantidad_antes - len(datos)}"
        )

    # *** busca duplicados según una columna / finds duplicates based on a column ***
    def por_columna():
        campo = pedir_columna("Duplicados")
        if campo:
            resultado_datos = datos[
                datos.duplicated(
                    subset=[campo],
                    keep=False
                )
            ]
            mostrar_texto(resultado_datos.to_string())

    lista_opciones = [
        ("Contar duplicados", contar),
        ("Mostrar duplicados", mostrar),
        ("Eliminar duplicados", eliminar),
        ("Duplicados por columna", por_columna),
        ("Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones)

# *** submenú de estadísticas descriptivas / descriptive statistics submenu ***
# *** abre las opciones de estadísticas descriptivas / opens the descriptive statistics options ***
def ventana_estadisticas():
    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Estadísticas descriptivas",
        "460x600"
    )

    # *** muestra un resumen del análisis / displays an analysis summary ***
    def resumen():
        mostrar_texto(
            datos.describe().to_string()
        )

    # *** calcula la media de una columna numérica / calculates the mean of a numeric column ***
    def media():
        campo = pedir_columna_numerica()
        if campo:
            mostrar_texto(
                f"media de {campo}: "
                f"{datos[campo].mean():.2f}"
            )

    # *** calcula la mediana de una columna numérica / calculates the median of a numeric column ***
    def mediana():
        campo = pedir_columna_numerica()
        if campo:
            mostrar_texto(
                f"mediana de {campo}: "
                f"{datos[campo].median():.2f}"
            )

    # *** calcula la moda de una columna / calculates the mode of a column ***
    def moda():
        campo = pedir_columna("Moda")
        if campo:
            mostrar_texto(
                "moda:\n"
                + str(datos[campo].mode().tolist())
            )

    # *** calcula el valor mínimo y máximo / calculates the minimum and maximum value ***
    def minimo_maximo():
        campo = pedir_columna_numerica()
        if campo:
            mostrar_texto(
                f"mínimo: {datos[campo].min()}\n"
                f"máximo: {datos[campo].max()}"
            )

    # *** calcula el rango de una columna numérica / calculates the range of a numeric column ***
    def rango():
        campo = pedir_columna_numerica()
        if campo:
            resultado_datos = (
                datos[campo].max()
                - datos[campo].min()
            )
            mostrar_texto(
                f"rango: {resultado_datos:.2f}"
            )

    # *** calcula la varianza de una columna numérica / calculates the variance of a numeric column ***
    def varianza():
        campo = pedir_columna_numerica()
        if campo:
            mostrar_texto(
                f"varianza: {datos[campo].var():.2f}"
            )

    # *** calcula la desviación estándar / calculates the standard deviation ***
    def desviacion():
        campo = pedir_columna_numerica()
        if campo:
            mostrar_texto(
                f"desviación estándar: "
                f"{datos[campo].std():.2f}"
            )

    # *** calcula el coeficiente de variación / calculates the coefficient of variation ***
    def coeficiente_variacion():
        campo = pedir_columna_numerica()

        if campo:
            valor_media = datos[campo].mean()

            if valor_media == 0:
                messagebox.showwarning(
                    "Advertencia",
                    "No se puede calcular porque la media es 0."
                )
                return

            coef_variacion = (
                datos[campo].std()
                / valor_media
            ) * 100

            mostrar_texto(
                f"coeficiente de variación: "
                f"{coef_variacion:.2f}%"
            )

    # *** calcula los tres cuartiles principales / calculates the three main quartiles ***
    def cuartiles():
        campo = pedir_columna_numerica()
        if campo:
            cuartil_uno = datos[campo].quantile(0.25)
            cuartil_dos = datos[campo].quantile(0.50)
            cuartil_tres = datos[campo].quantile(0.75)

            mostrar_texto(
                f"q1: {cuartil_uno:.2f}\n"
                f"q2: {cuartil_dos:.2f}\n"
                f"q3: {cuartil_tres:.2f}"
            )

    # *** identifica valores atípicos mediante el rango intercuartílico / identifies outliers using the interquartile range ***
    def atipicos():
        campo = pedir_columna_numerica()

        if campo:
            cuartil_uno = datos[campo].quantile(0.25)
            cuartil_tres = datos[campo].quantile(0.75)
            rango_intercuartil = cuartil_tres - cuartil_uno

            limite_inferior = cuartil_uno - 1.5 * rango_intercuartil
            limite_superior = cuartil_tres + 1.5 * rango_intercuartil

            resultado_datos = datos[
                (datos[campo] < limite_inferior)
                |
                (datos[campo] > limite_superior)
            ]

            mostrar_texto(
                f"q1: {cuartil_uno:.2f}\n"
                f"q3: {cuartil_tres:.2f}\n"
                f"ric: {rango_intercuartil:.2f}\n"
                f"límite inferior: {limite_inferior:.2f}\n"
                f"límite superior: {limite_superior:.2f}\n"
                f"atípicos: {len(resultado_datos)}\n\n"
                + resultado_datos.to_string()
            )

    lista_opciones = [
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
        ("Valores atípicos", atipicos),
        ("Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones)

# *** submenú de filtros y consultas / filters and queries submenu ***
# *** abre las opciones de filtros y consultas / opens the filters and queries options ***
def ventana_filtros():
    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Filtros y consultas",
        "450x550"
    )

    # *** busca un valor dentro de una columna / searches for a value within a column ***
    def buscar():
        campo = pedir_columna("Buscar")
        if not campo:
            return

        dato = simpledialog.askstring(
            "Buscar",
            "Digite el valor:"
        )

        if dato is None:
            return

        resultado_datos = datos[
            datos[campo]
            .astype(str)
            .str.strip()
            .str.lower()
            == dato.strip().lower()
        ]

        mostrar_texto(
            "No se encontraron resultados."
            if resultado_datos.empty
            else resultado_datos.to_string()
        )

    # *** identifica registros con cantidades negativas / identifies records with negative quantities ***
    def cantidad_negativa():
        if "cantidad" not in datos.columns:
            messagebox.showerror(
                "Error",
                "No existe la columna cantidad."
            )
            return

        resultado_datos = datos[
            datos["cantidad"] < 0
        ]

        mostrar_texto(
            "No existen cantidades negativas."
            if resultado_datos.empty
            else (
                "****** cantidades negativas ******\n\n"
                + resultado_datos.to_string()
                + "\n\ncantidad de registros: "
                + str(len(resultado_datos))
            )
        )

    # *** filtra los datos según una columna y un valor / filters data by a column and a value ***
    def filtrar_columna(nombre_campo, encabezado):
        if nombre_campo not in datos.columns:
            messagebox.showerror(
                "Error",
                f"No existe la columna {nombre_campo}."
            )
            return

        dato = simpledialog.askstring(
            encabezado,
            f"Digite {encabezado.lower()}:"
        )

        if dato is None:
            return

        resultado_datos = datos[
            datos[nombre_campo]
            .astype(str)
            .str.strip()
            .str.lower()
            == dato.strip().lower()
        ]

        mostrar_texto(
            f"No se encontraron registros para {encabezado.lower()}: {dato}"
            if resultado_datos.empty
            else resultado_datos.to_string()
        )

    # *** muestra los registros de clientes frecuentes / displays frequent customer records ***
    def clientes_frecuentes():
        if "cliente_frecuente" not in datos.columns:
            messagebox.showerror(
                "Error",
                "No existe la columna cliente_frecuente."
            )
            return

        resultado_datos = datos[
            datos["cliente_frecuente"]
            .astype(str)
            .str.strip()
            .str.lower()
            .isin(["sí", "si"])
        ]

        mostrar_texto(
            "No existen clientes frecuentes."
            if resultado_datos.empty
            else (
                "****** clientes frecuentes ******\n\n"
                + resultado_datos.to_string()
                + "\n\ncantidad de registros: "
                + str(len(resultado_datos))
            )
        )

    # *** muestra los valores únicos de una columna / displays the unique values of a column ***
    def valores_unicos():
        campo = pedir_columna("Valores únicos")
        if campo:
            resultado_datos = datos[campo].dropna().unique()

            mostrar_texto(
                "****** valores únicos de "
                + campo.lower()
                + " ******\n\n"
                + "\n".join(map(str, resultado_datos))
                + "\n\ncantidad de valores únicos: "
                + str(len(resultado_datos))
            )

    lista_opciones = [
        ("1. Buscar un valor", buscar),
        ("2. Mostrar cantidades negativas", cantidad_negativa),
        ("3. Filtrar por categoría", lambda: filtrar_columna("categoria", "Categoría")),
        ("4. Filtrar por región", lambda: filtrar_columna("region", "Región")),
        ("5. Filtrar por vendedor", lambda: filtrar_columna("vendedor", "Vendedor")),
        ("6. Filtrar por método de pago", lambda: filtrar_columna("metodo_pago", "Método de pago")),
        ("7. Mostrar clientes frecuentes", clientes_frecuentes),
        ("8. Mostrar valores únicos", valores_unicos),
        ("9. Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones, 38)

# *** submenú de agrupaciones / grouping submenu ***
# *** abre las opciones para agrupar datos / opens the options to group data ***
def ventana_agrupaciones():
    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Agrupaciones",
        "430x420"
    )

    # *** realiza una operación sobre datos agrupados / performs an operation on grouped data ***
    def operacion(tipo_operacion):
        campo_grupo = pedir_columna("Agrupar")
        if not campo_grupo:
            return

        if tipo_operacion == "conteo":
            resultado_datos = datos.groupby(
                campo_grupo
            ).size()

        else:
            campo = pedir_columna_numerica(
                "Variable numérica"
            )

            if not campo:
                return

            datos_agrupados = datos.groupby(
                campo_grupo
            )[campo]

            diccionario_operaciones = {
                "promedio": datos_agrupados.mean,
                "suma": datos_agrupados.sum,
                "minimo": datos_agrupados.min,
                "maximo": datos_agrupados.max
            }

            resultado_datos = diccionario_operaciones[tipo_operacion]()

        mostrar_texto(
            resultado_datos.round(2).to_string()
        )

    lista_opciones = [
        ("Contar por grupo", lambda: operacion("conteo")),
        ("Promedio por grupo", lambda: operacion("promedio")),
        ("Suma por grupo", lambda: operacion("suma")),
        ("Mínimo por grupo", lambda: operacion("minimo")),
        ("Máximo por grupo", lambda: operacion("maximo")),
        ("Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones)

# *** submenú de gráficos / charts submenu ***
# *** abre las opciones de representaciones gráficas / opens the chart options ***
def ventana_graficos():
    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Gráficos",
        "450x500"
    )

    # *** crea un gráfico de barras / creates a bar chart ***
    def barras():
        campo = pedir_columna(
            "Gráfico de barras"
        )

        if campo:
            datos_grafico = (
                datos[campo]
                .value_counts()
                .head(10)
            )

            plt.figure(figsize=(9, 5))

            datos_grafico.plot(
                kind="bar",
                color="green",
                edgecolor="black"
            )

            plt.title(
                "Frecuencia de " + campo
            )

            plt.xlabel(campo)
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

    # *** crea un histograma / creates a histogram ***
    def histograma():
        campo = pedir_columna_numerica(
            "Histograma"
        )

        if campo:
            datos_grafico = datos[campo].dropna()

            plt.figure(figsize=(9, 5))

            plt.hist(
                datos_grafico,
                bins=15,
                color="lightgreen",
                edgecolor="black"
            )

            plt.title(
                "Distribución de " + campo
            )

            plt.xlabel(campo)
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

    # *** crea un gráfico de líneas / creates a line chart ***
    def linea():
        campo = pedir_columna_numerica(
            "Gráfico de líneas"
        )

        if not campo:
            return

        plt.figure(figsize=(10, 5))

        if "fecha" in datos.columns:
            datos_grafico = datos.copy()

            datos_grafico["fecha"] = pd.to_datetime(
                datos_grafico["fecha"],
                errors="coerce"
            )

            datos_grafico = datos_grafico.dropna(
                subset=["fecha", campo]
            )

            resultado_datos = (
                datos_grafico
                .groupby("fecha")[campo]
                .mean()
                .sort_index()
            )

            plt.plot(
                resultado_datos.index,
                resultado_datos.values,
                marker="o",
                markersize=3,
                color="red"
            )

            plt.title(
                "Promedio de "
                + campo
                + " por fecha"
            )

            plt.xlabel("Fecha")
            plt.xticks(rotation=45)

        else:
            datos_grafico = datos[campo].dropna()

            plt.plot(
                datos_grafico.values,
                color="red"
            )

            plt.title(
                "Gráfico de líneas de "
                + campo
            )

            plt.xlabel("Registro")

        plt.ylabel(campo)

        plt.grid(alpha=0.3)

        plt.ticklabel_format(
            style="plain",
            axis="y"
        )

        plt.tight_layout()
        plt.show()

    # *** crea un gráfico de dispersión / creates a scatter plot ***
    def dispersion():
        variable_x = pedir_columna_numerica(
            "Variable X"
        )

        if not variable_x:
            return

        variable_y = pedir_columna_numerica(
            "Variable Y"
        )

        if not variable_y:
            return

        datos_grafico = datos[
            [variable_x, variable_y]
        ].dropna()

        plt.figure(figsize=(8, 5))

        plt.scatter(
            datos_grafico[variable_x],
            datos_grafico[variable_y],
            alpha=0.6
        )

        plt.title(
            variable_x + " vs " + variable_y
        )

        plt.xlabel(variable_x)
        plt.ylabel(variable_y)

        plt.grid(alpha=0.3)

        plt.ticklabel_format(
            style="plain"
        )

        plt.tight_layout()
        plt.show()

    # *** crea un diagrama de caja / creates a box plot ***
    def boxplot():
        campo = pedir_columna_numerica(
            "Boxplot"
        )

        if campo:
            datos_grafico = datos[campo].dropna()

            plt.figure(figsize=(7, 5))

            plt.boxplot(
                datos_grafico,
                vert=True
            )

            plt.title(
                "Boxplot de " + campo
            )

            plt.ylabel(campo)

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

    lista_opciones = [
        ("1. Gráfico de barras", barras),
        ("2. Histograma", histograma),
        ("3. Gráfico de líneas", linea),
        ("4. Gráfico de dispersión", dispersion),
        ("5. Boxplot", boxplot),
        ("6. Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones, 36)

# *** análisis adicional / additional analysis ***
# *** abre las opciones de análisis adicional / opens the additional analysis options ***
def ventana_adicional():
    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Análisis adicional",
        "350x350"
    )

    # *** calcula la matriz de correlaciones / calculates the correlation matrix ***
    def matriz():
        campos_numericos = datos.select_dtypes(
            include="number"
        )

        if campos_numericos.shape[1] < 2:
            messagebox.showwarning(
                "Advertencia",
                "No hay suficientes variables numéricas."
            )
            return

        mostrar_texto(
            campos_numericos.corr().round(2).to_string()
        )

    # *** cuenta los valores únicos por columna / counts unique values by column ***
    def unicos():
        mostrar_texto(
            "valores únicos por columna\n\n"
            + datos.nunique().to_string()
        )

    # *** muestra un resumen del análisis / displays an analysis summary ***
    def resumen():
        mostrar_texto(
            "****** resumen general ******\n\n"
            f"filas: {datos.shape[0]}\n"
            f"columnas: {datos.shape[1]}\n"
            f"valores nulos: {datos.isnull().sum().sum()}\n"
            f"duplicados: {datos.duplicated().sum()}\n"
        )

    lista_opciones = [
        ("Matriz de correlaciones", matriz),
        ("Valores únicos", unicos),
        ("Resumen general", resumen),
        ("Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones)

# *** ingreso de datos y readme / data entry and readme ***
# *** abre las opciones de ingreso de datos y readme / opens the data entry and readme options ***
def ventana_ingreso():
    global datos
    global nuevos_registros

    if not verificar_df():
        return

    ventana_actual = crear_ventana(
        "Ingreso de datos",
        "450x450"
    )

    # *** captura un nuevo registro / captures a new record ***
    def nuevo_registro():
        registro_actual = {}

        for campo in datos.columns:
            dato = simpledialog.askstring(
                "Nuevo registro",
                campo + ":"
            )

            registro_actual[campo] = dato

        nuevos_registros.append(
            registro_actual
        )

        messagebox.showinfo(
            "Correcto",
            "Registro agregado."
        )

    # *** muestra los nuevos registros ingresados / displays the newly entered records ***
    def mostrar_nuevos():
        if not nuevos_registros:
            mostrar_texto(
                "No existen registros nuevos."
            )
            return

        mostrar_texto(
            pd.DataFrame(
                nuevos_registros
            ).to_string()
        )

    # *** guarda los nuevos datos en un archivo csv / saves the new data to a csv file ***
    def guardar():
        global datos
        global nuevos_registros

        if not nuevos_registros:
            messagebox.showwarning(
                "Advertencia",
                "No hay registros para guardar."
            )
            return

        tabla_nuevos = pd.DataFrame(
            nuevos_registros
        )

        datos = pd.concat(
            [datos, tabla_nuevos],
            ignore_index=True
        )

        ruta_archivo = filedialog.asksaveasfilename(
            title="Guardar archivo",
            defaultextension=".csv",
            filetypes=[("Archivo CSV", "*.csv")]
        )

        if ruta_archivo:
            datos.to_csv(
                ruta_archivo,
                index=False
            )

            nuevos_registros.clear()

            messagebox.showinfo(
                "Correcto",
                "Datos guardados correctamente."
            )

    # *** crea un archivo readme con información del proyecto / creates a readme file with project information ***
    def crear_readme():
        ruta_archivo = filedialog.asksaveasfilename(
            title="Guardar README",
            defaultextension=".txt",
            filetypes=[("Archivo de texto", "*.txt")]
        )

        if not ruta_archivo:
            return

        try:
            with open(
                ruta_archivo,
                "w",
                encoding="utf-8"
            ) as archivo_readme:

                archivo_readme.write(
                    "Proyecto Final - Manejo de datos – EDA\n"
                )

                archivo_readme.write(
                    "Módulo: Manejo de datos - EDA\n"
                )

                archivo_readme.write(
                    "Estudiante: Marilyn Miranda Jaen\n\n"
                )

                archivo_readme.write(
                    "Descripción\n"
                    "programa desarrollado en python para "
                    "cargar, explorar, analizar e interpretar "
                    "datos de un archivo csv.\n\n"
                )

                archivo_readme.write(
                    "Estructura del dataset\n"
                )

                archivo_readme.write(
                    f"Filas: {datos.shape[0]}\n"
                    f"Columnas: {datos.shape[1]}\n\n"
                )

                archivo_readme.write(
                    "Columnas y tipos de datos\n"
                )

                for campo in datos.columns:
                    archivo_readme.write(
                        f"- {campo}: "
                        f"{datos[campo].dtype}\n"
                    )

                archivo_readme.write(
                    "\nFunciones del programa\n"
                    "1. Cargar archivo csv\n"
                    "2. Información del dataset\n"
                    "3. Primeras y últimas filas\n"
                    "4. Tipos de datos\n"
                    "5. Valores nulos\n"
                    "6. Datos duplicados\n"
                    "7. Estadísticas descriptivas\n"
                    "8. Filtros\n"
                    "9. Agrupaciones\n"
                    "10. Representaciones gráficas\n"
                    "11. Análisis adicional\n"
                    "12. Ingreso de datos\n"
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

    lista_opciones = [
        ("Ingresar nuevo registro", nuevo_registro),
        ("Mostrar registros ingresados", mostrar_nuevos),
        ("Guardar nuevos datos", guardar),
        ("Crear archivo README", crear_readme),
        ("Cerrar", ventana_actual.destroy)
    ]

    crear_botones(ventana_actual, lista_opciones)

# *** ventana principal / main window ***
ventana_principal = tk.Tk()

ventana_principal.title(
    "Proyecto Final - Marilyn Miranda Jaen"
)

ventana_principal.geometry(
    "1250x720"
)

ventana_principal.minsize(
    1100,
    650
)

# *** título principal / main title ***
encabezado = tk.Label(
    ventana_principal,
    text="Manejo de Datos – EDA",
    font=("Arial", 18, "bold")
)

encabezado.pack(
    pady=(15, 10)
)

# *** contenedor general / main container ***
contenedor_general = tk.Frame(
    ventana_principal
)

contenedor_general.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)

# *** menú del panel izquierdo / left panel menu ***
panel_menu = tk.LabelFrame(
    contenedor_general,
    text=" Menú Principal ",
    font=("Arial", 11, "bold"),
    padx=12,
    pady=10,
    labelanchor="n"
)

panel_menu.pack(
    side="left",
    fill="y",
    padx=(0, 15)
)

# *** botones principales / main buttons ***
botones_menu = [
    ("1. Cargar CSV", cargar_csv),
    ("2. Información del conjunto de datos", informacion_dataset),
    ("3. Primeras y últimas filas", primeras_ultimas),
    ("4. Analizar tipos de datos", ventana_tipos),
    ("5. Analizar valores nulos", ventana_nulos),
    ("6. Analizar datos duplicados", ventana_duplicados),
    ("7. Estadísticas descriptivas", ventana_estadisticas),
    ("8. Filtrar o consultar datos", ventana_filtros),
    ("9. Agrupaciones y operaciones", ventana_agrupaciones),
    ("10. Representaciones gráficas", ventana_graficos),
    ("11. Análisis adicional", ventana_adicional),
    ("12. Ingreso de datos / README", ventana_ingreso)
]

for contenido, accion in botones_menu:
    tk.Button(
        panel_menu,
        text=contenido,
        width=34,
        height=1,
        font=("Arial", 10, "bold"),
        anchor="center",
        command=accion
    ).pack(
        fill="x",
        pady=3
    )

# *** botón salir / exit button ***
tk.Button(
    panel_menu,
    text="13. Salir",
    width=34,
    height=1,
    font=("Arial", 10, "bold"),
    command=ventana_principal.destroy
).pack(
    fill="x",
    pady=(10, 3)
)

# *** resultados del panel derecho / right panel results ***
panel_resultados = tk.LabelFrame(
    contenedor_general,
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

marco_texto = tk.Frame(
    panel_resultados
)

marco_texto.pack(
    fill="both",
    expand=True
)

barra_vertical = tk.Scrollbar(
    marco_texto
)

barra_vertical.pack(
    side="right",
    fill="y"
)

barra_horizontal = tk.Scrollbar(
    marco_texto,
    orient="horizontal"
)

barra_horizontal.pack(
    side="bottom",
    fill="x"
)

area_resultados = tk.Text(
    marco_texto,
    wrap="none",
    font=("Consolas", 10),
    yscrollcommand=barra_vertical.set,
    xscrollcommand=barra_horizontal.set
)

area_resultados.pack(
    fill="both",
    expand=True
)

barra_vertical.config(
    command=area_resultados.yview
)

barra_horizontal.config(
    command=area_resultados.xview
)

# *** inicia la interfaz / starts the interface ***
ventana_principal.mainloop()
