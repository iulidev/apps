"""
Virtual environments =  medii virtuale izolate care permit separarea proiectelor
                        prin instalarea librariilor (packages) specifice, cu
                        versiuni specifice, la nivel de proiect
Prin crearea unui mediu izolat de lucru (de dezvoltare) lucram cu librarii
specifice proiectului, versiuni specifice, fara a fi nevoie sa avem toate
librariile instalate global.

Pentru a lucra cu virtual environments trebuie instalata libraria virtualenv
pip install virtualenv

1/ Pentru a crea un mediu izolat de lucru (virtual environment):
py -m venv nume_virtual_env
ex: py -m venv mediu
sau ruland:
virtualenv nume_virtual_env
ex: virtualenv mediu2

2/ Activarea unui virtual environment
./nume_virtual_env/Scripts/activate

Se schimba promptul in format (nume_virtual_env)cale_director

3/ Dezactivarea unui virtual environment
deactivate
Promptul nu mai are intre paranteze rotunde numele virtual enviromentului.

4/ pip freeze
afiseaza modulele si versiunea intr-un format specific, outputul fiind cel 
utilizat la crearea unor fisiere de requirements (fisiere text care contin
toate librariile din proiect si versiunile acestora)

5/ Crearea unui fisier de requirements 
pip freeze > requirements.txt

6/ La clonarea sau copierea unui proiect se pot instala toate librariile cu
comanda (dupa crearea unui mediu izolat cu comanda "virtualenv envone" si
activarea acestuia cu ".\envone\Scripts\activate"):
pip install -r requirements.txt
"""
