from xml.etree import ElementTree

art = ElementTree.parse('Artikelen.xml')

artikelen = art.findall('artikel/naam')

for a in artikelen:
    print(a.text)