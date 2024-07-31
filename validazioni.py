# validazioni.py

def valida_nome_cognome(input_str):
    """
    Verifica se l'input contiene solo lettere e spazi.
    Restituisce True se valido, False altrimenti.
    """
    return all(char.isalpha() or char.isspace() for char in input_str) and input_str.strip()

def valida_telefono(input_str):
    """
    Verifica se l'input contiene solo numeri e caratteri speciali consentiti.
    Restituisce True se valido, False altrimenti.
    """
    caratteri_consentiti = frozenset("0123456789+")
    return all(char in caratteri_consentiti for char in input_str)

def input_valido(prompt, validazione_func):
    """
    Richiede input all'utente e lo valida usando la funzione di validazione fornita.
    Continua a richiedere l'input finché non è valido.
    """
    while True:
        user_input = input(f"{prompt}: ").strip()
        if validazione_func(user_input):
            return user_input
        else:
            print("Input non valido. Riprova")