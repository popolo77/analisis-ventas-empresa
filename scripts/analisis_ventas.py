
# Script de análisis de ventas

# Importación de librerías
import pandas as pd
import matplotlib.pyplot as plt

# Lectura del dataset
df = pd.read_csv("datos/ventas.csv")

# Cálculo del total vendido por operación
df["total"] = df["cantidad"] * df["precio"]

# Cálculo de ventas totales
ventas_totales = df["total"].sum()

print("Ventas totales:", ventas_totales)

# Producto más vendido
producto_mas_vendido = df.groupby("producto")["cantidad"].sum()

print(producto_mas_vendido)

# Conversión de fecha
df["fecha"] = pd.to_datetime(df["fecha"])

# Extracción del mes
df["mes"] = df["fecha"].dt.month

# Ventas agrupadas por mes
ventas_por_mes = df.groupby("mes")["total"].sum()

print(ventas_por_mes)

# Generación del gráfico
ventas_por_mes.plot(kind="bar")

plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Total Vendido")

# Guardado del gráfico
plt.savefig("resultados/grafico_ventas.png")

plt.show()
