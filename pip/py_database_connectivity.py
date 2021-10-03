"""
Python database connectivity
Database (baza de date)     = colectie organizata de date
Tipuri de baza de date:
1/ Baza de date relationala (SQL) - Relational Database
2/ Baza de date non-SQL - non relational Database
SQL - Structured Query Language - limbaj de interogare a datelor
intr-un sistem de gestiune a bazelor de date
https://ro.wikipedia.org/wiki/SQL
DBMS (Database Management System) - sistem de gestiune a bazelor
de date = software care permite administrarea bazelor de date,
manipularea datelor din baze de date
https://ro.wikipedia.org/wiki/Sistem_de_gestiune_a_bazelor_de_date
CRUD - Create, Read, Update, Delete
Python are librarii dedicate pentru conectivitatea la baze de date
din diferite DBMS

SQLite  - Python are o librarie sqlite3 care opereaza cu baze de
date SQLite (un sistem de gestiune a bazelor de date, stocate pe
disc sau in memorie, care nu necesita un server pentru procesarea
queries/interogarilor)
sqlite3 - inclus in libraria standard, nu necesita instalare cu pip
https://docs.python.org/3/library/sqlite3.html
MySQL - Python permite conectivitatea la baze date MySQL cu libraria
mysql-connector-python
https://pypi.org/project/mysql-connector-python/
PostgreSQL - psycopg2 - librarie specifica pentru lucrul cu baze date
https://pypi.org/project/psycopg2/
"""