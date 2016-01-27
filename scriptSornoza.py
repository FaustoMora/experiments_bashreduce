#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys
from datetime import datetime

i = 0
salto = '\n'
contador = -1
tiempo_total_procesar = datetime.now() - datetime.now()
tiempo_total_contar = datetime.now() - datetime.now()
tiempo_total = datetime.now() - datetime.now()

globalinicio = datetime.now()
for line in sys.stdin:
	
	inicio = datetime.now()
	n1 = re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚ]',r' ',line) #Elimino los caracteres que no sean alfabeticos.
	n2 = re.sub(r'[\t\n\r\f]',r' ',n1) #Elimino los tab, retornos, saltos y similares.
	n3 = re.sub(r'[ ]+',' ', n2) #Elimino los espacios multiples.
	fin = datetime.now()
	tiempo_total_procesar = fin - inicio + tiempo_total_procesar
	if n3.strip(): #Si es el fin de una linea entro.
		i = i + 1 #Contador de iteracion, habra tantos iteradores como trabajos definidos por br.
		inicio = datetime.now()
		for palabra in n3.split(' '):
			contador+=1
		fin = datetime.now()
		tiempo_total_contar = fin - inicio + tiempo_total_contar
		print 'Recorrido ' +  str(i) + ':'+ salto  + n3 + salto
		print ('Tiempo que tomo procesar esta linea: {}'.format(fin - inicio)+salto)
globalfin = datetime.now()
tiempo_total = globalfin - globalinicio + tiempo_total

print salto + 'Palabras totales contadas en el archivo:' + str(contador) + salto
print ('Tiempo que tomo contar todas las palabras: {}'.format(tiempo_total_contar)+salto)
print ('Tiempo que tomo procesar todas las lineas: {}'.format(tiempo_total_procesar)+salto)
print ('Tiempo total de ejecucion: {}'.format(tiempo_total)+salto)



