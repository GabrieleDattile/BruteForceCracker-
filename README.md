# Brute Force

Questo è un progetto di brute force che tenta di craccare le password di un sito web usando una lista di password comuni.

## Autore

Gabriele D'Attile

## Github

https://github.com/GabrieleDattile

## Requisiti

Per eseguire questo progetto, hai bisogno di:

- Python 3
- requests
- threading
- time
- sys

## Installazione

Per installare le dipendenze, puoi usare il comando:

`pip install -r requirements.txt`

## Uso

Per usare questo progetto, devi modificare il file `bruteforce.py` e inserire l'URL del sito web da attaccare, il nome utente da usare e il messaggio di errore che appare quando la password è sbagliata. Poi, devi eseguire il file con il comando:

`python bruteforce.py`

Il programma proverà tutte le password presenti nel file `passwords.txt` e ti mostrerà se ne trova una valida.

# Brute Force Cracker in Rust

Questo progetto implementa un semplice cracker di password brute force in Rust.

## Requisiti

- Rust 1.54.0 o versioni successive
- Libreria `reqwest`

## Installazione

1. Installa Rust sul tuo sistema. Puoi scaricarlo dal sito ufficiale di Rust.
2. Clona questo repository sul tuo sistema locale.
3. Naviga nella directory del progetto e installa le dipendenze con `cargo build`.

## Utilizzo

Esegui il programma con `cargo run`. Il programma proverà una serie di password e stamperà l'username e la password se trova una corrispondenza.
