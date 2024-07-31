import functions
import validazioni

def input_con_prompt(prompt):
    """Richiede input all'utente con un prompt."""
    return input(f"{prompt}: ").strip()

def main():
    rubrica = functions.Rubrica()
    operazioni = {
        "i": ("Inserimento", rubrica.aggiunta_contatto),
        "r": ("Ricerca", rubrica.cerca_contatto),
        "v": ("Visualizza", rubrica.stampa_rubrica),
        "e": ("Elimina", rubrica.elimina_contatto),
        "m": ("Modifica", rubrica.modifica_contatto),
    }

    try:
        while True:
            opzioni = " - ".join(f"{k}={v[0]}" for k, v in operazioni.items())
            op = input_con_prompt(f"Operazione ({opzioni} - q=esci)")
            
            if op == "q":
                break
            elif op in operazioni:
                operazioni[op][1]()
            else:
                print("Operazione non valida")
                
            input("\nPremi INVIO per continuare...")
    finally:
        # Questo blocco verrà eseguito sempre, sia in caso di uscita normale che in caso di eccezione
        rubrica.salva_contatti()
        print("Contatti salvati.\nGrazie per aver usato la rubrica!")
    
        
if __name__ == "__main__":
    main()