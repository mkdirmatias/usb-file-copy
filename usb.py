#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
import os
import funciones

#
# Carpeta donde se montan los discos
# Linux -> /media
# MAC -> /Volumes
#
carpeta = "/Volumes"


#
# Copiar todo el usb o solo los archivos permitidos
# 1 -> todo
# 2 -> archivos permitidos
#
metodo = 2


#
# Archivos Permitidos a copiar
#
permitidos = ['pdf','xls','doc','ppt','txt','jpg','png']


#
# Guardamos los usb montados
#
guardados = funciones.usb(carpeta)


#
# Carpeta donde se guardarán los archivos
#
destino = '/Users/unkndown'


#
# Verificamos si hay nuevos usb
#
while 1:
    nuevos = funciones.usb(carpeta)
    for new in nuevos:
        ruta = carpeta+new
        if new not in guardados:
            destino = destino+new
            comando = "mkdir -p %s" % destino
            os.system(comando)
            if(metodo == 1):
                funciones.copiar_archivos(ruta,destino,permitidos)
            else:
                funciones.copiar_todo(ruta,destino,permitidos)
    guardados = nuevos
    time.sleep(1)
