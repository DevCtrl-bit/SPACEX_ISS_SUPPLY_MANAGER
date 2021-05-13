#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 04:04:28 2021

@author: diegotellez
"""
import time
import menu

def errorComun(textoError):
    print(chr(1421)*30)
    print("\nERROR: ", textoError)
    print("\nPor favor vuelva a intentarlo\n")
    print("Los cambios introducidos no se han guardado.\n")
    print("Será redirigido al Menú Principal en...\n")
    for c in range(3, 0, -1):
        print(c, "...")
        time.sleep(1)
    opcion = menu.imprimeMenu()
    return opcion

def errorFichero(textoError):
    
    print(chr(1421)*30)
    print("\nERROR: ", textoError)
    print("\nPor favor vuelva a intentarlo\n")
    print("Será redirigido al Menú Ficheros en...\n")
    for c in range(3, 0, -1):
        print(c, "...")
        time.sleep(1)
    opcion = menu.menuFicheros()
    return opcion