"""
Set up a connection to a SQLite database
(conectivitatea la o baza de date SQLite)
https://www.sqlite.org/index.html
SQLite - librarie in C care implementeaza un sistem de gestiune a bazelor de
date light-weight (SQL engine disk-based)
    - baza de date este stocata pe disc (alternativ, se poate salva in memorie)
    - nu necesita un server care sa execute / proceseze interogarile
sqlite3
"""
import sqlite3

# seta o conexiune la o baza de date
con = sqlite3.connect('curs.db')
