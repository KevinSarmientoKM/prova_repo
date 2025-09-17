menu = '''
1 - L'elenco completo di tutti i paesi
2 - L'elenco dei paesi che hanno una moneta a scelta
3 - L'elenco dei paesi che sono isole 
4 - Elenco delle isole col numero di abitanti inferiore alla media totale
5 - Elenco dei paesi ordinati per popolazione
6 - Elenco dei paesi di religione a scelta
7 - La somma degli abitanti di una religione a scelta
8 - Numero dei paesi che usano la stessa moneta
0 - Esci
'''
# file:
#     paese,capitale,n_abitanti,isola,moneta,religione
#     Giappone,Tokyo,12344444444,true,Yen,Shintoismo


def leggi_file(percorso: str):
    lista = []
    with open(percorso) as file:
        intestazione = file.readline().strip().split(",")
        for riga in file:
            valori = riga.strip().split(',')
            paese = {}
            # Giappone,Tokyo,12344444444,true,Yen,Shintoismo
            paese[intestazione[0]] = valori[0]
            paese[intestazione[1]] = valori[1]
            paese[intestazione[2]] = int(valori[2])
            paese[intestazione[3]] = True if valori[3] == "True" else False
            paese[intestazione[4]] = valori[4]
            paese[intestazione[5]] = valori[5]
            lista.append(paese)
            
    return lista

def stampa(lista: list[dict]) -> str:
    ris = ""
    for diz in lista:
        # \t -> tab
        ris += f"""\tPaese: {diz["paese"]} 
- Capitale: {diz["capitale"]}
- Abitanti: {diz["n_abitanti"]}
- Isola: {"Si" if diz["isola"] == True else "No"} 
- Moneta: {diz["moneta"]}       
- Religione: {diz["religione"]}

"""
    return ris


def paesi_moneta(moneta: str, lista: list[dict]):
    lista_moneta = []
    for diz in lista:
        # Sterlinaegiziana == Sterlinaegiziana
        if diz["moneta"].replace(" ", "") == moneta.replace(" ", "").capitalize():
            lista_moneta.append(diz)
    return lista_moneta
            
lista_paesi = leggi_file("./file/paesi.csv")
    

while True:
    print(menu)
    cmd = input("Inserisci un comando: ")
    ris = ""
    match cmd:
        case "1":
            ris = stampa(lista_paesi)
        case "2":
            moneta = input("Inserisci una moneta: ").strip().capitalize()
            #ris = stampa(paesi_moneta(moneta, lista_paesi))
            lista_moneta = [paese for paese in lista_paesi if paese["moneta"].replace(" ", "") == moneta.replace(" ", "")]
            ris = stampa(lista_moneta)
        case "3":                                       
            lista_isole = [paese for paese in lista_paesi if paese["isola"]]
            ris = stampa(lista_isole)
        case "4": # 4 - Elenco delle isole col numero di abitanti inferiore alla media totale
            media = sum([paese["n_abitanti"] for paese in lista_paesi]) / len(lista_paesi)
            lista_isole_inf_media = [paese for paese in lista_paesi if paese["isola"] and paese["n_abitanti"] < media]
            #lista_isole_inf_media = [paese for paese in [paese for paese in lista_paesi if paese["isola"]] if paese["n_abitanti"] < media]
            print(f"Elenco delle isole col numero di abitanti inferiore alla media totale {round(media)}:")
            ris = stampa(lista_isole_inf_media)
        case "5":
            lista_ordinata = sorted(lista_paesi, key= lambda x: x["n_abitanti"])
            ris = stampa(lista_ordinata)
        case "6": # 6 - Elenco dei paesi di religione a scelta
            religione = input("Inserisci una religione: ").strip().capitalize()
            religioni = {paese["religione"] for paese in lista_paesi}
            if religione in religioni:
                lista_religione = [paese for paese in lista_paesi if paese["religione"].replace(" ", "") == religione.replace(" ", "")]
                ris = stampa(lista_religione)
            else:
                ris = f"Nessun paese con {religione} come religione. Riprova!"
        case "7": #La somma degli abitanti di una religione a scelta
            religione = input("Inserisci una religione: ").strip().capitalize()
            religioni = {paese["religione"] for paese in lista_paesi}
            if religione in religioni:
                somma = sum([paese["n_abitanti"] for paese in lista_paesi if paese["religione"].replace(" ", "") == religione.replace(" ", "")])
                ris = f"La somma degli abitanti di religione {religione} è: {somma}"
            else: 
                ris = f"Nessun paese con {religione} come religione. Riprova!"
        case "8": # Numero dei paesi che usano la stessa moneta
            #moneta = input("Inserisci una moneta: ").strip().capitalize()
            diz_moneta = {}
            for paese in lista_paesi:
                moneta = paese["moneta"]
                if moneta not in diz_moneta:
                    diz_moneta[moneta] = 1
                else:
                    diz_moneta[moneta] += 1
            for k,v in diz_moneta.items():
                ris += f"La moneta {k} è utilizzata da {v} {"paesi" if v > 1 else "paese"}\n"
        case "0":
            print("Ciao! A presto!")
            break
        case _:
            ris = "Errore: valore errato, riprova!"
            
    print(ris)
