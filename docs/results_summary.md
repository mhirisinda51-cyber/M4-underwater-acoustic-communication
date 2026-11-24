\# Resultados preliminares



\## 1. Pérdida de transmisión



El modelo estima la pérdida de transmisión acústica submarina mediante la propagación esférica (con un factor de propagación de 20) y la absorción de Thorp. La pérdida aumenta con la distancia y la frecuencia. Por tanto, bajo las hipótesis actuales del modelo, las frecuencias más altas tienen un alcance de comunicación útil menor.



\## 2. Relación señal-ruido (SNR)



El primer modelo de SNR utiliza un nivel de fuente supuesto de 190 dB y un nivel de ruido de 60 dB. Estos valores son ilustrativos y no corresponden a mediciones ni a las especificaciones de un módem acústico concreto.



La SNR estimada disminuye al aumentar la distancia y la frecuencia. A 10 km, el modelo actual estima aproximadamente 46,18 dB a 5 kHz, 38,13 dB a 10 kHz, 8,66 dB a 20 kHz y −32,80 dB a 30 kHz.

\## 3. Capacidad teórica



El modelo de capacidad de Shannon utiliza un ancho de banda provisional de 1.000 Hz. Los resultados representan límites teóricos, no velocidades de transmisión garantizadas para un módem real.



La capacidad teórica estimada disminuye al aumentar la distancia y la frecuencia. A 10 km, el modelo obtiene aproximadamente 15,34 kbps a 5 kHz, 12,67 kbps a 10 kHz y 3,06 kbps a 20 kHz. Estos valores se calculan con un ancho de banda supuesto de 1 kHz y no representan velocidades garantizadas de un módem real.



!\[Capacidad teórica estimada en función de la distancia](capacity\_vs\_distance.png)

\## 4. Retardo de propagación



Suponiendo una velocidad del sonido de 1.500 m/s, el retardo de propagación estimado en un solo sentido es de aproximadamente 0,67 segundos por kilómetro. Esto corresponde a unos 3,33 segundos a 5 km y 6,67 segundos a 10 km, sin incluir los retardos de procesamiento ni los del protocolo de comunicación.



\## 5. Limitaciones y próximos pasos



Estos son resultados preliminares basados en hipótesis simplificadas. Antes de extraer conclusiones definitivas, es necesario revisar el nivel de fuente, el modelo de ruido, el ancho de banda, el modelo de propagación y las limitaciones de los módems reales.



El siguiente paso consiste en comparar el modelo con las especificaciones publicadas de módems acústicos comerciales, utilizando condiciones de funcionamiento comparables.

