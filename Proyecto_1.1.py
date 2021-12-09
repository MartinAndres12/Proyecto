# Martin Bahamondes | 21.125.833-0

import pandas as pd

while True: 
    print("Bienvenid@!, seleccione con el numero correspondiente la región a consultar.")
    print("- - - - -")
    print("Regiones disponibles: ")

    print(" 1  - Arica y Parinacota")
    print(" 2  - Tarapacá")
    print(" 3  - Antofagasta")
    print(" 4  - Atacama")
    print(" 5  - Coquimbo")
    print(" 6  - Valparaíso")
    print(" 7  - Metropolitana")    
    print(" 8  - O'Higgins")
    print(" 9  - Maule")
    print(" 10 - Ñuble")
    print(" 11 - Biobío")
    print(" 12 - Araucanía")
    print(" 13 - Los Ríos")
    print(" 14 - Los Lagos")
    print(" 15 - Aysén")
    print(" 16 - Magallanes")
    print("")
    print(" 17 - Salir")
    print("")


    regionseleccionada = input()

    regiones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]

    while not regionseleccionada in regiones:
        print("         ✘ Error ✘")
        print("             ↓    ")
        print("Seleccione un numero disponible")
        print("")
        regionseleccionada = input()
    else:
        print("")
        print("► Cargando...")
        print("")



    if regionseleccionada == regiones[0]:
        print("     • Arica y Parinacota •")
        print("1) ")
        print("2) ")
        print("3) ")
    else:
        if regionseleccionada == regiones[1]:
            print("     • Tarapacá •")
            print("1) ")
            print("2) ")
            print("3) ")
        else:
            if regionseleccionada == regiones[2]:
                print("     • Antofagasta •")
                print("1) ")
                print("2) ")
                print("3) ")
            else: 
                if regionseleccionada == regiones[3]:
                    print("     • Atacama •")
                    print("1) ")
                    print("2) ")
                    print("3) ")
                else: 
                    if regionseleccionada == regiones[4]:
                        print("     • Coquimbo •")
                        print("1) ")
                        print("2) ")
                        print("3) ")
                    else: 
                       if regionseleccionada == regiones[5]:
                            print("     • Valparaíso •")
                            print("1) ")
                            print("2) ")
                            print("3) ")
                       else:
                           if regionseleccionada == regiones[6]:
                                print("     • Metropolitana •")
                                print("1) ")
                                print("2) ")
                                print("3) ")
                           else:
                               if regionseleccionada == regiones[7]:
                                   print("     • O'Higgins •")
                                   print("1) ")
                                   print("2) ")
                                   print("3) ")
                               else:
                                   if regionseleccionada == regiones[8]:
                                       print("     • Maule •")
                                       print("1) ")
                                       print("2) ")
                                       print("3) ")
                                   else:
                                       if regionseleccionada == regiones[9]:
                                           print("     • Ñuble •")
                                           print("1) ")
                                           print("2) ")
                                           print("3) ")
                                       else:
                                           if regionseleccionada == regiones[10]:
                                               print("     • Biobío •")
                                               print("1) ")
                                               print("2) ")
                                               print("3) ")
                                           else:
                                               if regionseleccionada == regiones[11]:
                                                   print("     • Araucanía •")
                                                   print("1) ")
                                                   print("2) ")
                                                   print("3) ")
                                               else:
                                                   if regionseleccionada == regiones[12]:
                                                       print("     • Los Ríos •")
                                                       print("1) ")
                                                       print("2) ")
                                                       print("3) ")
                                                   else:
                                                       if regionseleccionada == regiones[13]:
                                                           print("     • Los Lagos •")
                                                           print("1) ")
                                                           print("2) ")
                                                           print("3) ")
                                                       else:
                                                           if regionseleccionada == regiones[14]:
                                                               print("     • Aysén •")
                                                               print("1) ")
                                                               print("2) ")
                                                               print("3) ")
                                                           else:
                                                               if regionseleccionada == regiones[15]:
                                                                   print("     • Magallanes •")
                                                                   print("1) ")
                                                                   print("2) ")
                                                                   print("3) ")
                                                                   
                                                               else:
                                                                   if regionseleccionada == regiones[16]:
                                                                       exit()
                            
                    
    








    print("")
    if input("Le gustaría repetir el programa? (y/n) → " ) == "n": 
      exit()                                                         
    print("")         