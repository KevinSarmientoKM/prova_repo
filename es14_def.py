# 1 - Funzione per convertire le temperatura -> da celsius a fahrenheit e viceversa

# 2 - Funzione per analizzare un testo -> numero di parole, numero di caratteri, numero frasi

# 3 - Funzione per calcolare somma e differenza

# 4 - Funzione per validare l'età -> in base all'età dire se è maggiorenne o minorenne

# 5 - Funzione per verificare se un numero è pari

# 6 - Funzione per convertire una valuta -> importo * tasso_cambio

# 1 - Conversione temperatura
def converti_temperatura(gradi: int, scala="C"):
    if scala == "C":
        return (gradi * 9/5) + 32  # da Celsius a Fahrenheit
    elif scala == "F":
        return (gradi - 32) * 5/9  # da Fahrenheit a Celsius
    else:
        return "Scala non valida (usa 'C' o 'F')"

# 2 - Analisi del testo
def analizza_testo(testo):
    parole = testo.split()
    caratteri = len(testo)
    frasi = testo.count('.') + testo.count('!') + testo.count('?')
    return {
        "parole": len(parole),
        "caratteri": caratteri,
        "frasi": frasi
    }

# 3 - Somma e differenza
def somma_e_differenza(a, b):
    return {
        "somma": a + b,
        "differenza": a - b
    }

# 4 - Validazione età
def valida_eta(eta):
    if eta >= 18:
        return "Maggiorenne"
    else:
        return "Minorenne"

# 5 - Verifica numero pari
def è_pari(numero):
    return numero % 2 == 0

# 6 - Conversione valuta
def converti_valuta(importo, tasso_cambio):
    return importo * tasso_cambio



""""
tassi_di_cambio = {
    "EUR/USD": 1.08,
    "USD/EUR": 0.93,
    "EUR/GBP": 0.85,
    "GBP/EUR": 1.18
}
def converti_valuta(importo, da_valuta, a_valuta):
    coppia = f"{da_valuta.upper()}/{a_valuta.upper()}"
    if coppia in tassi_di_cambio:
        tasso = tassi_di_cambio[coppia]
        risultato = round(importo * tasso, 2)
        return f"{importo} {da_valuta.upper()} corrispondono a {risultato} {a_valuta.upper()}"
    else:
        return "Tasso di cambio non disponibile per questa coppia di valute."
    
print(converti_valuta(1034, "eur", "usd"))"""