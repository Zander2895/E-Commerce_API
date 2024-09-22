from flask import Blueprint, request, jsonify
from models import db, Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], stock=data.get('stock', 0))
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201

@products_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({'name': product.name, 'price': product.price, 'stock': product.stock})

@products_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = Product.query.get_or_404(id)
    product.name = data['name']
    product.price = data['price']
    product.stock = data.get('stock', product.stock)
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

@products_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

@products_bp.route('/', methods=['GET'])
def list_products():
    products = Product.query.all()
    products_list = [{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in products]
    return jsonify(products_list)
