# Scrivi un programma che determina chi è idoneo a donare il sangue. 
# Per poter donare, è necessario soddisfare i seguenti requisiti: 
# essere maggiorenni, non fare uso di sostanze stupefacenti e 
# non aver fatto un tatuaggio nei sei mesi precedenti alla donazione. 
# Alla fine del programma, comunica all'utente se può o non può donare il sangue.


eta = int (input ("eta :"))

esito = False

if eta >= 18 :
    sost_stup = input("Fai uso di sostanze stupefacenti ?: (si/no)\n ").casefold().strip()
    if not sost_stup :
        tatuaggio = input("Hai fatto un tatuaggio nei sei mesi precedenti alla donazione? (si/no)\n ").casefold().strip() == "si"
        if not tatuaggio :
            esito = True

print(f"Dal controllo risulta che {"sei idoneo" if esito else "non sei "} idoneo")

