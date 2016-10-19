from __future__ import unicode_literals

import settings

from lxml.html import parse
from lxml.etree import Element
from lxml.etree import tostring


if __name__ == "__main__":
    print tostring(get_products(), pretty_print=True, xml_declaration=True, encoding='UTF-8')
