from flask import Blueprint, jsonify, request

from sensyne.db import db
from sensyne.models import Product


bp = Blueprint('main', __name__)


@bp.route("/products")
def get_products():
    """Endpoint returning all products.
    ---
    responses:
      200:
        description: A list of all products
        schema:
          id: Product
          properties:
            code:
              type: integer
              description: The code of the product
            name:
              type: string
              description: The name of the product
            price:
              type: number
              description: The price of the product in pounds
    """
    products = db.session.query(Product).all()
    return jsonify([Product.serialize(product) for product in products])


@bp.route("/product", methods=['POST'])
def create_product():
    """Endpoint for creating a new product.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: Product
          required:
            - name
            - price
          properties:
            code:
              type: integer
              description: The code of the product
            name:
              type: string
              description: The name of the product
            price:
              type: number
              description: The price of the product in pounds
    responses:
      201:
        description: Serialized fields of the newly created product.
        schema:
          id: Product
          properties:
            code:
              type: integer
              description: The code of the product
            name:
              type: string
              description: The name of the product
            price:
              type: number
              description: The price of the product in pounds
    """
    name = request.json['name']
    price = request.json['price']
    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return jsonify(Product.serialize(new_product)), 201


@bp.route("/product/<product_id>", methods=['GET'])
def get_product_with_id(product_id):
    """Endpoint for retrieving a product by ID.
    ---
    parameters:
      - name: product_id
        in: path
        required: true
        schema:
          id: Product
          required:
            - name
            - price
          properties:
            code:
              type: integer
              description: The code of the product
            name:
              type: string
              description: The name of the product
            price:
              type: number
              description: The price of the product in pounds
    responses:
      204:
        description: Product with specified ID not found.
      201:
        description: Serialized fields of the newly created product.
        schema:
          id: Product
          properties:
            code:
              type: integer
              description: The code of the product
            name:
              type: string
              description: The name of the product
            price:
              type: number
              description: The price of the product in pounds
    """
    product = db.session.query(Product).filter(Product.code == product_id).first()
    if not product:
        return jsonify(message='Resource not found.'), 204
    return jsonify(Product.serialize(product))


@bp.route("/product/<product_id>", methods=['PUT'])
def put_product_with_id(product_id):
    """Endpoint for updating a product by ID.
    ---
    parameters:
      - name: product_id
        in: path
        required: true
        schema:
          id: Product
          required:
            - name
            - price
          properties:
            code:
              type: integer
              description: The code of the product
            name:
              type: string
              description: The name of the product
            price:
              type: number
              description: The price of the product in pounds
    responses:
      204:
        description: Product with specified ID not found.
      201:
        description: Serialized fields of the newly updated product.
        schema:
          id: Product
          properties:
            code:
              type: integer
              description: The code of the product
            name:
              type: string
              description: The name of the product
            price:
              type: number
              description: The price of the product in pounds
    """
    product = db.session.query(Product).filter(Product.code == product_id).first()
    if not product:
        return '', 204

    for attr_name in ('name', 'price'):
        attr = request.json.get(attr_name)
        if attr:
            setattr(product, attr_name, attr)

    db.session.add(product)
    db.session.commit()

    return jsonify(Product.serialize(product))


@bp.route("/product/<product_id>", methods=['DELETE'])
def delete_product_with_id(product_id):
    """Endpoint for deleting a product by ID.
    ---
    parameters:
      - name: product_id
        in: path
        required: true
        schema:
          id: Product
          required:
            - name
            - price
          properties:
            code:
              type: integer
              description: The code of the product
            name:
              type: string
              description: The name of the product
            price:
              type: number
              description: The price of the product in pounds
    responses:
      204:
        description: Product with specified ID not found.
      201:
        description: The ID of the deleted product.
        schema:
          properties:
            deleted_product_id:
              type: integer
              description: The ID of the deleted product.
    """
    product_to_delete = db.session.query(Product).filter(Product.code == product_id).first()
    if not product_to_delete:
        return '', 204
    db.session.delete(product_to_delete)
    db.session.commit()
    return jsonify(deleted_product_id=product_id)
