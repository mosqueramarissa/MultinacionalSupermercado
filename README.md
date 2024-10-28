# MultinacionalSupermercado

# Análisis de Viabilidad - Nueva Sucursal Walmart Juriquilla

## Descripción del Proyecto
Este proyecto realiza un análisis estadístico completo para evaluar la viabilidad de abrir una nueva sucursal de Walmart en Juriquilla, una comunidad con aproximadamente 40,000 habitantes. El análisis incluye estimaciones de ventas, cálculos de gastos operativos, análisis poblacional y proyecciones de satisfacción del cliente.

## Objetivos
- Determinar el número necesario de ventas para alcanzar una ganancia mensual de $1,500,000 MXN
- Estimar el porcentaje de la población que necesitamos como clientes
- Analizar y proyectar niveles de satisfacción del cliente
- Calcular gastos operativos detallados
- Proporcionar recomendaciones basadas en datos


## Metodología
1. **Análisis de Ventas**
   - Normalización de datos históricos
   - Ajuste a distribución Beta
   - Estimación de parámetros por máxima verosimilitud

2. **Análisis de Gastos**
   - Cálculo de nómina para diferentes roles
   - Estimación de gastos operativos
   - Proyección de gastos de servicios

3. **Análisis Poblacional**
   - Estimación de frecuencia de compras
   - Cálculo de base de clientes necesaria

4. **Análisis de Satisfacción**
   - Distribución de ratings
   - Proyecciones usando Teorema del Límite Central

## Dentro del Código
```python
# Ejecutar el análisis completo
python MultinacionalSuper.py

# Los resultados incluirán:
- Parámetros de la distribución de ventas
- Número necesario de ventas mensuales
- Porcentaje de población objetivo
- Probabilidades de ratings altos
```

## Variables Principales
```python
# Datos de entrada
población_total = 40,000
ganancia_objetivo = 1,500,000 MXN
nivel_confianza = 99%

# Personal requerido
cajeros = 30
almacenistas = 40
personal_piso = 60
conserjes = 20
gerentes = 1
subgerentes = 4
```

## Resultados Clave
- Número de ventas mensuales necesarias
- Gastos operativos totales
- Porcentaje de población necesaria como clientes
- Probabilidad de mantener ratings altos

## Consideraciones y Mejoras Futuras
1. **Gastos Adicionales**
   - Consumo de agua
   - Variaciones en consumo eléctrico
   - Gastos de mantenimiento

2. **Patrones de Compra**
   - Variaciones estacionales
   - Días y horas pico
   - Comportamiento por segmento demográfico

3. **Personal**
   - Rotación de turnos
   - Personal temporal
   - Capacitación

## Visualizaciones Disponibles
- Distribución de ventas
- Proyecciones de gastos
- Análisis de ratings
- Tendencias temporales


## Consideraciones
- Los datos de ventas están en pesos mexicanos
- Se asume una compra semanal por cliente
- Los cálculos incluyen un margen de seguridad del 15% en salarios

## Referencias
- Datos salariales: glassdoor.com.mx
- Tabla de salarios mínimos: gob.mx
- Tarifas CFE: cfe.mx
