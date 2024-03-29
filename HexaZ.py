
# HexaZ.py
# Version: v1.0.4
# Python 3

from datetime import datetime
from time import time
import sys, os

pause = lambda: os.system('pause > nul')

def estimateTotal(l_str, lenght):
	val = 0
	if _type == 'pyramid':
		for x in range(1,lenght+1):
			val += (l_str ** x)
	elif _type == 'exact':
		val = (l_str ** lenght)
	return val

def estimateBytesTotal(estimate, l_str, lenght):
	val = 0
	if _type == 'pyramid':
		# Cantidad de bytes generados por los saltos de linea.
		# Son 2 bytes por salto, porque son 2 caracteres: \n
		val = estimate*2
		for x in range(1,lenght+1):
			val += ((l_str ** x) * x)
	elif _type == 'exact':
		val = (estimate*2) + (estimate*lenght)
	return val

def getSizeFile(total_bytes):
	total = total_bytes
	_type = 'Bytes'
	if total_bytes >= (1024**4):
		total = total_bytes / (1024**4)
		_type = 'Tb'
	elif total_bytes >= (1024**3):
		total = total_bytes / (1024**3)
		_type = 'Gb'
	elif total_bytes >= (1024**2):
		total = total_bytes / (1024**2)
		_type = 'Mb'
	elif total_bytes >=1024:
		total = total_bytes / 1024
		_type = 'Kb'
	return total, _type

def normalizeNumber(number):
	total = str(number)[::-1]
	val = ''
	cont = 1
	for n in total:
		val += n
		if cont % 3 == 0 and not cont == len(total):
			val += ','
		cont += 1
	return val[::-1]
	
def getPorcent():
	porcent = (cont / estimate) * 100
	return porcent

def write(cad):
	global cont
	cont += 1
	fil.write(cad+'\n')

def showPorcent():
	global sec
	sec_n = int(datetime.now().strftime('%S'))
	if sec_n > sec or (sec_n == 0 and not sec == 0):
		sec = sec_n
		sys.stdout.write('\r Total: {:.2f}%    \t {} segs   '.format(
							getPorcent(), int(time()-tiempo_inicial)))



def pyramidData(string, prefijo):
	for c in string:
		cadena = prefijo+c
		write(cadena)
		if not len(cadena) == longy:
			pyramidData(string, cadena)
	showPorcent()
	

def exactData(string, prefijo):
	for c in string:
		cadena = prefijo+c
		if len(cadena) == longy:
			write(cadena)
		else:
			exactData(string, cadena)
	showPorcent()



__version__ = 'v1.0.4'
__author__ = 'LawlietJH'



if __name__ == '__main__':
	
	ver = 'v1.0.4'
	_type = 'exact'		# ['pyramid', 'exact']
	longy = 5			# Modificar por la cantidad que se desee. 1 a 8
	
	STRING = '0123456789ABCDEF'
	sec = 0
	cont = 0
	
	estimate = estimateTotal(len(STRING), longy)
	total_bytes = estimateBytesTotal(estimate, len(STRING), longy)
	espacio, tipo = getSizeFile(total_bytes)
	
	print('\n\n Generador de Diccionario Hexadecimal. {}'.format(ver))
	print('\n Longitud: {}'.format(longy))
	print('\n Tipo: {} ({})'.format(_type, 'De Longitud Exacta Deseada' 
											if _type == 'exact' else 
											'De Longitud 1 a Cantidad Deseada'))
	print('\n Total Estimado de Cadenas: {}'.format(normalizeNumber(estimate)))
	if tipo == 'Bytes':
		print('\n Peso Exacto de Salida: ''{} {} ({} bytes)\n\n\n'.format(
									espacio, tipo, normalizeNumber(total_bytes)))
	else:
		print('\n Peso Exacto de Salida: ''{:.3f} {} ({} bytes)\n\n\n'.format(
									espacio, tipo, normalizeNumber(total_bytes)))
	
	fil = open('hexaz - len_{}-{}.zion'.format(longy, _type.title()),'w')
	
	tiempo_inicial = time()
	
	if _type == 'pyramid': pyramidData(STRING, '')
	elif _type == 'exact': exactData(STRING, '')
	
	tiempo_final = time() 
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	
	fil.close()
	
	sys.stdout.write('\r Porcentaje Total: {:.2f}%        '.format(getPorcent()))
	print('\n\n Total de Cadenas Generadas: {}    '.format(normalizeNumber(cont)))
	print('\n\n Tiempo transcurrido: {} segundos'.format(int(tiempo_ejecucion)))

	


