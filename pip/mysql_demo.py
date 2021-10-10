"""
Set up a connection to a MySQL database
MySQL   - pentru setare conexiune:
    - libraria Python mysql-connector-python
    https://pypi.org/project/mysql-connector-python/
    pip install mysql-connector-python

    - server MySQL care sa ruleze in background si trebuie
    in prealabil instalat
    Instalarea in windows se realizeaza cu MySQL Installer for Windows
    https://www.mysql.com/
    Arhitectura MySQL, platforme (SO):
    https://www.mysql.com/support/supportedplatforms/database.html

    Manual MySQL 5.7:
    https://dev.mysql.com/doc/refman/5.7/en/

    Instructiuni instalare MySQL Installer
    Windows
    https://dev.mysql.com/doc/refman/5.7/en/windows-installation.html
    Linux
    https://dev.mysql.com/doc/refman/5.7/en/linux-installation.html
    Link installer:
    https://dev.mysql.com/downloads/installer/
    Link instalare Linux, apt install:
    https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#apt-repo-fresh-install
    
    Comenzi instalare mysql in Linux Mint / Ubuntu (in terminal):
    - dezinstalare versiuni anterioare
    sudo apt-get remove --purge mysql-\*
    sudo apt-get purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*
    sudo rm -rf /etc/mysql /var/lib/mysql
    sudo apt-get autoremove
    sudo apt-get autoclean
    - instalare mysql-server
    Link: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04
    sudo apt update
    sudo apt install mysql-server

    
    sudo apt-get install mysql-server
        Dupa instalare, securizare instalare 
            sudo mysql_secure_installation
        si verificare stare mysql server
            sudo systemctl status mysql
        sau
            sudo service mysql status
    Schimbare auth_plugin pentru a folosi "mysql_native_password":
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'pythonD77_'
    Creare alt user, de exp pentru a crea iulian:
    CREATE USER 'iulian'@'localhost' IDENTIFIED WITH mysql_native_password BY 'pydev';
    GRANT PRIVILEGE ON database.table TO 'username'@'host';
        GRANT PRIVILEGE ON *.* TO 'iulian'@'localhost';
        GRANT PRIVILEGE ON *.* TO 'iulian'@'localhost' WITH GRANT OPTION;
        FLUSH PRIVILEGES;
     
    Instalare mariadb (MariaDB server):
    sudo apt-get install mariadb-client mariadb-server -y
    Tutorial MySQL:
    https://dev.mysql.com/doc/refman/8.0/en/tutorial.html
    MySQL data types:
    https://dev.mysql.com/doc/refman/8.0/en/data-types.html
"""
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pythonD77_",
    database="dbtest"
)
cursor = con.cursor()
print('Citim informatiile din baza de date inainte de inserare')
cursor.execute("SELECT * FROM produse")
results = cursor.fetchall()
print(results)
fruct = 'smochine'
pret = 27
dict = {
    'visine': 7,
    'piersici': 20,
    'prune': 5
}
# cursor.execute("""INSERT INTO produse(nume, pret) VALUES('cirese', 12)""")
cursor.execute(
    """INSERT INTO produse(nume, pret) VALUES(%s, %s)""", (fruct, pret))
for fruct, pret in dict.items():
    cursor.execute(
        """INSERT INTO produse(nume, pret) VALUES(%s, %s)""", (fruct, pret))
con.commit()
print('Liniile din tabela dupa inserare linie noua')
cursor.execute("SELECT * FROM produse")
results = cursor.fetchall()
# print(results)
for row in results:
    print(row)
con.commit()
con.close()
