from task_1 import get_xml
from lxml.etree import tostring

xml = get_xml()
with open('stejka.xml', 'w') as xml_file:
    xml_file.write(tostring(get_xml(), pretty_print=True, xml_declaration=True, encoding='UTF-8'))

hyperlinks = xml.xpath('//*[contains(@type, "hyperlink")]/text()')
for link in hyperlinks:
    print link
