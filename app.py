from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db
from routes.customers import customers_bp
from routes.products import products_bp
from routes.orders import orders_bp

# Initialize Flask App
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Database
db.init_app(app)

# Register Blueprints
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(orders_bp, url_prefix='/orders')

@app.route('/')
def home():
    return "Welcome to the E-Commerce API!"

if __name__ == "__main__":
    app.run(debug=True)
