 #Ingresar cuenta()
 # Importacion de Librerias
# -*- coding: utf-8 -*-
#!/usr/bin/env python
import time
import os
import sys
import sqlite3
import getpass
 
#declaracion de variables
 
usuariosRegistrados = ('KathyDally','KimCol','GuestUser')
passRegistradas = ('code2016')
 
#declaracion de funciones
def login(usuario,contraseña):
    if usuario in usuariosRegistrados:
        if contraseña in passRegistradas:
            return 1
        else:
            print("\n\tCONTRASEÑA NO COINCIDE...\n")
    else:
        return 2
 
 #inicializacion de procesos
usuario=input('Usuario: ')
contraseña = getpass.getpass('Contraseña: ')
 
if login(usuario,contraseña)==1:
    print('BIENVENIDO ',usuario)
else:
    print('ERROR! USUARIO NO REGISTRADO.')

#Cerrar sesión()

#Recuperar contraseña()

