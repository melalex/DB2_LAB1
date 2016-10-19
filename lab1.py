import settings

from task_1 import get_xml
from task_3 import get_products
from task_4 import transform_to_xhtml
from lxml.etree import tostring

stejka_xml = get_xml()
with open(settings.BASE_PAGE_XML, 'w') as xml_file:
    xml_file.write(tostring(stejka_xml, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

hyperlinks = stejka_xml.xpath('//*[contains(@type, "hyperlink")]/text()')
for link in hyperlinks:
    print link

mebli_lviv_xml = get_products()
with open(settings.SHOP_XML, 'w') as xml_file:
    xml_file.write(tostring(mebli_lviv_xml, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

mebli_lviv_xhtml = transform_to_xhtml(mebli_lviv_xml, settings.SHOP_XSL)
with open(settings.SHOP_XHTML, 'w') as xhtml_file:
    xhtml_file.write(tostring(mebli_lviv_xhtml, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
