import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import beta, norm
import matplotlib.pyplot as plt

# Lectura y procesamiento inicial de datos
df = pd.read_csv('SuperMarketData.csv')
sales = np.array(df["Sales"]) * 19.88  # Conversión de dólares a pesos
max_sales = np.max(sales)
min_sales = np.min(sales)
sales_norm = 1/(max_sales-min_sales) * (sales - min_sales)  # Corrección en la normalización

# Estimación de parámetros de la distribución beta
a, b, _, _ = beta.fit(sales_norm)  # Ajuste de la distribución beta

# Cálculo de estadísticas para datos normalizados
mu_norm = a/(a+b)  # Media normalizada
var_norm = (a*b)/((a+b)**2*(a+b+1))  # Varianza normalizada
std_norm = np.sqrt(var_norm)  # Desviación estándar normalizada

# Desnormalización de estadísticas
mu = (max_sales-min_sales)*mu_norm + min_sales  # Media real
var = (max_sales-min_sales)**2 * var_norm
sigma = np.sqrt(var)

# Cálculo de gastos operativos
dias_trab = 24
fact = 1.15  # Factor de incremento salarial (15%)

# Cálculo de nómina por categoría
sal_cajeros = 258.25
num_cajeros = 30
tot_sal_cajeros = sal_cajeros * num_cajeros * dias_trab * fact

sal_conserjes = 5000
num_conserjes = 20
tot_sal_conserjes = sal_conserjes * num_conserjes * fact

tot_sal_gerente = 100000

sub_gerente = 45000
num_sub_gerente = 4
tot_sal_sub_gerente = sub_gerente * num_sub_gerente

sal_almacenista = 262.13
almacenista = 40
tot_sal_almacenista = sal_almacenista * almacenista * dias_trab * fact

g_pasillo = 264.65
num_pasillo = 40
tot_sal_pasillo = g_pasillo * num_pasillo * dias_trab * fact

# Total nómina
nomina_total = (tot_sal_cajeros + tot_sal_conserjes + tot_sal_gerente + 
                tot_sal_sub_gerente + tot_sal_almacenista + tot_sal_pasillo)

# Gastos de luz
gasto_luz = 120 * 2000 * 12 * 2.3 * 30
gastos_tot = gasto_luz + nomina_total

# Cálculo del número de ventas necesarias
omega = norm.ppf(0.01)  # Valor crítico para 99% de confianza
ingreso = gastos_tot + 1500000  # Gastos totales más ganancia deseada

# Coeficientes para la ecuación cuadrática
a_ = mu**2
b_ = -2*mu*ingreso - omega*2*sigma**2
c_ = ingreso**2

# Resolución de la ecuación cuadrática
N1 = (-b_ + np.sqrt(b_**2 - 4*a_*c_))/(2*a_)
N2 = (-b_ - np.sqrt(b_**2 - 4*a_*c_))/(2*a_)
N = max(N1, N2)

# Análisis de población y porcentaje necesario
poblacion_total = 40000
compras_por_semana = 1
semanas_por_mes = 4

# Cálculo del número de personas necesarias
personas_necesarias = N / (compras_por_semana * semanas_por_mes)
porcentaje_poblacion = (personas_necesarias / poblacion_total) * 100

# Análisis de ratings (asumiendo que están en el DataFrame)
ratings = np.array(df['Rating'])
rating_mean = np.mean(ratings)
rating_std = np.std(ratings)

# Probabilidad de rating >= 8.5 usando Teorema del Límite Central
z_score = (8.5 - rating_mean) / (rating_std / np.sqrt(30))  # Asumiendo n=30 para TCL
prob_rating_alto = 1 - norm.cdf(z_score)

# Impresión de resultados
print(f'''\n=== Resultados del Análisis ===
\nPasos 1-4: Análisis de Ventas y Gastos
Parámetros de la distribución beta: α = {a:.2f}, β = {b:.2f}
Media de ventas: ${mu:,.2f}
Desviación estándar de ventas: ${sigma:,.2f}
Gastos totales mensuales: ${gastos_tot:,.2f}
Número de ventas necesarias mensuales: {N:.0f}''')

print(f'''\nPaso 5: Análisis de Población
Personas necesarias por mes: {personas_necesarias:.0f}
Porcentaje de la población a convencer: {porcentaje_poblacion:.1f}%''')

print(f'''\nPasos 6-8: Análisis de Ratings
Media de ratings: {rating_mean:.2f}
Desviación estándar de ratings: {rating_std:.2f}
Probabilidad de rating ≥ 8.5: {prob_rating_alto:.2%}''')

print(''' \nPuntos de Mejora Sugeridos:
      1. Revisar el cálculo de consumo eléctrico con datos actualizados de CFE
      2. Incluir gastos de agua y otros servicios
      3. Considerar variaciones en frecuencia de compra por temporada
      4. Evaluar necesidad de personal adicional en horas pico''')
