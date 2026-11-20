# M4 – Comunicación acústica submarina para AUV y ROV

## 1. Introducción

La comunicación bajo el agua es uno de los retos que encontramos al trabajar con vehículos submarinos autónomos (AUV) y vehículos operados remotamente (ROV). A diferencia de las comunicaciones habituales por radio, bajo el agua se utilizan principalmente ondas acústicas. Su funcionamiento depende de factores como la distancia, la frecuencia y el ruido del entorno.

En este proyecto se estudiará cómo se comporta la comunicación acústica submarina mediante un modelo desarrollado en Python. El objetivo es analizar sus principales limitaciones y conocer qué prestaciones se pueden conseguir en diferentes condiciones.

## 2. Objetivos

El trabajo se centrará en los siguientes aspectos:

- Estudiar la absorción acústica del agua utilizando la fórmula de Thorp.
- Analizar las pérdidas de propagación según la distancia y la frecuencia.
- Modelar el ruido ambiente y calcular la relación señal-ruido (SNR).
- Estimar la capacidad del canal mediante la fórmula de Shannon.
- Comparar diferentes técnicas de modulación.
- Analizar la relación entre el alcance y la tasa de datos.
- Calcular la latencia de propagación de las señales acústicas.
- Comparar los resultados con las especificaciones de módems acústicos comerciales.

## 3. Metodología

Primero se estudiará el comportamiento de la absorción acústica en función de la frecuencia. Después se desarrollará un modelo de propagación para diferentes distancias y se tendrán en cuenta los efectos del ruido ambiente.

A partir de estos resultados se calculará la SNR y se estimará la capacidad teórica del canal. Finalmente, se compararán diferentes técnicas de modulación y se analizará cómo varía el alcance en función de la tasa de transmisión.

Los resultados se representarán mediante gráficas y se contrastarán con las especificaciones técnicas de equipos comerciales.

## 4. Herramientas

- Python
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook
- Git y GitHub

## 5. Organización del repositorio

- `data/`: datos y parámetros utilizados en el modelo.
- `src/`: código Python del proyecto.
- `notebooks/`: pruebas, cálculos y análisis.
- `docs/`: documentación, referencias y memoria final.

## 6. Resultados esperados

Se espera obtener un modelo que permita estudiar las prestaciones de una comunicación acústica submarina para diferentes distancias y frecuencias.

También se elaborarán gráficas para visualizar las pérdidas de propagación, la relación señal-ruido y la tasa de datos alcanzable. A partir de los resultados se identificarán las condiciones de comunicación más adecuadas para diferentes aplicaciones con AUV y ROV.

## 7. Estado del proyecto

Proyecto en desarrollo.

## 8. Referencias iniciales

- Zia, M. Y. I., Poncela, J. y Otero, P. (2021). *State-of-the-art underwater acoustic communication modems: Classifications, analyses and design challenges*. Wireless Personal Communications, 116, 1325–1360. https://doi.org/10.1007/s11277-020-07431-x

- Stojanovic, M. (2006). *On the relationship between capacity and distance in an underwater acoustic communication channel*. Proceedings of WUWNet '06. https://doi.org/10.1145/1161039.1161049

---

**Máster en Vehículos Autónomos (MuVA)**  
Proyecto individual – M4
