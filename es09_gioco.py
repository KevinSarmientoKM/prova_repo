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



# Inizio info giocatori
nome_giocatore1 = None
nome_giocatore2 = None

# Imposto l'input dei nomi, ma a condizione che siano diversi tra loro:
while nome_giocatore1 is None or nome_giocatore2 is None:
    nome_giocatore1 = input("Inserisci il nome del primo giocatore: ")
    nome_giocatore2 = input("Inserisci il nome del secondo giocatore: ")
    if nome_giocatore1 == nome_giocatore2:
        print("I nomi dei giocatori devono essere diversi!")
        nome_giocatore1 = None
        nome_giocatore2 = None

while True:
    # Scelte dei giocatori
    scelta_giocatore1 = None
    scelta_giocatore2 = None
#scelta giocatore 1
    while scelta_giocatore1 is None:
        scelta_giocatore1 = input(f"{nome_giocatore1}, scegli tra carta (c), forbice (f) o sasso (s): ")
        if scelta_giocatore1.lower() not in ['c', 'f', 's']: #costringo al giocatore scegliere tra carta, forbice o sasso
            print("Scelta non valida. Scegli tra carta (c), forbice (f) o sasso (s).")
            scelta_giocatore1 = None
#scelta giocatore 2 
    while scelta_giocatore2 is None:
        scelta_giocatore2 = input(f"{nome_giocatore2}, scegli tra carta (c), forbice (f) o sasso (s): ")
        if scelta_giocatore2.lower() not in ['c', 'f', 's']: #costringo al giocatore2 scegliere tra carta, forbice o sasso
            print("Scelta non valida. Scegli tra carta (c), forbice (f) o sasso (s).")
            scelta_giocatore2 = None

    # determina il vincitore tra i due
    if scelta_giocatore1 == scelta_giocatore2:
        print("Pareggio!") #caso pareggio!
    elif (scelta_giocatore1 == 'c' and scelta_giocatore2 == 's') or \
         (scelta_giocatore1 == 's' and scelta_giocatore2 == 'f') or \
         (scelta_giocatore1 == 'f' and scelta_giocatore2 == 'c'):
        print(f"{nome_giocatore1} ha vinto!")
    else:
        print(f"{nome_giocatore2} ha vinto!") 

    # chiedi ai giocatori se continuare o uscire
    uscita = input("Vuoi uscire dal programma? (s/n): ") 
    if uscita.lower() == 's':
        print("Grazie per aver giocato!")
        break #interrompo il gioco



