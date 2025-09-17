




with open("./file/menu_gruppi.txt" , encoding="utf-8") as file:
    menu = file.read()

cmd = ""
leggi_file = True

while cmd != "0":
    if leggi_file:
        with open("./file/es13_file_GroupMusic.csv") as file:
            gruppi: list[list[str,int,str]] = []

            lista_righe = file.read().splitlines()

            for riga in lista_righe:
                lista_dati_gruppo = riga.split(",")
                lista_dati_gruppo[1] = int(lista_dati_gruppo[1])
                gruppi.append(lista_dati_gruppo)
        leggi_file = False

    print()
    print(menu)
    print()
    cmd = input("Inserisci il comando: ")
    ris = ""

    if cmd == "0":
        ris += "Termino il programma"

    elif cmd == "1":
        for gruppo in gruppi:
            ris += f"Gruppo: {gruppo[0]} - N. Dischi: {gruppo[1]} - Paese: {gruppo[2]}\n"

    elif cmd == "2":
        somma = 0
        for gruppo in gruppi:
            somma += gruppo[1]

            media = round(somma / len(gruppi))
        ris = f"La media dei dischi è {media}"

    elif cmd == "3":
        for gruppo in gruppi:
            if gruppo[2] == "Regno Unito":
                ris += f"Gruppo: {gruppo[0]} - N. Dischi: {gruppo[1]} - Paese: {gruppo[2]}\n"

    elif cmd == "4":
        somma = 0
        count = 0

        for gruppo in gruppi:
            if gruppo[2] == "Regno Unito":
                somma += gruppo[1]
                count += 1
        
        media = round(somma / count)
        ris = f"La media dei dischi dei gruppi inglesi è {media}"
    
    elif cmd == "5":
        somma = 0
        count = 0

        for gruppo in gruppi:
            if gruppo[2] == "Stati Uniti":
                somma += gruppo[1]
                count += 1
        
        media = round(somma / count)
        ris = f"La media dei dischi dei gruppi americani è {media}"

    elif cmd == "6":
        for gruppo in gruppi:
            if gruppo[1] > 10:
                ris += f"Gruppo: {gruppo[0]} - N. Dischi: {gruppo[1]} - Paese: {gruppo[2]}\n"

    elif cmd == "7":

        gruppi_ord = gruppi.copy()

        for i in range(len(gruppi_ord)):
            for j in range(i+1, len(gruppi_ord)):
                if gruppi_ord[j][1] < gruppi_ord[i][1]:
                    temp = gruppi_ord[i]
                    gruppi_ord[i] = gruppi_ord[j]
                    gruppi_ord[j] = temp
                
        for gruppo in gruppi_ord:
            ris += f"Gruppo: {gruppo[0]} - N. Dischi: {gruppo[1]} - Paese: {gruppo[2]}\n"

    elif cmd == "8":
        minimo = gruppi[0][1]
        cont = 0
        for gruppo in gruppi:
            if gruppo[1] < minimo:
                minimo = gruppo[1]
                ris = f"{gruppo[0]} - N. Dischi: {gruppo[1]}\n"
                cont = 1
            elif gruppo[1] == minimo:
                ris += f"{gruppo[0]} - N. Dischi: {gruppo[1]}\n"
                cont += 1

        ris = f"{"Gruppo" if cont == 1 else "Gruppi"} con meno dischi:\n{ris}" 

    elif cmd == "9":
        diz_paesi = {}

        for gruppo in gruppi:
            if gruppo[2] not in diz_paesi:
                diz_paesi[gruppo[2]] = 1
            else:
                diz_paesi[gruppo[2]] += 1
        
        for k, v in diz_paesi.items():
            ris += f"Paese: {k} - N. Gruppi: {v}\n"

    elif cmd == "10":
        nome = input("Inserisci un nome: ").casefold()
        
        ris = f"{nome} non è presente"
        for gruppo in gruppi:
            if gruppo[0].casefold() == nome:
                ris = f"{nome} è presente"
    
    elif cmd == "11":
        parola = input("Inserisci il termine da cercare: ").casefold()
        print()
        ris = f"Gruppi che contengono nel nome {parola}:\n"
        for gruppo in gruppi:
            if parola in gruppo[0].casefold():
                ris += f"Gruppo: {gruppo[0]} - N. Dischi: {gruppo[1]} - Paese: {gruppo[2]}\n"

    elif cmd == "12":
        nome = input("Inserisci il nome: ")
        dischi = int(input("Inserisci il numero di dischi: "))
        paese = input("Inserisci il paese: ")

        stringa_per_file = f"\n{nome},{dischi},{paese}"
        with open("./res/gruppi.csv", "a") as file:
            file.write(stringa_per_file)
        leggi_file = True
        ris = "Gruppo aggiunto con successo"
        

    elif cmd == "13":
        paese = input("Inserisci il paese: ").casefold()

        testo_file = ""

        for gruppo in gruppi:
            if gruppo[2].casefold() != paese:
                testo_file += f"{gruppo[0]},{gruppo[1]},{gruppo[2]}\n"

        with open("./file/es13_file_GroupMusic.csv", "w") as file:
            file.write(testo_file[:-1])
        
        leggi_file = True
        ris = "File modificato con successo"
    
    else:
        ris = "Comando sconosciuto"

    print(ris)