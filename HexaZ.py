
import sys, os
import threading
from datetime import datetime

pause = lambda: os.system('Pause > NUL')

def estimateTotal(l_str, lenght):
	val = 0
	for x in range(1,lenght+1):
		val += (l_str ** x)
	return val

def estimateBytesTotal(estimate, l_str, lenght):
	# val = Cantidad de bytes generados por los saltos de linea.
	# Son 2 bytes por salto, porque son 2 caracteres: \n
	val = estimate*2
	for x in range(1,lenght+1):
		val += ((l_str ** x)*x)
	return val

def getSizeFile(total_bytes):
	total = 0
	_type = 'Bytes'
	if total_bytes > (1024**3):
		total = total_bytes / (1024**3)
		_type = 'Gb'
	elif total_bytes > (1024**2):
		total = total_bytes / (1024**2)
		_type = 'Mb'
	elif total_bytes > 1024:
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
			val += '.'
		cont += 1
	return val[::-1]
	

def getPorcent():
	porcent = (cont / estimate) * 100
	return porcent

def piramidData(s, c):
	
	global cont, sec
	
	for l in s:
		
		l = c+l
		cont += 1
		fil.write(l+'\n')
		
		if not len(l) == longy:
			piramidData(s, l)
	
	sec_n = int(datetime.now().strftime('%S'))
	
	if sec_n > sec or (sec_n == 0 and not sec == 0):
		sec = sec_n
		sys.stdout.write('\r Total: {:.2f}%    '.format(getPorcent()))
	


if __name__ == '__main__':
	
	ver = 'v1.0.1'
	sec = 0
	string = '0123456789ABCDEF'
	longy = 8	# Modificar por la cantidad que se desee.
	cont = 0
	estimate = estimateTotal(len(string), longy)
	total_bytes = estimateBytesTotal(estimate, len(string), longy)
	espacio, tipo = getSizeFile(total_bytes)
	
	print('\n\n Generador de Diccionario Hexadecimal. {}'.format(ver))
	print('\n Total Estimado de Cadenas: {}'.format(normalizeNumber(estimate)))
	print('\n Peso Exacto de Salida: ''{:.3f} {} ({} bytes)\n\n\n'.format(
									espacio, tipo, normalizeNumber(total_bytes)))
	
	fil = open('hex_len-{}.zion'.format(longy),'w')
	piramidData(string, '')
	sys.stdout.write('\r Porcentaje Total: {:.2f}%    '.format(getPorcent()))
	print('\n\n Total de Cadenas Generado: {}    '.format(normalizeNumber(cont)))

	fil.close()
	


