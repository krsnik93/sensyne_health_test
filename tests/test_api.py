import json


def test_get_products(client):
    response = client.get('/v1/products')
    content = response.json
    
    assert len(content) == 3
    assert content == [
        {
            'code': 1,
            'name': 'Lavender heart',
            'price': 9.25
        },
        {
            'code': 2,
            'name': 'Personalised cufflinks',
            'price': 45.0
        },
        {
            'code': 3,
            'name': 'Kids T-shirt',
            'price': 19.95
        }
    ]

def test_get_product_with_id(client):
    response = client.get('/v1/product/1')
    content = response.json
    assert content == {
        'code': 1,
        'name': 'Lavender heart',
        'price': 9.25
    }