from lxml import etree as ET
from lib.product import Product


class XML:
    def __init__(self):
        pass

    def write2file(self, products = []):
        root = ET.Element('Toys')

        for product in products:
            level1 = ET.SubElement(root, 'Toy')
            main = ET.SubElement(level1, 'Id')
            main.text = str(product.id);
            main = ET.SubElement(level1, 'Name')
            main.text = str(product.name)
            main = ET.SubElement(level1, 'Address')
            main.text = str(product.address)

        tree = ET.ElementTree(root)
        tree.write('output.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")