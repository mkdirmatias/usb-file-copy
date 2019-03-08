#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import commands
import os
import shutil

#
# Verificamos si hay un usb nuevo montado
#
def usb(carpeta):
    guardados = []
    comando   = "df -h | grep %s" % carpeta
    discos    = commands.getstatusoutput(comando)
    discos    = discos[1].split("/dev")

    for disco in discos:
        nombre = disco.split(carpeta)
        if nombre[0] != '':
            guardados.append(nombre[1])

    return guardados


#
# Copiar archivos permitidos encontrados en el usb
#
def copiar_archivos(path,destino,permitidos):
    for path, dirs, files in os.walk(path):
        for filename in files:
            full_file_name = os.path.join(path, filename)
            if '.' in full_file_name:
                extension = full_file_name.split('.')[1]
                if extension in permitidos:
                    try:
                        shutil.copy2(full_file_name, destino)
                    except IOError:
                        pass


#
# Copiar todo el pendrive, siguiendo la estrucutra de carpetas
#
def copiar_todo(path,destino):
    shutil.copytree(path, destino,symlinks=False, ignore=None)
