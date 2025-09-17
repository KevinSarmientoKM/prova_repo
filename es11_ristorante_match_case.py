piatti = [
    {'Nome': 'Brasato al barolo', 'Prezzo': 20, 'Tipo': 'Secondo'},
    {'Nome': 'Spaghetti allo scoglio', 'Prezzo': 15, 'Tipo': 'Primo'},
    {'Nome': 'Risotto ai funghi', 'Prezzo': 13, 'Tipo': 'Primo'},
    {'Nome': "Spaghetti all'Amatriciana", 'Prezzo': 9, 'Tipo': 'Primo'},
    {'Nome': 'Risotto ai frutti di mare', 'Prezzo': 18, 'Tipo': 'Primo'},
    {'Nome': 'Salamelle in umido', 'Prezzo': 12, 'Tipo': 'Secondo'},
    {'Nome': 'Carpaccio di manzo', 'Prezzo': 8, 'Tipo': 'Antipasto'},
    {'Nome': 'Gamberetti in salsa rosa', 'Prezzo': 7, 'Tipo': 'Antipasto'},
    {'Nome': 'Arrosto', 'Prezzo': 20, 'Tipo': 'Secondo'},
    {'Nome': 'Fagiolini', 'Prezzo': 2, 'Tipo': 'Contorno'}
]

categorie = ['Antipasto', 'Primo', 'Secondo', 'Contorno']

# Funzioni utili
def calcola_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

def elenco_piatti(tipo=None):
    if tipo:
        return [piatto for piatto in piatti if piatto['Tipo'].casefold() == tipo.casefold()]
    return piatti

def piatto_piu_costoso():
    return max(piatti, key=lambda piatto: piatto['Prezzo'])

def categoria_piu_ricorrente():
    frequenze = {categoria: sum(1 for piatto in piatti if piatto['Tipo'].casefold() == categoria.casefold()) for categoria in categorie}
    max_categoria = max(frequenze, key=frequenze.get)
    return max_categoria, frequenze[max_categoria]

def prezzo_medio_categoria(tipo):
    piatti_categoria = [piatto['Prezzo'] for piatto in piatti if piatto['Tipo'].casefold() == tipo.casefold()]
    return calcola_media(piatti_categoria)

# Menu interattivo
print("Benvenuto al nostro ristorante!")
while True:
    print(f"""
        ----------------------------------------------------------------------------------------
        1-Elenco piatti
        2-Costo medio piatti
        3-Elenco per categoria indicata dall'utente
        4-Prezzo medio categoria indicata dall'utente
        5-Piatto più costoso
        6-Categoria più ricorrente
        0-Esci  
        ----------------------------------------------------------------------------------------
    """)
    
    try:
        scelta_menu = int(input("Inserisci un numero da 1 a 6 per scoprire cosa abbiamo nel menù: "))
    except ValueError:
        print("Per favore, inserisci un numero valido.")
        continue
    
    match scelta_menu:
        case 1:
            print("\nEcco la lista dei nostri piatti: ")
            for piatto in elenco_piatti():
                print(f"{piatto['Nome']} - {piatto['Prezzo']}€")
        case 2:
            costo_medio = calcola_media([piatto['Prezzo'] for piatto in piatti])
            print(f"\nIl costo medio dei nostri piatti è: {costo_medio:.2f}€")
        case 3:
            scelta_categoria = input(f"Seleziona la categoria che vuoi esplorare ({', '.join(categorie)}): ").casefold()
            if scelta_categoria in [categoria.casefold() for categoria in categorie]:
                piatti_categoria = elenco_piatti(scelta_categoria)
                if piatti_categoria:
                    print("\nEcco i piatti della categoria selezionata:")
                    for piatto in piatti_categoria:
                        print(f"{piatto['Nome']} - {piatto['Prezzo']}€")
                else:
                    print("Nessun piatto trovato per questa categoria.")
            else:
                print("Categoria non valida.")
        case 4:
            scelta_categoria_prezzo = input(f"Seleziona la categoria per cui vuoi sapere il prezzo medio ({', '.join(categorie)}): ").casefold()
            if scelta_categoria_prezzo in [categoria.casefold() for categoria in categorie]:
                prezzo_medio = prezzo_medio_categoria(scelta_categoria_prezzo)
                print(f"\nIl prezzo medio per la categoria {scelta_categoria_prezzo.capitalize()} è: {prezzo_medio:.2f}€")
            else:
                print("Categoria non valida.")
        case 5:
            piatto_costoso = piatto_piu_costoso()
            print(f"\nIl nostro piatto più costoso è {piatto_costoso['Nome']} con un prezzo di {piatto_costoso['Prezzo']}€")
        case 6:
            categoria_ricorrente, frequenza = categoria_piu_ricorrente()
            print(f"\nLa categoria più ricorrente è {categoria_ricorrente} con {frequenza} piatti.")
        case 0:
            print("\nGrazie per averci scelto! Arrivederci!")
            break
        case _:
            print("Opzione non valida, riprova.")
                        