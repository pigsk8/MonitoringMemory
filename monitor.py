#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
import sys
import psutil

if len(sys.argv) < 2:
	print "Necesita Prametros"
	print "Ejemplo: -s 20"
else:
	comando=sys.argv[1]
 	tiempo=sys.argv[2]
	if comando!='-s' and comando!='-segundos' and comando!='--segundos':
		print "Comando no permitido"
  	else:	
  		#print "Comando es "+comando
		#tiempo de ejecución
		print "Tiempo de ejecución: "+tiempo+"sg"
		
		#Memoria Total
		mem=psutil.virtual_memory().total
		float(mem)
		mem=mem/1048576
		print "Total de memoria del equipo: ",mem,"MB"

		#Picos Mayor y Menor
		mayor=-1
		menor=99999999999
		tiempouso=0
		tiempoeje = int(tiempo)
		tiempoeje = tiempoeje*2
		#print tiempoeje
		while (tiempouso < tiempoeje):
			
			auxmayor = psutil.virtual_memory().used
			float(auxmayor)
			auxmayor=auxmayor/1048576
			if auxmayor > mayor:
				mayor=auxmayor
			#print "Mayor: ",mayor			

			auxmenor = psutil.virtual_memory().used
			float(auxmenor)
			auxmenor=auxmenor/1048576
			if auxmenor < menor:
				menor=auxmenor
			#print "menor: ",menor


			#print tiempouso
			time.sleep(0.5)
			tiempouso=tiempouso+1
		
		print "Mayor pico de memoria detectado: ",mayor,"MB"
		print "Menor pico de memoria detectado: ",menor, "MB"

		#cantidad de procesos
		proces = psutil.pids()
		cantproc = len(proces)
		print "Cantidad de procesos: ", cantproc

		#Promedio general por proceso
		prom = ((mayor+menor)/2)/cantproc
		print "Promedio general de memoria por proceso: ", prom,"MB"


print "Elaborado por:"
print "Leonard Mendoza y Juan Scrocchi"
time.sleep(2)
