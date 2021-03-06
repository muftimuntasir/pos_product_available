# -*- coding: utf-8 -*-
{
    'name': 'Available quantity of products in POS',
    'version': '8.0.1.0.2',
    'images': ['images/pos_product_available.jpg'],
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'GPL-3',
    'category': 'Point Of Sale',
    'website': 'https://twitter.com/yelizariev',
    'depends': ['point_of_sale', 'stock'],
    'data': [
        'data.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'installable': True,
}
