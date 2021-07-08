"""
XML file (Fisier XML)
XML     - eXtensible Markup Language
        - format de interschimbare a datelor in care informatia este
        organizata ierarhic, intr-un arbore (tree) cu elemente caracterizate
        de un tag (eticheta) si atribute.
        - are un root (radacina)
Modulul xml permite prelucrarea fisierelor XML
Un obiect din clasa ElementTree este intreg documentul XML
Elementele sunt de tipul xml.etree.ElementTree.Element
"""
from xml.etree import ElementTree

tree = ElementTree.parse('data/countries.xml')
print(type(tree))
root = tree.getroot()
# print(type(root))   # xml.etree.ElementTree.Element
print(f'Elementul root: {root} {root.tag}')
country_elements = tree.findall("country")  # lista elementelor
print(f'Lista de elemente de tip country: {country_elements} ')
for element in country_elements:
    # print(element)
    print(f'Tag: {element.tag}')
    print(f'Atribute: {element.attrib}')
    print(element.attrib['name'], end=' ')
    year = element.find('year')     # returneaza primul Element gasit
    print(f'Anul: {year.text}')

