## Descripción
Clona un dispositivo usb con Raspberry y python.
El script se ejecuta al prender la Raspberry, verifica cada 1 segundo si se ha montado un nuevo dispositivo según la carpeta definida por cada S.O y copia todos los archivos del USB en la carpeta de destino especificada.

# Uso
Seguir las siguientes instrucciones para un correcto funcionamiento.

## Carpeta Discos
Definir la carpeta donde se montan los discos:

 1. **Linux:** /media
 2. **MAC:** /Volumes

Para eso, editamos la siguiente linea del script (variable **carpeta**)

    carpeta = "/media"
    
## Metodo de copiado
Podemos seleccionar entre clonar todo el dispositivo, siguiendo la misma estructura de carpeta, o copiar solo los archivos específicos.

 - **1:**  Clonar todo
 - **2:**  Copiar archivos específicos
 
Para esto especificamos nuestra opción en la linea:

    metodo = 2

## Archivos a copiar
Podemos definir que tipos de archivos queremos copiar, esto se tomará en cuenta siempre y cuando se haya seleccionado el método de copiado 2. Para ello editamos la siguiente linea:

    permitidos = ['pdf','xls','doc','ppt','txt','jpg','png']

## Carpeta de destino
Aquí seleccionamos la carpeta de destino, en la cual queremos que los archivos copiados queden guardados:

    destino = '/Users/unkndown'
