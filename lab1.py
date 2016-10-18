from task_1 import get_xml
from task_3 import get_products
from lxml.etree import tostring

stejka_xml = get_xml()
with open('stejka.xml', 'w') as xml_file:
    xml_file.write(tostring(stejka_xml, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

hyperlinks = stejka_xml.xpath('//*[contains(@type, "hyperlink")]/text()')
for link in hyperlinks:
    print link

mebli_lviv_xml = get_products()
with open('mebli_lviv.xml', 'w') as xml_file:
    xml_file.write(tostring(mebli_lviv_xml, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
