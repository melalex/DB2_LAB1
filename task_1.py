from __future__ import unicode_literals

import settings
import re

from lxml.html import parse
from lxml.etree import Element
from lxml.etree import tostring


def __add_fragments(url, parent):
    html = parse(url)
    image_url_regex = re.compile(r'^background-image: url\((.+)\)', re.IGNORECASE)
    for element in html.iter():
        if element.tag == 'a':
            href = element.get('href')
            if element.get('href'):
                fragment = Element("fragment", type='hyperlink')
                fragment.text = settings.BASE_PAGE + href
                parent.append(fragment)
        elif element.tag == 'img':
            fragment = Element("fragment", type='image')
            fragment.text = element.get('scr')
            parent.append(fragment)
        elif element.tag == 'div':
            style = element.get('style', '')
            image_url = image_url_regex.match(style)
            if image_url:
                fragment = Element("fragment", type='image')
                fragment.text = settings.BASE_PAGE + image_url.group(1)
                parent.append(fragment)
        elif element.text and element.tag != 'script' and element.tag != 'style':
            fragment = Element("fragment", type='text')
            fragment.text = element.text
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
            if a.get("href") and settings.BASE_PAGE + a.get("href") not in visited_hrefs
        )
        visited_hrefs.append(next_page.next())
        xml.append(page)

    return xml


if __name__ == "__main__":
    print tostring(get_xml(), pretty_print=True, xml_declaration=True, encoding='UTF-8')
