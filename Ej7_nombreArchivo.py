# Obtner la extencion de un archivo especificado por el usuario.

nombre_archivo = input('Ingrrese el nombre del archivo: ')

extencion = nombre_archivo.split('.')

print(extencion)

print('la extencion es: ',extencion[-1])
