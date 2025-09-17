# Scrivi un programma che determina chi è idoneo a donare il sangue. 
# Per poter donare, è necessario soddisfare i seguenti requisiti: 
# essere maggiorenni, non fare uso di sostanze stupefacenti e 
# non aver fatto un tatuaggio nei sei mesi precedenti alla donazione. 
# Alla fine del programma, comunica all'utente se può o non può donare il sangue.

#se non e idione allora lo mandiamo via

print("Benvenuto nel programma di donazione di sangue!")

# Richiediamo il nome, cognome e età dell'utente
nome = input("inserisci il tuo nome: ").casefold().strip()
cognome = input("inserisci il tuo cognome: ").casefold().strip()

# Richiediamo l'età dell'utente
eta = int(input("Inserisci la tua età: ").strip())

# Richiediamo se l'utente fa uso di sostanze stupefacenti
uso_stupefacenti = input("Fai uso di sostanze stupefacenti ?:  ").casefold().strip()

# Richiediamo se l'utente ha fatto un tatuaggio nei sei mesi precedenti alla donazione
tatuaggio = input("Hai fatto un tatuaggio nei sei mesi precedenti alla donazione? (si/no): ").casefold()

# Verifichiamo se l'utente è idoneo

if eta >= 18 and uso_stupefacenti.lower() != "si" and tatuaggio.lower() != "si":
    print("Puoi donare il sangue!")
    print("Contattare un medico per ulteriori consulenze.")
    print("Grazie per la tua attenzione!")

else:
    print("Non puoi donare il sangue!")
    print("Contattare un medico per ulteriori consulenze.")
    print("Grazie per la tua attenzione!")

