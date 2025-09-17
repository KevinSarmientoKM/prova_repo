'''
Calcolatore del Prezzo del Biglietto Aereo

Scrivi un programma che calcoli diverse informazioni relative al prezzo del biglietto aereo.

Chiediamo le seguenti informazioni all'utente:

Il numero totale di persone per il viaggio.
Quanti tra queste persone hanno un'età inferiore a 14 anni e quante hanno un'età superiore ai 65 anni.
Quanti bagagli da stiva devono essere registrati.
La destinazione del viaggio (il continente).
Il mese di partenza.


Il prezzo del biglietto si calcola nel seguente modo:
A seconda della destinazione, il prezzo di partenza per persona varia:
Europa: 100 euro.
Africa: 150 euro.
Asia: 250 euro.
America: 400 euro.
Altri continenti: 600 euro.

A seconda dell'età, si applica uno sconto al prezzo del biglietto:
Le persone sotto i 14 anni ricevono uno sconto del 15%.
Le persone sopra i 65 anni ricevono uno sconto del 10%.

A seconda del mese di partenza, si applica un sovrapprezzo al prezzo del gruppo:
Febbraio e Novembre: 20% in più.
Gennaio e Dicembre: 30% in più.
Giugno, Luglio e Agosto: 50% in più.

Per ogni bagaglio da stiva registrato, viene aggiunto un sovrapprezzo di 20 euro al prezzo del gruppo.

In output, desideriamo ottenere le seguenti informazioni:
Il costo totale del gruppo.
Il costo del biglietto per un adulto.
Il costo del biglietto per una persona sotto i 14 anni.
Il costo del biglietto per una persona sopra i 65 anni.
Il numero di bagagli da stiva registrati e il costo.
'''

print("Benvenuto nel portale di acquisto biglietto aereo!")
#chiediamo al utente le seguenti info :
num_persone = int(input("Inserisci il numero totale di persone per il viaggio: "))

#exit() esce dal programma 
if num_persone <= 0:
    print("Dati non validi - numero di persone non può essere negativo o zero.")
    exit()
    #se l utente mette negativi allora la funzione exit() fa si che il programma sia terminato se non sono soddisfate i requisiti 

#per gli under 14
n_u14 = int(input("Inserisci il numero di persone sotto i 14 anni: "))

#per gli over 65
n_o65 = int(input("Inserisci il numero di persone sopra i 65 anni: "))

n_adulti = num_persone - n_u14 - n_o65 #calcolo il numero di adulti presenti sottraendo gli under14\over65

#impongo il controllo cosi: se i gruppi sono minori di zero impongo l uscita forzata
if n_adulti < 0 or n_u14 < 0 or n_o65 < 0:
    print("Dati non validi - numero di persone non può essere negativo o zero.")
    exit()

n_bagagli = int(input("Inserisci il numero di bagagli da stiva registrati: "))

if n_bagagli < 0:
    print("Dati non validi - numero di bagagli non può essere negativo o zero")
    exit()

#tassa sui bagali da stiva al pezzo!
TASSA_BAGAGLIO =20 #E UNA COSTANTE

costo_bagagli = n_bagagli * TASSA_BAGAGLIO

destinazione = input("Inserisci la destinazione del viaggio (Europa, Africa, Asia, America, Altri continenti): ").strip().casefold()
#inserisci il mese di partenza
mese = input("Inserisci il mese di partenza: ").strip().casefold()

#creeremo il match case per i continenti 
"""Il prezzo del biglietto si calcola nel seguente modo:
A seconda della destinazione, il prezzo di partenza per persona varia:
Europa: 100 euro.
Africa: 150 euro.
Asia: 250 euro.
America: 400 euro.
Altri continenti: 600 euro."""
match destinazione:
    case "europa":
        prezzo_adulto = 100
    case "africa":
        prezzo_adulto = 150
    case "asia":
        prezzo_adulto = 250
    case "america":
        prezzo_adulto = 400
    case  _:
        prezzo_adulto = 600
    
#ora gestiamo i prezzi per gli under14 e gli over65
#calcolato in vari modo tenendo conto che gli under14 e del 15% e over65 e del 10%
#prezzo_u14 = prezzo_adulto - (prezzo_adulto / 100 * 15)
#prezzo_u14 = prezzo_adulto - (prezzo_adulto * 0.15)

prezzo_u14 = prezzo_adulto * 0.85

prezzo_o65 = prezzo_adulto * 0.90

#ora vediamo i costi totale 
costo_totale_adulti = n_adulti * prezzo_adulto
#costo tot delle persone presenti under14
costo_totale_u14 = n_u14 * prezzo_u14

#costo tot delle persone presenti over65
costo_totale_o65 = n_o65 * prezzo_o65

#imponiamo poi il costo totale del gruppo
costo_totale_gruppo = costo_totale_adulti + costo_totale_u14 + costo_totale_o65  

#ora gestiamo i mesi dei rispettivi prezzi 

if mese == "febbraio" or mese == "novembre":
    costo_totale_gruppo *= 1.2 #e come scrivere [costo_totale_gruppo  = costo_totale_gruppo * 1.2] | oppure costo_totale_gruppo  = costo_totale_gruppo + (costo_totale_gruppo / 100 * 20)
elif mese == "gennaio" or mese == "dicembre":
    costo_totale_gruppo *= 1.3
elif mese == "giugno" or mese == "luglio" or mese == "agosto":
    costo_totale_gruppo *= 1.5

costo_totale_gruppo += costo_bagagli #aggiungo il costo dei bagagli al prezzo del gruppo

"""In output, desideriamo ottenere le seguenti informazioni:
Il costo totale del gruppo.
Il costo del biglietto per un adulto.
Il costo del biglietto per una persona sotto i 14 anni.
Il costo del biglietto per una persona sopra i 65 anni.
Il numero di bagagli da stiva registrati e il costo."""

print(""" 
Il costo totale del gruppo è {costo_totale_gruppo} euro
Il costo del biglietto per un adulto è: {prezzo_adulto} euro
Il costo del biglietto per una persona sotto i 14 anni è : {prezzo_u14} euro
Il costo del biglietto per una persona sopra i 65 anni è : {prezzo_o65} euro
Il numero di bagagli da stiva registrati è {n_bagagli} | Costo : {costo_bagagli} euro
""")




