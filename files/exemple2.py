"""
Afisarea continutului folderului curent si filtrarea dupa un wildcard
Listam fisierele cu extensia .py din folderul curent
"""

import glob


def main():
    # print(glob.glob('*.py'))
    lista_fisiere = glob.glob('data/*.py')
    for file in lista_fisiere:
        print(file)
    print(
        f'In folderul curent sunt {len(lista_fisiere)} fisiere cu extensia py')


if __name__ == '__main__':
    main()
