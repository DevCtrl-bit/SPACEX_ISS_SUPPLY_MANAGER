#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:10:33 2021

VERSION: _1.2.3_ 

@author: diegotellez
"""
import sys #necesario para poder finalizar el programa inmediatamente cuando lo desee el usuario 
           # o en caso de producirse un error fatal que pudiera corromper la base de datos
import error
import menu
#import ficheros //valorar la opcion de crear un modulo para gestionar ficheros
import time
    
#VARIABLES 

cohetes = []#[['Falcon 1', 670], ['Falcon 9', 22800]]
peticiones = []#[['p1O', 'Oxígeno', 105.7, 28, 0], ['p2C', 'Comida', 300, 28, 0], ['p3R', 'Repuestos', 800, 61, 0], ['p4R', 'Repuestos', 20.2, 3, 0], ['p5G', 'Gas', 21594.3, 65, 0] ]
lanzamientos = []#[['Falcon 1', 10], ['Falcon 1', 30], ['Falcon 9', 60]]
cohetesLlenos = []
peticionesOrdenada = []
lanzamientosOrdenado = []
peticionAsignada = []
#peticionSimular = []
peticionCompletada = []
cohetesEnRuta = []


def gestionaMenu(opcion):
    
    if opcion == 1:
        tipoCohete(cohetes)
    elif opcion == 2:
        peticionSuministro(peticiones)
    elif opcion == 3:
        lanzamientoDisponible(lanzamientos)
    elif opcion == 4:
        asignacionPrioritarios(lanzamientos, peticiones, cohetes)
    elif opcion == 5:
        simulacionDias(peticiones)
    elif opcion == 6:
        infoSistema(cohetes, peticiones, lanzamientos)
    elif opcion == 7:
        gestionaFicheros(menu.menuFicheros())   
    elif opcion == 0:
        print("Hasta pronto")
        sys.exit()

def gestionaFicheros(opt):
      
    if opt == 1:
        guardaDatos(cohetes, peticiones, lanzamientos)
    elif opt == 2:
        cargaDatos()
    elif opt == 0:
        print("Hasta pronto")
        sys.exit()
        
def tipoCohete(cohetes):

    coheteTemp = []
        
    try:
        
        nombreCohete = input("Por favor introduzca el nombre del cohete:")
        
          
    except Exception as e:       
        
        gestionaMenu(error.errorComun(e.__doc__))
    
    else:
            
        for h in cohetes:
                
            while nombreCohete == h[0] or len(nombreCohete) < 3:
                print("Introduzca otro nombre (Debe contener al menos 3 caracteres y no existir previamente en el sistema)")
                try:
            
                    nombreCohete = input("Por favor introduzca el nombre del cohete:")
            
              
                except Exception as e:  
                    
                    gestionaMenu(error.errorComun(e.__doc__))
                       
    try:
        
        cargaUtil = input("Introduzca la carga útil del cohete:")
        
        while cargaUtil.isnumeric() == False:
            
            print("La carga util debe ser un numero entero positivo...")
        
            try: 
                cargaUtil = input("Introduzca la carga útil del cohete:")
                
            except Exception as e:       
        
                gestionaMenu(error.errorComun(e.__doc__))
        
        cargaUtil = int(cargaUtil)
        
    except Exception as e:       
        
        gestionaMenu(error.errorComun(e.__doc__))
    
    else:
        
        while type(cargaUtil) != int or cargaUtil<=0:
            
            print("La carga util debe ser un numero entero positivo...")
            try:
            
                cargaUtil = input("Introduzca la carga útil del cohete:")
                
                while cargaUtil.isnumeric()==False:
                    print("La carga util debe ser un numero entero positivo...")
                    cargaUtil = input("Introduzca la carga útil del cohete:")
                    
                cargaUtil = int(cargaUtil)
                    
            
            except Exception as e:       
        
                gestionaMenu(error.errorComun(e.__doc__))
            
    
    #EN CASO DE QUE TODO HAYA SIDO CORRECTO CON LA TOMA DE DATOS DEL USUARIO
    #SE ASIGNAN LOS VALORES DEL NUEVO COHETE A LA LISTA. ASI EVITAMOS QUE POR EJEMPLO
    #SE ASIGNE UN NOMBRE DE COHETE PREVIAMENTE A LA INTRODUCCION DE LA CARGA UTIL
    #QUE SI POR ERROR NO SE ASIGNARA NOS "DESBARATARÍA" LA LISTA DE COHETES

    coheteTemp.append(nombreCohete)
    coheteTemp.append(cargaUtil)
    
    cohetes.append(coheteTemp)
    
    print('COHETE INTRODUCIDO CON ÉXITO\n')

    print("Cohetes en sistema:\n")
    

    # con el siguiente bucle anidado vamos a mostrar los cohetes actuales al usuario
    for i in cohetes:       
        print("Cohete:", i[0])
        print("Carga útil:", i[1])
        print(chr(1421)*20)
           
    try:
        
        a = input("¿Deseea introducir otro cohete?(s/n):")
    
    except Exception as e:       
        
        gestionaMenu(error.errorComun(e.__doc__))
        
    if a == 's':
        tipoCohete(cohetes)
    elif a == 'n':  
        gestionaMenu(menu.imprimeMenu())
    else:
        gestionaMenu(error.errorComun())
    
    
def peticionSuministro(peticiones):
    
    peticionTemp = []
    
    try:
        
        numeroPeticion = input("Identificador de la petición:")
        
          
    except Exception as e:       
        
        gestionaMenu(error.errorComun(e.__doc__))
    
    else:
            
        for h in peticiones:
                
            while numeroPeticion == h[0] or len(numeroPeticion) < 3:
                print("Introduzca otro id de peticion (Debe contener al menos 3 caracteres y no existir previamente en el sistema)")
                try:
            
                    numeroPeticion = input("Identificador de la petición:")
            
              
                except Exception as e:       
        
                    gestionaMenu(error.errorComun(e.__doc__))
    
    try:
        
        tipoSuministro = input("Tipo de suministro:")        
          
    except Exception as e:       
        
        gestionaMenu(error.errorComun(e.__doc__))
    
    else:
        #vamos a exigir que el tipo de suministro tenga al menos 2 caracteres, ya que salvo 
        #"té" no se me ocurre otra posible petición con menos caracteres y aun así no se 
        #hasta que punto se solicitaría una petición con el ejemplo dado
        while len(tipoSuministro) < 2:
            
            print("Introduzca otro tipo de suministro (Debe contener al menos 2 caracteres)")
            
            try:
            
                tipoSuministro = input("Tipo de suministro:")  
            
              
            except Exception as e:       
        
                gestionaMenu(error.errorComun(e.__doc__))
    

    try:
        
        pesoSuministro = input("Cantidad solicitada, en KG:")
        
        while pesoSuministro.isnumeric() == False:
            
            print("El peso debe ser un número superior a 0...")
            
            try:
                
                pesoSuministro = input("Cantidad solicitada, en KG:")
            
              
            except Exception as e:       
        
                gestionaMenu(error.errorComun(e.__doc__))
            
            
        pesoSuministro = round(float(pesoSuministro), 3)
        
          
    except Exception as e:       
        
        gestionaMenu(error.errorComun(e.__doc__))
    
    else:
            
                
        while type(pesoSuministro) != float or pesoSuministro<=0:
            
            print("El peso debe ser superior a 0...")
            
            try:
                
                pesoSuministro = input("Cantidad solicitada, en KG:")
                
                while pesoSuministro.isnumeric()==False:
                    print("El peso debe ser superior a 0...")
                    pesoSuministro = input("Cantidad solicitada, en KG:")
                    
            except Exception as e:       
        
                gestionaMenu(error.errorComun(e.__doc__))
                
            pesoSuministro = round(float(pesoSuministro), 3)       
        
    try:
        
        tiempoSuministro = input("Dias para recibir:")
        
        while tiempoSuministro.isnumeric() == False:
            
            print("El tiempo debe ser un número entero positivo...")
            tiempoSuministro = input("Dias para recibir:")
        
        tiempoSuministro = int(tiempoSuministro)
        
          
    except Exception as e:       
        
        gestionaMenu(error.errorComun(e.__doc__))
    
    else:
            
                
        while type(tiempoSuministro) != int or tiempoSuministro <= 0:
            
            print("El tiempo debe ser superior a 0...")
            
            try:
                
                tiempoSuministro = input("Dias para recibir:")
                
                while tiempoSuministro.isnumeric() == False:
                    print("El tiempo debe ser superior a 0...")
                    tiempoSuministro = input("Dias para recibir:")
                
                tiempoSuministro = int(tiempoSuministro)
            
              
            except Exception as e:       
        
                gestionaMenu(error.errorComun(e.__doc__))
   
    #UNA VEZ QUE SABEMOS QUE TODOS LOS DATOS INTRODUCIDOS SON CORRECTOS SEGUN LAS ESPECIFICACIONES
    #DADAS POR EL CLIENTE, PODEMOS ASIGNARLAS A LA LISTA DE PETICIONES SIN DUDA DE COMPLICACIONES
    
    peticionTemp.append(numeroPeticion)
    peticionTemp.append(tipoSuministro)
    peticionTemp.append(pesoSuministro)
    peticionTemp.append(tiempoSuministro)
    peticionTemp.append(0) #por defecto ponemos las nuevas peticiones como no asignadas
    
    peticiones.append(peticionTemp)
    
    print('PETICION INTRODUCIDA CON ÉXITO')
    print(' ')
    
    print("Peticiones de suministro en sistema:")
    

    # con el siguiente bucle anidado vamos a mostrar las peticiones actuales al usuario
    for i in peticiones:
            print("Identificador:", i[0])
            print("Tipo de suministro :", i[1])
            print("Peso:", i[2])
            print("Tiempo para entrega:",i[3])
            if i[4]==0:
                print("Petición pendiente de asignar")
            elif i[4]==1:
                print("Petición previamente asignada")
            print(chr(1421)*20)
    
    a = input("¿Deseea introducir otra peticion?(s/n):")               
    
    if a == 's':
        peticionSuministro(peticiones)
    else:
        gestionaMenu(menu.imprimeMenu())
    

def lanzamientoDisponible(lanzamientos):
    flag = 0
    lanzamientoTemp = []
    
    if len(cohetes)==0:
        
        print("No existen cohetes en el sistema; para introducir lanzamientos por favor introduzca cohetes primero.")
        threeSecDelayToMainMenu()
        
    else:
        try:
            
            idCohete = input("Por favor introduzca el nombre exacto (con mayúsculas y/o minúsculas) del cohete:")
            
              
        except Exception as e:       
            
            gestionaMenu(error.errorComun(e.__doc__))
        
        else:
                               
            for i in cohetes:
                if i[0] == idCohete:
                    flag = 1
                    
            if flag != 1:
                print("No existe ningún cohete con ese nombre en el sistema...")
                lanzamientoDisponible(lanzamientos)
        
        
        try:
            
            tiempoMision = input("Introduzca dias de duracion de la mision:")
            
            while tiempoMision.isnumeric() == False:
                
                print("El tiempo debe ser un entero superior a 0...")
                tiempoMision = input("Introduzca dias de duracion de la mision:")
            
            tiempoMision = int(tiempoMision)
            
              
        except Exception as e:       
            
            gestionaMenu(error.errorComun(e.__doc__))
        
        else:
                
                    
            while type(tiempoMision) != int or tiempoMision <= 0:
                
                print("El tiempo debe ser un entero superior a 0...")
                
                try:
                    tiempoMision = input("Dias para recibir:")
                    while tiempoMision.isnumeric() == False:
                        print("El tiempo debe ser un entero superior a 0...")
                        tiempoMision = input("Dias para recibir:")
                    
                    tiempoMision = int(tiempoMision)
                
                  
                except Exception as e:       
            
                    gestionaMenu(error.errorComun(e.__doc__))
                
        
        #si todo ha ido bien, asignamos los datos del usuario a la lista de lanzamientos
        
        lanzamientoTemp.append(idCohete)
        lanzamientoTemp.append(tiempoMision)
        
        lanzamientos.append(lanzamientoTemp)
    
        print("LANZAMIENTO INTRODUCIDO CON EXITO\n")
    
        
        print("Lanzamientos en sistema:")
        
        # con el siguiente bucle anidado vamos a mostrar los cohetes actuales al usuario
        for i in lanzamientos:
    
                print("Cohete:", i[0])
                print("Días misión:", i[1])
                print(chr(1421)*20)
           
        
        a = input("¿Deseea introducir otro lanzamiento?(s/n):")
        
        if a == 's':
            lanzamientoDisponible(lanzamientos)
        else:
            gestionaMenu(menu.imprimeMenu()) 


def infoSistema(cohetes, peticiones, lanzamientos):
    
    print('')
    
    if len(cohetes)!=0:
    
        #MOSTRAMOS LISTA DE COHETES
        print("COHETES EN SISTEMA")
        print(chr(734)*10)
        for i in cohetes:       
            print("Cohete:", i[0])
            print("Carga útil:", i[1])
            print(chr(1421)*20)
    else:
        
        print("- NO EXISTEN COHETES EN EL SISTEMA. \n")
     
    if len(peticiones)!=0:
        #MOSTRAMOS LISTA DE PETICIONES    
        print("PETICIONES EN SISTEMA")
        print(chr(734)*10)        
        for i in peticiones:
                print("Identificador:", i[0])
                print("Tipo de suministro :", i[1])
                print("Peso:", i[2])
                if i[3]==0:
                    print("Tiempo para entrega: Petición ya entregada")
                else:
                    print("Tiempo para entrega:",i[3])
                                
                if i[4]==0:
                    print("Petición pendiente de asignar")
                elif i[4]==1:
                    print("Petición previamente asignada")
                    
                print(chr(1421)*20)
    else:
        
        print("- NO EXISTEN PETICIONES EN EL SISTEMA. \n")
          
    if len(lanzamientos)!=0:
        #MOSTRAMOS LISTA DE LANZAMIENTOS
        print("LANZAMIENTOS EN SISTEMA")
        print(chr(734)*10)
        for i in lanzamientos:
                print("Cohete:", i[0])
                if i[1]==0:
                    print("Días misión: Misión ya completada")
                else:
                    print("Días misión:", i[1])
                print(chr(1421)*20)
    
    else:
        
        print("- NO EXISTEN LANZAMIENTOS EN EL SISTEMA. \n")
    
    gestionaMenu(menu.imprimeMenu())

#LA SIGUIENTE FUNCIÓN VA A REALIZAR UNA ORDENACIÓN DE TIPO BURBUJA. RECORRERÁ LA LISTA TANTAS VECES 
#COMO ELEMENTOS CONTENGA LA LISTA ORIGINAL
#PARA ASEGURARNOS DE ORDENARLA COMPLETA DE MENOR A MAYOR (POR TIEMPO DE ENTREGA)
#APROVECHAMOS LA ASIGNACION SIMULTANEA QUE NOS PERMITE PYTHON PARA NO MACHACAR DATOS DE LA LISTA
#SIN USAR VARIABLE TEMPORAL  
def ordenaPeticiones(peticionesOrdenada):
    
    for j in range(len(peticionesOrdenada)):
        for i in range(len(peticionesOrdenada)-1):
            if peticionesOrdenada[i][3] > peticionesOrdenada[i+1][3]:
                peticionesOrdenada[i], peticionesOrdenada[i+1] = peticionesOrdenada[i+1], peticionesOrdenada[i]
     
    print("PETICIONES ORDENADAS")
    print(chr(734)*20)   
    for i in peticionesOrdenada:
            print("Identificador:", i[0])
            print("Tipo de suministro :", i[1])
            print("Peso:", i[2])
            if i[3] == 0:
                print("Tiempo para entrega: petición ya entregada")
            else:
                print("Tiempo para entrega:",i[3])
            print(chr(1421)*20)
#LA SIGUIENTE FUNCIÓN VA A REALIZAR UNA ORDENACIÓN DE TIPO BURBUJA. RECORRERÁ LA LISTA TANTAS VECES 
#COMO ELEMENTOS CONTENGA LA LISTA ORIGINAL
#PARA ASEGURARNOS DE ORDENARLA COMPLETA DE MENOR A MAYOR (POR TIEMPO DE ENTREGA) 
#APROVECHAMOS LA ASIGNACION SIMULTANEA QUE NOS PERMITE PYTHON PARA NO MACHACAR DATOS DE LA LISTA
#SIN USAR VARIABLE TEMPORAL                      
def ordenaLanzamientos(lanzamientosOrdenado):
    
#ESTA FUNCION VA A ASIGNAR LAS PETICIONES A LOS LANZAMIENTOS SIGUIENDO LA PRIORIDAD ESTABLECIDA POR
#LAS FUNCIONES DE ORDENACION. SE ASIGNARAN PRIMERO LAS PETICIONES MAS URGENTES Y SE USARAN PRIMERO
#LOS LANZAMIENTOS QUE LLEGUEN ANTES. MOSTRAREMOS POR CONSOLA UN REGISTRO DE LO QUE VA OCURRIENDO
    for j in range(len(lanzamientosOrdenado)):
        for i in range(len(lanzamientosOrdenado)-1):
            if lanzamientosOrdenado[i][1] > lanzamientosOrdenado[i+1][1]:
                lanzamientosOrdenado[i], lanzamientosOrdenado[i+1] = lanzamientosOrdenado[i+1], lanzamientosOrdenado[i]
    
    print("LANZAMIENTOS ORDENADOS")
    print(chr(734)*10)

    for i in lanzamientosOrdenado:
        
        print("Cohete:", i[0])
        if i[1] == 0:
            print("Días misión: misión finalizada")
        else:
            print("Días misión:", i[1])
        print(chr(1421)*20)

    
def asignacionPrioritarios(lanzamientos, peticiones, cohetes):
    
    if len(cohetes)==0 or len(peticiones)==0 or len(lanzamientos)==0:
        
        print("No existen datos suficientes para llevar a cabo la asignación. Por favor introduce cohetes, peticiones y lanzamientos.")
        
        threeSecDelayToMainMenu()
     
    peticionesOrdenada = peticiones.copy()
    ordenaPeticiones(peticionesOrdenada)
    lanzamientosOrdenado = lanzamientos.copy()
    ordenaLanzamientos(lanzamientosOrdenado)

    asignar = True
    
    if len(peticionAsignada)!=0:
        asignar = False
    
    #PARA COMPRENDER LA ASIGNACION DEBEMOS TENER MUY CLARAS LAS ESTRUCTURAS DE DATOS ASI COMO LAS 
    #VARIABLES DE ITERACION QUE SE USARÁ CON CADA UNA (I, J, K, ETC...) YA QUE IREMOS RECORRIENDO LAS
    #LISTAS DE DATOS USANDO LOS INDICES QUE CORRESPONDAN 
    for i in peticionesOrdenada: #check i[3] numero de dias
        
        if i[4]==0: #La peticion debe no haber sido asignada previamente para ser tenida en cuenta en la asignación
            
            for k in lanzamientosOrdenado: #check k[1] numero de dias
    
                #el requisito principal de asignación es que los dias de la peticion sean superiores a los dias
                #del lanzamiento. Además para no tener en cuenta en futuras asignaciones las peticiones ya asignadas
                #o entregadas estas deben tener mas de 0 dias (ya ha sido entregada)
                if i[3] >= k[1] and i[3]>0 :
                                    
                    for j in cohetes: # j[0] es nombreCohete j[1] es cargaUtil
                        
                        if k[0] == j[0]:
                            
                            j[1] = j[1] - i[2]
                                                 
                            if j[1] == 0:
                                
                                    
                                for f in peticionAsignada:
                                    
                                    #comprobamos que la peticion no haya sido asignada previamente
                                    if f[0] == i[0]:
                                        
                                        asignar = False
                                        
                                    else:
                                        
                                        asignar = True
                                    
                                while asignar:
                                    
                                    print("La petición ", i[0], "(", i[2], " Kg de ", i[1], ")")
                                    print("ha sido asignada al cohete ", k[0], "...Duración lanzamiento: ", k[1], "dias.\n")
                                    peticionAsignada.append([i[0],k[1], j[0], 0])   
                                    cohetesLlenos.append(j[0]) 
                                    cambioEstado = peticiones.index(i)
                                    peticiones[cambioEstado][4]=1 #Actualizamos el estado de la peticion a "Asignada" 
                                    print("ATENCION: EL COHETE ", j[0], " ESTÁ CARGADO A MÁXIMA CARGA\n")
                                    break
                                    
                                    
                            elif j[1] < 0:
                                #para no dejar la carga util en menos de cero si hubieramos
                                #llegado al límite, volvemos atrás de este modo.
                                #así además cumplimos el requisito de llenar cohetes hasta
                                #que tengan la carga util menor a cualquier petición pendiente
                                #y nunca se asignará carga a dicho cohete
                                j[1] = j[1] + i[2]
                            
                            else:
                                #comprobamos que la peticion no haya sido asignada previamente
                                for g in peticionAsignada:
                                    
                                    if g[0] == i[0]:
                                        
                                        asignar = False
                                    
                                    else:
                                        
                                        asignar = True
                                    
                                while asignar:
                                    print("La petición ", i[0], "(", i[2], " Kg de ", i[1], ")")
                                    print("ha sido asignada al cohete ", k[0], "...Duración lanzamiento: ", k[1], "dias.")
                                    
                                    print("El cohete ", k[0], " aún dispone de ", j[1], "kg de carga útil.\n")
                                    
                                    peticionAsignada.append([i[0],k[1],j[0], 0])  
                                    
                                    cambioEstado = peticiones.index(i)
                                    peticiones[cambioEstado][4]=1 #Actualizamos el estado de la peticion a "Asignada" 
    
                                   
                                    cohetesLlenos.append(j[0])
                             
                                    break

        
     
    print("MISIONES IMPOSIBLES DE CUMPLIR:")  #cualquier peticiones que siga en la lista de peticiones significa que no ha sido posible de cumplit
    print(chr(734)*35)                
    for z in peticiones:
        
        if z[4]!=1:
            
            print("La petición", z[0], " es imposible de cumplir")
            print(chr(734)*15)
        
            
        
    print("PETICIONES YA ASIGNADAS PERO NO ENVIADAS")
    print(chr(734)*38)

    for r in peticionAsignada:
           
        if r[3]==0:
            print("Mision: ", r[0], " Duración: ", r[1], " Cohete asignado: ", r[2])
            print(chr(734)*15)
                          
    gestionaMenu(menu.imprimeMenu()) 
#EN ESTA FUNCION VAMOS A SIMULAR EL PASO DE LOS DIAS Y SE IRÁN DESCONTANDO DIAS A LOS LANZAMIENTOS
#HASTA QUE LAS ENTREGAS VAYAN COMPLETANDOSE. MOSTRAREMOS POR CONSOLA UN REGISTRO DE LO QUE VA OCURRIENDO
def simulacionDias(peticiones):
    
    if len(peticionAsignada) == 0:
        
        print("NO HAY DATOS SUFICIENTES EN EL SISTEMA PARA REALIZAR LA SIMULACIÓN, POR FAVOR INTRODUZCA COHETES, PETICIONES Y LANZAMIENTOS Y ASIGNE LAS PETICIONES.")
        threeSecDelayToMainMenu()
        
    else:
        cohetesEnRutaTemp = []
        try:
            dias = input("¿Cuantos días van a pasar?:")
            
            while dias.isnumeric() == False:
                print("El número de dias debe ser un entero positivo...")
                dias = input("¿Cuantos días van a pasar?:")
            
            dias = int(dias)
            
        except Exception as e:       
            
            gestionaMenu(error.errorComun(e.__doc__))
        
        else:
                
                    
            while dias <= 0 or type(dias) != int:
                
                print("El tiempo debe ser superior a 0...")
                
                try:
                    
                    dias = input("¿Cuantos días van a pasar?:")
                    while dias.isnumeric() == False:
                        print("El tiempo debe ser superior a 0...")
                        dias = input("¿Cuantos días van a pasar?:")
                        
                    dias = int(dias)
                      
                except Exception as e:       
            
                    gestionaMenu(error.errorComun(e.__doc__))
        
        
        #AHORA SE LANZARÍAN TODOS LOS COHETES QUE TUVIERAN CARGA ASIGNADA
        for i in peticionAsignada: #Cada peticion asignada se compone de IDmision, duracion, cohete, enviada (0 no 1 si)
            for j in peticiones: #j[3] son numero de dias
                
                if i[0] == j[0]:
                    i[1] = i[1] - dias
                    
                    if i[1]<=0:
                        if i[3]==0:
                            print("\n",chr(1421),"La petición ", j[0], " ha sido entregada a tiempo.")
                            peticionCompletada.append(j[0])
                            i[3] = 1                      
                            j[3] = 0
                        i[1] = 0
                for r in lanzamientos:
                    r[1] -= dias
                    if r[1]<0:
                        r[1]=0
                        
        print("\nPETICIONES PENDIENTES DE ENTREGA:\n")
        print(chr(734)*20)
        for g in peticiones:
            if g[3]!=0:
                print("Id de la petición: ", g[0])
        
        print("\nHISTÓRICO DE PETICIONES ENTREGADAS:\n")
        print(chr(734)*20)
        for g in peticionAsignada:
            if g[3]==1:
                print("Id de la petición: ", g[0])
        print("\n")  
        #AHORA SE QUITAN LOS COHETES LANZADOS DE LA LISTA DE DISPONIBLES
        for m in lanzamientos:
            
            if m[1]!=0:
                
                cohetesEnRutaTemp.append(m[0])      
                cohetesEnRutaTemp.append(m[1])
                
                cohetesEnRuta.append(cohetesEnRutaTemp)
                
           # elif lanzamientos[m] >= dias:                     
                
        print("COHETES EN RUTA:")
        print(chr(734)*20)
        
        compruebaRepite = 0
               
        for n in peticionAsignada:
            
            if n[1]!=0:
                if compruebaRepite != n[2]:
                    print("NOMBRE DEL COHETE: ", n[2])
                    compruebaRepite=n[2]
                    print("Dias de viaje restantes: ", n[1])
    
        print("\n")
        gestionaMenu(menu.imprimeMenu())
                    
        #SE ACTUALIZA LISTA cohetesEnRuta CON LOS COHETES LANZADOS
        #cohetesEnRuta tendrá dos elementos: nombreCohete y diasLlegada
    
def guardaDatos(cohetes, peticiones, lanzamientos):
    
    if len(cohetes)==0 or len(peticiones)==0 or len(lanzamientos)==0:
        print("No existen datos suficientes en el sistema para guardar")
        print("Por favor asegurese de introducir datos para cohetes, peticiones y lanzamientos")
        print("Redirigiendo al menú principal, en...")
        
        threeSecDelayToMainMenu()
        
    try: nombreFichero = input("Introduzca el nombre del fichero:")
    except Exception as e: gestionaFicheros(error.errorFichero(e.__doc__))
    else:
        
        while len(nombreFichero)<=3:
            
            print("El nombre del fichero debe contener al menos 3 caracteres")
            
            guardaDatos(cohetes, peticiones, lanzamientos)
    
    try:fichero = open(nombreFichero+".txt",'w') 
    except Exception as e: gestionaFicheros(error.errorFichero(e.__doc__))
    
    try:
        fichero.write('COHETES:\n')
        fichero.write(str(len(cohetes)))
        fichero.write('\n')
        #fichero.write(str(len(cohetes)))
        #fichero.write(',')
        for i in cohetes:
            fichero.write(str(i))
            fichero.write('\n')
        #fichero.write('\n')
    except Exception as e: 
        fichero.close()
        gestionaFicheros(error.errorFichero(e.__doc__))
    
    print("Backup de COHETES completado con éxito...")
    time.sleep(1.5)
    
    try:
        fichero.write('\nPETICIONES:\n')
        fichero.write(str(len(peticiones)))
        fichero.write('\n')
        #fichero.write(str(len(peticiones)))
        #fichero.write(',')
        for j in peticiones:
            
            fichero.write(str(j))
            fichero.write('\n')
        #fichero.write('\n')
    except Exception as e: 
        fichero.close()
        gestionaFicheros(error.errorFichero(e.__doc__))
        
    print("Backup de PETICIONES completado con éxito...")
    time.sleep(1.5)
    
    try:
        fichero.write('\nLANZAMIENTOS:\n')
        fichero.write(str(len(lanzamientos)))
        fichero.write('\n')
        #fichero.write(str(len(lanzamientos)))
        #fichero.write(',')
        for k in lanzamientos:
            fichero.write(str(k))
            fichero.write('\n')
        #fichero.write('\n')
    except Exception as e: 
        fichero.close()
        gestionaFicheros(error.errorFichero(e.__doc__))
        
    print("Backup de LANZAMIENTOS completado con éxito...")
    time.sleep(1.5)   
    
    #haciendo backup de las peticiones asignadas aseguramos que se mantenga el sistema si se guarda tras hacer la asignacion
    if len(peticionAsignada) != 0:
        try:
            fichero.write('\nPETICIONES ASIGNADAS:\n')
            fichero.write(str(len(peticionAsignada)))
            fichero.write('\n')
            #fichero.write(str(len(peticiones)))
            #fichero.write(',')
            for j in peticionAsignada:
                
                fichero.write(str(j))
                fichero.write('\n')
        #fichero.write('\n')
        except Exception as e: 
            fichero.close()
            gestionaFicheros(error.errorFichero(e.__doc__))
    
    try: fichero.close()
    except Exception as e: gestionaFicheros(error.errorFichero(e.__doc__))
    
    print("BACKUP completado con éxito, será redirigido al Menú Principal en...")
    
    threeSecDelayToMainMenu()
    
def cargaDatos():
        
    try: nombreFichero = input("Introduzca el nombre del fichero:")
    except Exception as e: gestionaFicheros(error.errorFichero(e.__doc__))
    
    try:
        fichero = open(nombreFichero+".txt") #sin especificar modo abrirá en modo lectura (r) por defecto
    except Exception as e: gestionaFicheros(error.errorFichero(e.__doc__))
    else:
        
        #CARGAMOS COHETES
        ###################################################
        
        
        conjunto = fichero.readline().replace('\n', '')
        numeroElementos = int(fichero.readline().replace('\n', ''))
        
        #x = [[] for i in range(3)]
        
        cohetes_TEST_fichero = [[] for i in range(numeroElementos)] #inicializamos una lista vacía con tantos elementos como sean necesarios
        
        if conjunto == 'COHETES:':
            
            for i in range (0, numeroElementos, +1):
                
                for dato in fichero.readline().split(','):
                    
                    try:
                        int(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        cohetes_TEST_fichero[i].append(int(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", '')))
                        #print('dato en cohetes_TEST_fichero[',i,'] en cada vuelta = ',dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        
                    except:
                        
                        try: #en caso de que se haya operado ya con la carga util, esta se habrá convertido a float por lo que en siguientes cargas no lo convertirá a int si no a string. Lo evitamos como sigue:
                            float(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                            cohetes_TEST_fichero[i].append(float(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", '')))                           
        
                        except:cohetes_TEST_fichero[i].append(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        #print('dato en cohetes_TEST_fichero[',i,'] en cada vuelta = ',dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))

                    
                               
        global cohetes 
        cohetes = cohetes_TEST_fichero.copy()  
        
        for k in cohetes:
            for j in range (0, len(cohetes)-1, 1):
                print("tipo de dato de:",j, type(k[j]) )
        
        print("Datos de COHETES cargados con éxito.")
        time.sleep(1)  
                       
        #CARGAMOS PETICIONES
        ###################################################
        
        fichero.readline() #esta lectura nos permite saltar la linea en blanco tras el último elemento
        conjunto = fichero.readline().replace('\n', '')
        numeroElementos = int(fichero.readline().replace('\n', ''))
        
        #x = [[] for i in range(3)]
        
        peticiones_TEST_fichero = [[] for i in range(numeroElementos)] #inicializamos una lista vacía con tantos elementos como sean necesarios
        
        if conjunto == 'PETICIONES:':
            
            for i in range (0, numeroElementos, +1):
                
                for dato in fichero.readline().split(','):
                    
                    try:
                        float(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        peticiones_TEST_fichero[i].append(float(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", '')))
                        #print('dato en cohetes_TEST_fichero[',i,'] en cada vuelta = ',dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        
                    except:
        
                        peticiones_TEST_fichero[i].append(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        #print('dato en cohetes_TEST_fichero[',i,'] en cada vuelta = ',dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))

        
        for i in peticiones_TEST_fichero:
            for k in range (3, 5, 1):
                i[k]=int(i[k])
                
                   
        global peticiones
        peticiones = peticiones_TEST_fichero.copy()  

        print("Datos de PETICIONES cargados con éxito.")
        time.sleep(1)         
        
        
        #CARGAMOS LANZAMIENTOS
         ###################################################

        fichero.readline()
        conjunto = fichero.readline().replace('\n', '')
        numeroElementos = int(fichero.readline().replace('\n', ''))
        
        lanzamientos_TEST_fichero = [[] for i in range(numeroElementos)] #inicializamos una lista vacía con tantos elementos como sean necesarios
        
        if conjunto == 'LANZAMIENTOS:':
            
            for i in range (0, numeroElementos, +1):
                
                for dato in fichero.readline().split(','):
                    
                    try:
                        int(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        lanzamientos_TEST_fichero[i].append(int(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", '')))
                        #print('dato en cohetes_TEST_fichero[',i,'] en cada vuelta = ',dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        
                    except:
        
                        lanzamientos_TEST_fichero[i].append(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                        #print('dato en cohetes_TEST_fichero[',i,'] en cada vuelta = ',dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))

                    
                               
        global lanzamientos
        lanzamientos = lanzamientos_TEST_fichero.copy()  
        
        print("Datos de LANZAMIENTOS cargados con éxito.")
        time.sleep(1)  
                
        #CARGAMOS PETICIONES ASIGNADAS
        #################################################
        try:
            fichero.readline() #esta lectura nos permite saltar la linea en blanco tras el último elemento
            conjunto = fichero.readline().replace('\n', '')
            numeroElementos = int(fichero.readline().replace('\n', ''))
            
            #x = [[] for i in range(3)]
            
            peticionesASIGNA_TEST_fichero = [[] for i in range(numeroElementos)] #inicializamos una lista vacía con tantos elementos como sean necesarios
            
            if conjunto == 'PETICIONES ASIGNADAS:':
                
                for i in range (0, numeroElementos, +1):
                    
                    for dato in fichero.readline().split(','):
                        
                        try:
                            int(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                            peticionesASIGNA_TEST_fichero[i].append(int(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", '')))
                            #print('dato en cohetes_TEST_fichero[',i,'] en cada vuelta = ',dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                            
                        except:
            
                            peticionesASIGNA_TEST_fichero[i].append(dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
                            #print('dato en cohetes_TEST_fichero[',i,'] en cada vuelta = ',dato.replace('\n', '').replace('[', '').replace(']', '').replace("'", ''))
    
                                        
            global peticionAsignada
            peticionAsignada = peticionesASIGNA_TEST_fichero.copy()  
            
            print("Datos de PETICIONES ASIGNADAS cargados con éxito.")
            time.sleep(1)            
            

        except:
            print("No existen peticiones asignadas en el fichero. Haga una asignación si desea realizar una simulación.")
            
    try: fichero.close() 
    except Exception as e: gestionaFicheros(error.errorFichero(e.__doc__))
    else:
        print("\nVolviendo al menu en...")
        threeSecDelayToMainMenu()
     
    
def threeSecDelayToMainMenu():
    for c in range(3, 0, -1):
            print(c, "...")
            time.sleep(1)
    
    gestionaMenu(menu.imprimeMenu())
    
#COMIENZA MAIN

mensajeBienvenida = "BIENVENIDO A ISS_SUPPLY"

print('\n', mensajeBienvenida)
print(chr(773)*len(mensajeBienvenida))

gestionaMenu(menu.imprimeMenu())


    

    
    
