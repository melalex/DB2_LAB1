from __future__ import unicode_literals

import settings

from lxml.html import parse
from lxml.etree import Element
from lxml.etree import tostring


def get_products():
    xml = Element("data")
    html = parse(settings.SHOP_ALL_ITENS)
    products_types_urls = html.xpath('//div[contains(@class, "desc")]//a')
    for type_url in products_types_urls[:settings.PRODUCTS_TYPES_LIMITS]:
        url = type_url.get('href')
        product_type = Element("product_type", type_url=url)
        __add_products_from_url(url, product_type)
        xml.append(product_type)
    return xml


def __add_products_from_url(url, parent):
    if url != 'http://mebli-lviv.com.ua/ligko_kolusochka' and url != 'http://mebli-lviv.com.ua/kitchen-tables':
        html = parse(url)
        products_urls = html.xpath('//div[contains(@id, "page_content")]/div[not(contains(@class, "path"))]//div/a')
        for a in products_urls[:settings.PRODUCTS_LIMIT_PER_TYPE]:
            href = settings.SHOP + a.get('href', '')
            product = Element("product", product_url=href)
            __add_products_description_from_url(href, product)
            parent.append(product)


def __add_products_description_from_url(url, parent):
    html = parse(url)
    equipments = html.xpath('//table[contains(@class, "item_list")]/tr')[1:-1]
    for equipment in equipments[:settings.EQUIPMENT_LIMIT_PER_PRODUCT]:
        price = equipment.xpath('.//span[contains(@class, "price_main")]//text()')
        element = Element("equipment", price=price[0])
        description = equipment.xpath('.//td[contains(@valign, "top")]/text()')
        image = equipment.xpath('.//img')

        if description:
            description_element = Element('description')
            description_element.text = reduce(lambda res, x: res + '\n' + x, description).strip()
            element.append(description_element)

        if image:
            image_element = Element('image', scr=image[0].get('src'))
            element.append(image_element)

        parent.append(element)


if __name__ == "__main__":
    print tostring(get_products(), pretty_print=True, xml_declaration=True, encoding='UTF-8')
