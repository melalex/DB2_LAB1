from __future__ import unicode_literals

import settings

from lxml.etree import tostring
from lxml.etree import parse
from lxml.etree import XSLT


def transform_to_xhtml(xml_to_transform, xsl_doc):
    xsl = parse(xsl_doc)
    transform = XSLT(xsl)
    xhtml = transform(xml_to_transform)
    return xhtml


if __name__ == "__main__":
    xml = parse('mebli_lviv.xml')
    mebli_lviv_xhtml = transform_to_xhtml(xml, settings.SHOP_XSL)
    with open(settings.SHOP_XHTML, 'w') as xhtml_file:
        xhtml_file.write(tostring(mebli_lviv_xhtml, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
    print tostring(
        transform_to_xhtml(xml, settings.SHOP_XSL),
        pretty_print=True,
        xml_declaration=True,
        encoding='UTF-8'
    )
