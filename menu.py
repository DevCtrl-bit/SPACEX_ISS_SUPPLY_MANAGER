#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 04:10:22 2021

@author: diegotellez
"""

def imprimeMenu():
    #Usamos un diccionario para mostrar el menu completo con una sola instrucción iterativa
    diccionarioMenu = {'1':'AÑADIR COHETES', 
                   '2':'SOLICITAR PETICIONES ESTACIÓN', 
                   '3':'INTRODUCIR LANZAMIENTOS DISPONIBLES', 
                   '4':'ASIGNAR PETICIONES A LANZAMIENTOS',
                   '5':'SIMULACION DIAS',
                   '6':'INFORMACION DEL SISTEMA',
                   '7':'FICHEROS',
                   '0':'SALIR'}
    print(chr(1421)*18)
    print(chr(1421), " .-MENU PRINCIPAL-. ", chr(1421))
    print(chr(1421)*18)
    
    for i in diccionarioMenu:
        print(chr(1421), i, ".- ", diccionarioMenu.get(i))
    
    try:    
        print('\n')
        opcion = int(input("POR FAVOR ELIJA UNA OPCIÓN:"))
        while type(opcion)!= int or opcion < 0 or opcion > 7:
            print("Elija una opción (0-7) del menú...")
            opcion = int(input("POR FAVOR ELIJA UNA OPCIÓN:"))
        
        return opcion
    except:
        print("Debe introducir un número de las opciones disponibles.")
        opcion = imprimeMenu()
        
    return opcion
  
def menuFicheros():
    
    print(chr(1421)*17)
    print(chr(1421), " .-MENU FICHEROS-. ", chr(1421))
    print(chr(1421)*17)
    
    ficheroMenu = {'1':'Guardar datos', 
                   '2':'Cargar datos', 
                   '0':'Salir'}
    
    for i in ficheroMenu:
        print(chr(1421), i, ".- ", ficheroMenu.get(i))
    
    try:    
        print('\n')
        opcion = int(input("POR FAVOR ELIJA UNA OPCIÓN:"))
        while type(opcion)!= int or opcion < 0 or opcion > 2:
            print("Elija una opción (0-2) del menú...")
            opcion = int(input("POR FAVOR ELIJA UNA OPCIÓN:"))
        
        return opcion
    except:
        print("Debe introducir un número de las opciones disponibles.")
        opcion = menuFicheros()
        
    return opcion
    
    
    
    
    
    
    
    
    