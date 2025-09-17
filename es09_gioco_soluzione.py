'''
Scrivi un programma che permetta a due giocatori di sfidarsi in un gioco di "Carta, Forbice, Sasso".
Il programma deve svolgere le seguenti operazioni:

Chiedere all'utente di inserire il nome del primo giocatore e il nome del secondo giocatore.
chiedere al primo giocatore di scegliere tra carta (c), forbice (f) o sasso (s) fino a quando non viene inserita una scelta valida.
chiedere al secondo giocatore di fare lo stesso fino a quando non viene inserita una scelta valida.
Determinare il vincitore basandosi sulle scelte dei giocatori secondo le seguenti regole:
Carta batte sasso
Forbice batte carta
Sasso batte forbice
Stampare il nome del vincitore e il messaggio relativo alla combinazione delle scelte (ad esempio, "Carta batte sasso").
Se entrambi i giocatori scelgono lo stesso simbolo, stampare "Pareggio".
Gestire correttamente le situazioni in cui un giocatore inserisce una scelta non valida (non c, f o s).
Far giocare i giocatori finchè non decidono di uscire dal programma
'''

nome_g1 = input("Inserisci il nome del primo giocatore: ").capitalize()

while True:
    nome_g2 = input("Inserisci il nome del secondo giocatore: ").capitalize()
    if nome_g1 != nome_g2:
        break
    else:
        print("Il nome inserito è già stato utilizzato, riprova!")


vittorie_g1 = 0
vittorie_g2 = 0
pareggi = 0
partite = 0

valori_gioco = ["Carta","Forbice","Sasso"]

continua = "s"

while continua == "s":
    partite += 1
    print("\nRound:", partite)
    
    scelta1 = ""
    scelta2 = ""
    
    while scelta1 not in valori_gioco:
        scelta1 = input(f"{nome_g1} scegli Carta | Forbice | Sasso: ").strip().capitalize()
        if scelta1 not in valori_gioco:
            print("Scelta non valida, riprova")
        
    while scelta2 not in valori_gioco:
        scelta2 = input(f"{nome_g2} scegli scegli Carta | Forbice | Sasso: ").strip().capitalize()
        if scelta2 not in valori_gioco:
            print("Scelta non valida, riprova")
            
    if scelta1 == scelta2:
        print("Pareggio")
        pareggi += 1
    elif (scelta1 == "Carta" and scelta2 == "Sasso") or (scelta1 == "Forbice" and scelta2 == "Carta") or (scelta1 == "Sasso" and scelta2 == "Forbice"):
        print(f"CONGRATULAZIONI {nome_g1}! {scelta1} batte {scelta2}")
        vittorie_g1 += 1
    else:
        print(f"CONGRATULAZIONI {nome_g2}! {scelta2} batte {scelta1}")
        vittorie_g2 += 1
        
        
    while True:
        print()
        continua = input("Vuoi continuare? (s/n): ").casefold()
        if continua == "s" or continua == "n":
            break
        else:
            print("Valore non valido, riprova")
        

win1 = "vittoria" if vittorie_g1 == 1 else "vittorie"
win2 = "vittoria" if vittorie_g2 == 1 else "vittorie"
par = "pareggio" if pareggi == 1 else "pareggi"

print("-" * 30) 
print("Risultati finali:")
print(f"{pareggi} {par}")
print(f"{nome_g1}: {vittorie_g1} {win1}")
print(f"{nome_g2}: {vittorie_g2} {win2}")
print("-" * 30)

if vittorie_g1 > vittorie_g2:
    print(f"Ha vinto {nome_g1}")
elif vittorie_g2 > vittorie_g1:
    print(f"Ha vinto {nome_g2}")
else:
    print("Pareggio nel totale delle vittorie") 