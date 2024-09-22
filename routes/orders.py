from flask import Blueprint, request, jsonify
from models import db, Order

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/', methods=['POST'])
def place_order():
    data = request.get_json()
    new_order = Order(customer_id=data['customer_id'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order placed successfully'}), 201

@orders_bp.route('/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify({'customer_id': order.customer_id, 'order_date': order.order_date, 'status': order.status})
