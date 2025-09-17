# V1
lista_nomi = ['Brasato al barolo', 'Spaghetti allo scoglio', 'Risotto ai funghi', "Spaghetti all'Amatriciana", 'Risotto ai frutti di mare', 'Salamelle in umido', 'Carpaccio di manzo', 'Gamberetti in salsa rosa', 'Arrosto', 'Fagiolini']
lista_prezzi = ['20', '15', '13', '9', '18', '12', '8', '7', '20', '2']
lista_tipi = ['Secondo', 'Primo', 'Primo', 'Primo', 'Primo', 'Secondo', 'Antipasto', 'Antipasto', 'Secondo', 'Contorno']

# V2
lista_piatti = [['Brasato al barolo', 20, 'Secondo'], ['Spaghetti allo scoglio', 15, 'Primo'], ['Risotto ai funghi', 13, 'Primo'], ["Spaghetti all'Amatriciana", 9, 'Primo'], ['Risotto ai frutti di mare', 18, 'Primo'], ['Salamelle in umido', 12, 'Secondo'], ['Carpaccio di manzo', 8, 'Antipasto'], ['Gamberetti in salsa rosa', 7, 'Antipasto'], ['Arrosto', 20, 'Secondo'], ['Fagiolini', 2, 'Contorno']]

# v3
piatti = [{'Nome': 'Brasato al barolo', 'Prezzo': 20, 'Tipo': 'Secondo'}, {'Nome': 'Spaghetti allo scoglio', 'Prezzo': 15, 'Tipo': 'Primo'}, {'Nome': 'Risotto ai funghi', 'Prezzo': 13, 'Tipo': 'Primo'}, {'Nome': "Spaghetti all'Amatriciana", 'Prezzo': 9, 'Tipo': 'Primo'}, {'Nome': 'Risotto ai frutti di mare', 'Prezzo': 18, 'Tipo': 'Primo'}, {'Nome': 'Salamelle in umido', 'Prezzo': 12, 'Tipo': 'Secondo'}, {'Nome': 'Carpaccio di manzo', 'Prezzo': 8, 'Tipo': 'Antipasto'}, {'Nome': 'Gamberetti in salsa rosa', 'Prezzo': 7, 'Tipo': 'Antipasto'}, {'Nome': 'Arrosto', 'Prezzo': 20, 'Tipo': 'Secondo'}, {'Nome': 'Fagiolini', 'Prezzo': 2, 'Tipo': 'Contorno'}]

""" 
1-Elenco piatti
2-Costo medio piatti
3-Elenco per categoria indicata dall'utente
4-Prezzo medio categoria indicata dall'utente
5-Piatto più costoso
6-Categoria più ricorrente
0-Esci   
"""


lista_piatti = [
    ['Brasato al barolo', '20', 'Secondo'],
    ['Spaghetti allo scoglio', '15', 'Primo'],
    ['Risotto ai funghi', '13', 'Primo'],
    ["Spaghetti all'Amatriciana", '9', 'Primo'],
    ['Risotto ai frutti di mare', '18', 'Primo'],
    ['Salamelle in umido', '12', 'Secondo'],
    ['Carpaccio di manzo', '8', 'Antipasto'],
    ['Gamberetti in salsa rosa', '7', 'Antipasto'],
    ['Arrosto', '20', 'Secondo'],
    ['Fagiolini', '2', 'Contorno']
]

while True:
    print("\n1 - Elenco piatti")
    print("2 - Costo medio piatti")
    print("3 - Elenco per categoria" )
    print("4 - Prezzo medio categoria")
    print("5 - Piatto più costoso")
    print("6 - Categoria più ricorrente")
    print("0 - Esci")

    try:
        scelta = int(input("Scelta: "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if scelta == 0:
        print("Uscita dal programma.")
        break

    elif scelta == 1:
        for i in range(len(lista_piatti)):
            print(f"{i+1}. {lista_piatti[i][0]} - Prezzo: €{lista_piatti[i][1]} - Tipo: {lista_piatti[i][2]}")
    elif scelta == 2:
        costo_medio = sum(float(piatto[1]) for piatto in lista_piatti) / len(lista_piatti)
        print(f"Costo medio: €{costo_medio:.2f}")
    elif scelta == 3:
        categoria = input("Inserisci la categoria [Primo/Secondo/Antipasto/Contorno]: ").capitalize()
        trovati = False
        print(f"\nPiatti per la categoria '{categoria}':")
        for i in range(len(lista_piatti)):
            if lista_piatti[i][2] == categoria:
                print(f"{i+1}. {lista_piatti[i][0]} - Prezzo: €{lista_piatti[i][1]}")
                trovati = True
        if not trovati:
            print("Nessun piatto trovato in questa categoria.")

    elif scelta == 4:
        categoria = input("Inserisci la categoria: ").capitalize()
        piatti_categoria = [piatto for piatto in lista_piatti if piatto[2] == categoria]
        if piatti_categoria:
            costo_medio_categoria = sum(float(piatto[1]) for piatto in piatti_categoria) / len(piatti_categoria)
            print(f"Prezzo medio per la categoria '{categoria}': €{costo_medio_categoria:.2f}")
        else:
            print(f"Nessun piatto presente nella categoria '{categoria}'.")
    elif scelta == 5:
        piatto_costoso = max(lista_piatti, key=lambda piatto: float(piatto[1]))
        print(f"\nPiatto più costoso: {piatto_costoso[0]} - Prezzo: €{piatto_costoso[1]}")
    elif scelta == 6:
        from collections import Counter
        categorie = [piatto[2] for piatto in lista_piatti]
        categoria_ricorrente = Counter(categorie).most_common(1)[0]
        print(f"\nCategoria più ricorrente: {categoria_ricorrente[0]} ({categoria_ricorrente[1]} piatti)")
    else:
        print("Scelta non valida.")