# Scriviamo un programma che calcoli il prezzo di un biglietto per il cinema
# Chiediamo all'utente la sua età, il comune di residenza e il lavoro svolto
# Se l'utente è residente a Como, il prezzo del biglietto è 0
# Se l'utente è minorenne il prezzo del biglietto viene scontato di 3€
# Se l'utente ha più di 70 anni, il prezzo del biglietto viene scontato di 5€
# Se l'utente è uno studente o un docente, il biglietto viene scontato di altri 2€
# Di base, il biglietto costa 10€



# Chiediamo all'utente la sua età, il comune di residenza e il lavoro svolto
print("Benvenuto nel portale di acquisto biglietto di COMO_Cinema!")
eta = int(input("Inserisci la tua età: "))
comune = input("Inserisci il tuo comune di residenza: ").casefold()
lavoro = input("Inserisci il tuo lavoro: ").casefold()

# Definiamo le scontazioni per età, comune e lavoro
prezzo_base = 10
sconto_eta_stud = 3
sconto_eta_anz = 5
sconto_lavoro = 2
sconto_comune = 10
#sconto in base al eta 
if eta < 18:
    sconto_eta = prezzo_base - sconto_eta_stud
if eta > 70:
    sconto_eta = prezzo_base - sconto_eta_anz
#------------------------------------
#sconto in base al lavoro
if lavoro == "studente" or lavoro == "docente":
    sconto_lavoro = prezzo_base - sconto_lavoro
#-----------------------------------
#sconto in base al comune
if comune == "como" :
    sconto_comune = prezzo_base - sconto_comune
#-----------------------------------
# Calcoliamo il prezzo finale del biglietto
sconto_finale = prezzo_base - (sconto_eta + sconto_comune + sconto_lavoro)


# Stampiamo il prezzo finale
print(f"Il prezzo del biglietto è: {sconto_finale}€")
print("Grazie per aver scelto il nostro cinema!")
print("Buona visione!")



