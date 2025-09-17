
'''
1 - L'elenco completo di tutti i paesi
2 - L'elenco dei paesi che hanno una moneta a scelta
3 - L'elenco dei paesi che sono isole 
4 - Elenco delle isole col numero di abitanti inferiore alla media totale
5 - Elenco dei paesi ordinati per popolazione
6 - Elenco dei paesi di religione a scelta
7 - La somma degli abitanti di una religione a scelta
8 - Numero dei paesi che usano la stessa moneta
0 - Esci

file:
    paese,capitale,n_abitanti,isola,moneta,religione
    
'''

# Carica i dati
def leggi_csv(path):
    with open(path, encoding="utf-8") as file:
        righe = file.readlines()
    intestazioni = righe[0].strip().split(",")
    dati = []
    for riga in righe[1:]:
        valori = riga.strip().split(",")
        record = dict(zip(intestazioni, valori))
        # conversioni utili
        record["n_abitanti"] = int(record["n_abitanti"])
        record["isola"] = record.get("isola", "").strip().lower()
        record["moneta"] = record["moneta"].lower()
        record["religione"] = record["religione"].lower()
        dati.append(record)
    return dati

paesi = leggi_csv("./file/paesi.csv")

def mostra_menu():
    print("\n--- MENU ---")
    print("1 - Tutti i paesi")
    print("2 - Paesi con una certa moneta")
    print("3 - Paesi che sono isole")
    print("4 - Isole con meno abitanti della media")
    print("5 - Paesi ordinati per abitanti")
    print("6 - Paesi con una certa religione")
    print("7 - Somma abitanti per religione")
    print("8 - Quanti paesi usano la stessa moneta")
    print("0 - Esci")

while True:
    mostra_menu()
    scelta = input("Scegli un'opzione (0-8): ")

    match scelta:
        case "1":
            for paese in paesi:
                print(paese["paese"])

        case "2":
            moneta = input("Inserisci la moneta: ").lower()
            for paese in paesi:
                if paese["moneta"] == moneta:
                    print(paese["paese"], "-", paese["moneta"])

        case "3":
            for paese in paesi:
                if paese["isola"] == "si":
                    print(paese["paese"], "- Isola")

        case "4":
            media = sum(p["n_abitanti"] for p in paesi) / len(paesi)
            for paese in paesi:
                if paese["isola"] == "si" and paese["n_abitanti"] < media:
                    print(paese["paese"], "-", paese["n_abitanti"])

        case "5":
            ordinati = sorted(paesi, key=lambda x: x["n_abitanti"], reverse=True)
            for paese in ordinati:
                print(paese["paese"], "-", paese["n_abitanti"])

        case "6":
            religione = input("Inserisci la religione: ").lower()
            for paese in paesi:
                if paese["religione"] == religione:
                    print(paese["paese"], "-", paese["religione"])

        case "7":
            religione = input("Inserisci la religione: ").lower()
            totale = sum(p["n_abitanti"] for p in paesi if p["religione"] == religione)
            print("Totale abitanti:", totale)

        case "8":
            conteggio = {}
            for paese in paesi:
                m = paese["moneta"]
                conteggio[m] = conteggio.get(m, 0) + 1
            for moneta, count in conteggio.items():
                print(moneta, ":", count)

        case "0":
            print("Chiusura del programma.")
            break

        case _:
            print("Scelta non valida.")
