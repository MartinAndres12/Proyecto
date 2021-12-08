# Martin Bahamondes | 21.125.833-0
while True: 
    print("Bienvenid@!, seleccione con el numero correspondiente la region a consultar.")
    print("- - - - -")
    print("Regiones disponibles: ")

    print("1  - Arica y Parinacota")
    print("2  - Tarapacá")
    print("3  - Antofagasta")
    print("4  - Coquimbo")
    print("5  - Valparaíso")
    print("6  - Metropolitana")    
    print("7  - O'Higgins")
    print("8  - Maule")
    print("9  - Ñuble")
    print("10 - Biobío")
    print("11 - Araucanía")
    print("12 -  Los Ríos")
    print("13 - Los Lagos")
    print("14 - Aysén")
    print("15 - Magallanes")


    regionseleccionada = input()

    regiones = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

    while not regionseleccionada in regiones:
        print("         ✘ Error ✘")
        print("             ↓    ")
        print("Seleccione una region disponible")
        regionseleccionada = input()
    else:
        print("Region selecionada correctamente...")



    if regionseleccionada == regiones[0]:
        print("• Arica y Parinacota •")

    else:
        if regionseleccionada == regiones[1]:
            print("Cargando2")
        else:
            if regionseleccionada == regiones[2]:
                print("Cargando3")
            else: 
                if regionseleccionada == regiones[3]:
                    print("Cargando4")
                else: 
                    if regionseleccionada == regiones[4]:
                        print("Cargando4")
                    else: 
                       if regionseleccionada == regiones[5]:
                            print("Cargando4")
                    
    









    if input("Le gustaría repetir el programa? (y/n) → " ) == "n": 
      exit()                                                         
    print("")         