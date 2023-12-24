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
