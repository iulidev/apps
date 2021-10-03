"""
pip     - package installer pentru limbajul Python
        - tool care permite instalarea, dezinstalarea si managementul
        librariilor (modulelor) Python
Documentatie oficiala: https://pypi.org/project/pip/
Lista (index) de librarii: https://pypi.org/
Documentatie oficiala Python: https://docs.python.org/3/installing/index.html

Comenzi pip:
1/  pip --version
    pip -V
    afiseaza versiunea package installerului

2/  pip install nume_pachet
    pip install numpy
    - instalarea unei librarii

3/  pip install nume_pachet --upgrade
    pip install nume_pachet -U
    - upgrade-ul unei librarii (actualizarea la ultima versiune)

4/  pip list
    - afisarea listei de librarii instalate

5/  utilizarea efectiva a unei librarii
    import nume_librarie
    import nume_librarie as nume

    import numpy
    import numpy as np

6/ pip uninstall nume_librarie

"""

import camelcase
