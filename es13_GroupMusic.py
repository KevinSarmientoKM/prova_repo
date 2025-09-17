"""
1 - Elenco di tutti i gruppi
2 - Media complessiva dei dischi
3 - Elenco dei gruppi britannici (nome, dischi, paese)
4 - Media dischi dei gruppi britannici
5 - Media dischi dei gruppi americani
6 - Elenco dei gruppi che hanno più di 10 dischi
7 - Elenco dei gruppi in base al numero di dischi in ordine crescente
8 - Gruppo con meno dischi
9 - Conteggio dei gruppi per ogni paese
10 - Chiedere all'utente di inserire un nome e verificare se il gruppo è presente
11 - Elenco dei gruppi il cui nome contiene una specifica parola o carattere (chiedere all'utente)
12 - Aggiungi un nuovo gruppo
13 - Elimina i gruppi in base al paese indicato dall'utente
"""


gruppi = []
with open("./file/es13_file_GroupMusic.csv", "r") as f:
    for riga in f:
        nome, dischi, paese = riga.strip().split(",")
        gruppi.append({
            "nome": nome.strip(),
            "dischi": int(dischi.strip()),
            "paese": paese.strip()
        })

while True:
    print("""
1 - Elenco di tutti i gruppi
2 - Media complessiva dei dischi
3 - Elenco dei gruppi britannici
4 - Media dischi dei gruppi britannici
5 - Media dischi dei gruppi americani
6 - Gruppi con più di 10 dischi
7 - Gruppi ordinati per numero di dischi
8 - Gruppo con meno dischi
9 - Conteggio gruppi per paese
10 - Verifica presenza gruppo
11 - Ricerca per parola nel nome
12 - Aggiungi gruppo
13 - Elimina gruppi di un paese
0 - Esci
""")
    
    scelta = input("Scelta: ")

    if scelta == "1":
        for g in gruppi:
            print(g)
    elif scelta == "2":
        media = sum(g['dischi'] for g in gruppi) / len(gruppi)
        print("Media dischi:", round(media, 2))
    elif scelta == "3":
        for g in gruppi:
            if g['paese'].lower() == "regno unito":
                print(g)
    elif scelta == "4":
        uk = [g for g in gruppi if g['paese'].lower() == "regno unito"]
        media = sum(g['dischi'] for g in uk) / len(uk)
        print("Media UK:", round(media, 2))
    elif scelta == "5":
        usa = [g for g in gruppi if g['paese'].lower() == "stati uniti"]
        media = sum(g['dischi'] for g in usa) / len(usa)
        print("Media USA:", round(media, 2))
    elif scelta == "6":
        for g in gruppi:
            if g['dischi'] > 10:
                print(g)
    elif scelta == "7":
        for g in sorted(gruppi, key=lambda x: x['dischi']):
            print(g)
    elif scelta == "8":
        min_g = min(gruppi, key=lambda x: x['dischi'])
        print("Gruppo con meno dischi:", min_g)
    elif scelta == "9":
        conteggio = {}
        for g in gruppi:
            paese = g['paese']
            conteggio[paese] = conteggio.get(paese, 0) + 1
        print(conteggio)
    elif scelta == "10":
        nome = input("Nome da cercare: ")
        trovato = any(g['nome'].lower() == nome.lower() for g in gruppi)
        print("Presente." if trovato else "Non presente.")
    elif scelta == "11":
        parola = input("Parola o lettera da cercare: ").lower()
        for g in gruppi:
            if parola in g['nome'].lower():
                print(g)
    elif scelta == "12":
        nome = input("Nome: ")
        dischi = int(input("Numero dischi: "))
        paese = input("Paese: ")
        gruppi.append({"nome": nome, "dischi": dischi, "paese": paese})
        with open("./file/es13_file_GroupMusic.txt", "w", encoding="utf-8") as f:
            for g in gruppi:
                f.write(f"{g['nome']},{g['dischi']},{g['paese']}\n")
        print("Gruppo aggiunto.")
    elif scelta == "13":
        paese = input("Paese da eliminare: ").lower()
        gruppi = [g for g in gruppi if g['paese'].lower() != paese]
        with open("./file/es13_file_GroupMusic.txt", "w", encoding="utf-8") as f:
            for g in gruppi:
                f.write(f"{g['nome']},{g['dischi']},{g['paese']}\n")
        print("Gruppi eliminati.")
    elif scelta == "0":
        print("Ciao!")
        break
    else:
        print("Scelta non valida.")
