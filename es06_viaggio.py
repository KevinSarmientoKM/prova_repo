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


def calcola_prezzo_biglietto(num_persone, eta_inferiore_14, eta_superiore_65, num_bagagli, destinazione, mese_partenza):
    # Calcola il prezzo base del biglietto
    match destinazione:
        case "Europa":
            prezzo_base = 100
        case "Africa":
            prezzo_base = 150
        case "Asia":
            prezzo_base = 250
        case "America":
            prezzo_base = 400
        case "Altri continenti":
            prezzo_base = 600
        case _:
            print("Destinazione non valida.")
            

    # Calcola gli sconti
    sconto_eta_inferiore_14 = eta_inferiore_14 * 0.15
    sconto_eta_superiore_65 = eta_superiore_65 * 0.10

    # Calcola il prezzo del biglietto
    prezzo_biglietto = prezzo_base - sconto_eta_inferiore_14 - sconto_eta_superiore_65

    # Calcola il sovrapprezzo per il mese di partenza
    match mese_partenza:
        case "Febbraio" | "Novembre":
            sovrapprezzo = 0.20
        case "Gennaio" | "Dicembre":
            sovrapprezzo = 0.30
        case "Giugno" | "Luglio" | "Agosto" :
            sovrapprezzo = 0.50
        case _:
            sovrapprezzo = 0

    # Calcola il prezzo del biglietto per gruppo
    prezzo_biglietto_gruppo = prezzo_biglietto * num_persone * (1 + sovrapprezzo) + num_bagagli * 20

    print(prezzo_biglietto_gruppo)

def stampa_risultati(prezzo_biglietto_gruppo, prezzo_biglietto):
    print(f"Costo totale del gruppo: {prezzo_biglietto_gruppo} euro")
    print(f"Costo del biglietto per un adulto: {prezzo_biglietto} euro")

# Input utente
num_persone = int(input("Inserisci il numero totale di persone: "))
eta_inferiore_14 = int(input("Inserisci il numero di persone con età inferiore a 14 anni: "))
eta_superiore_65 = int(input("Inserisci il numero di persone con età superiore a 65 anni: "))
num_bagagli = int(input("Inserisci il numero di bagagli da stiva registrati: "))
destinazione = input("Inserisci la destinazione del viaggio (Europa, Africa, Asia, America, Altri continenti): ").strip().casefold()
mese_partenza = input("Inserisci il mese di partenza: ").strip().casefold()

prezzo_biglietto_gruppo = calcola_prezzo_biglietto(num_persone, eta_inferiore_14, eta_superiore_65, num_bagagli, destinazione, mese_partenza)



if prezzo_biglietto_gruppo is not None:
    stampa_risultati(prezzo_biglietto_gruppo, prezzo_biglietto_gruppo / num_persone)

print(f"Il costo totale del gruppo: {prezzo_biglietto_gruppo}")
print(f"il costo del biglietto per una persona sotto i 14 anni: {eta_inferiore_14}")
print(f"Il costo del biglietto per una persona sopra i 65 anni: {eta_superiore_65}")
print(f"Il numero di bagagli da stiva registrati: {num_bagagli}")
