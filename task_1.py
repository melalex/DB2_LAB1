from __future__ import unicode_literals

import settings

from lxml.html import parse
from lxml.etree import Element
from lxml.etree import tostring


def __add_fragments(url, parent):
    html = parse(url)
    texts = html.xpath("//*[not(self::script)]/text()")
    for text in texts:
        fragment = Element("fragment", type='text')
        fragment.text = text
        parent.append(fragment)
    imgs = html.xpath('.//div[starts-with(@style, "background-image: url(")]')
    for img in imgs:
        fragment = Element("fragment", type='image')
        fragment.text = img.get("style")
        parent.append(fragment)

    return html


def get_xml():
    visited_hrefs = [settings.BASE_PAGE]

    xml = Element("data")
    for i in xrange(0, 19):
        url = visited_hrefs[-1]
        page = Element("page", url=url)
        html = __add_fragments(url, page)
        next_page = (
            settings.BASE_PAGE + a.get("href") for a in html.findall('.//a')
            if settings.BASE_PAGE + a.get("href") not in visited_hrefs
        )
        visited_hrefs.append(next_page.next())
        xml.append(page)

    return xml


if __name__ == "__main__":
    print tostring(get_xml(), pretty_print=True, xml_declaration=True, encoding='UTF-8')
