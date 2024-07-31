import json
import validazioni
import importlib
importlib.reload(validazioni)

class Rubrica:
    
    #inizializzo la classe rubrica con il costruttore init
    def __init__(self):
        self.contatti = {}
        self.nome_file = "rubrica.json"
        self.carica_contatti()

    
    #Definisco una funzione per salvare i contatti 
    def salva_contatti(self):
        
        """
        Questa funzione si occupa di salvare i contatti
        """
        with open(self.nome_file, "w") as file:
            json.dump(self.contatti, file, indent=6)
        
    
        
    
    #Definisco la funzione per il caricamento dei contatti, se presente   
    def carica_contatti(self):
        
        """
        Questa funzione si occupa di caricare i contatti all'avvio, se presente il file di rubrica
        """
        try:
            with open(self.nome_file, "r") as file:
                self.contatti = json.load(file)
            print(f"Nella rubrica sono presenti {len(self.contatti)} contatti")
        except FileNotFoundError:
            print("Nessun file trovato. Verrà creata una nuova rubrica")
        except json.JSONDecodeError:
            print("Errore nel leggere il file rubrica. Verrà creata una nuova rubrica.")
            
            
    #Definisco la funzione per l'inserimento di un contatto
    def aggiunta_contatto(self):
        
        """
        Questa funzione si occupa di aggiungere un contatto alla rubrica
        """
        
        name_surname = validazioni.input_valido("Nome Cognome", validazioni.valida_nome_cognome).title()
        if name_surname != "":
            telefono = validazioni.input_valido("Numero di Cellulare", validazioni.valida_telefono)
            self.contatti[name_surname] = telefono
            print(f"Inserimento riuscito!\n{name_surname}, {telefono}")
        else:
            print("Nome non valido.\n Inserimento non riuscito")
    
    #Definisco la funzione per la ricerca di un contatto
    def cerca_contatto(self):
        
        """
        Questa funzione si occupa di cercare un contatto dalla rubrica
        """
        
        if not self.contatti:
            print("La rubrica è vuota")
            return
        name_surname = validazioni.input_valido("Cerca contatto inserendo Nome o Cognome\nPer il dettaglio inserisci Nome e Cognome", validazioni.valida_nome_cognome).title()
        if name_surname in self.contatti:
            print(f"{name_surname}, {self.contatti[name_surname].split()}")
        else:
            print(f"{name_surname} non è presente nella rubrica.")
            partial_matches = [contact for contact in self.contatti if name_surname in contact]
            if partial_matches:
                print("Contatti simili trovati:")
                for contact in partial_matches:
                    print(f"{contact}, {self.contatti[contact]}")
     
    
    #Definisco la funzione per la modifica di un contatto
    def modifica_contatto(self):
        name_surname = validazioni.input_valido("Inserisci nome e cognome del contatto da modificare: ", validazioni.valida_nome_cognome)
        
        if name_surname not in self.contatti:
            print("Contatto non trovato.")
            return
        
        print(f"Modifica del contatto: {name_surname}")
        name_surname_new = validazioni.input_valido("Inserisci nuovo nome e cognome (Lascia vuoto se non vuoi modificarlo): ", validazioni.valida_nome_cognome).title()
        new_telefono = validazioni.input_valido("Inserisci nuovo numero (Lascia vuoto se non vuoi modificarlo): ", validazioni.valida_telefono)
        
        if name_surname_new:
            self.contatti[name_surname_new] = self.contatti.pop(name_surname)
            name_surname = name_surname_new
        if new_telefono:
            self.contatti[name_surname] = new_telefono
        
        print("Contatto modificato con successo.")
    
    
    #Definisco la funzione per l'eliminazione di un contatto
    def elimina_contatto(self):
        """
        Questa funzione si occupa di cancellare un contatto dalla rubrica
        """
        name_surname = validazioni.input_valido("Inserisci nome e cognome del contatto da eliminare: ", validazioni.valida_nome_cognome).title()
        
        if name_surname not in self.contatti:
            print("Contatto non trovato.")
            return
        
        conferma = input(f"Sei sicuro di voler eliminare il contatto {name_surname}? (s/n): ").lower()
        if conferma == 's':
            del self.contatti[name_surname]
            print(f"{name_surname} eliminato con successo")
        else:
            print("Eliminazione annullata.")
    
    
    #Definisco la funzione per la visualizzazione della rubrica
    def stampa_rubrica(self):
        
        """
        Questa funzione si occupa di visualizzare i contatti dalla rubrica in ordine crescente
        """
        if not self.contatti:
            print("La rubrica è vuota")
        else:
            for name, telefono in sorted(self.contatti.items()):
                print(f"{name}: {telefono}")

                