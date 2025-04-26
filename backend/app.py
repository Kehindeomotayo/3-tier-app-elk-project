import os
<<<<<<< HEAD
=======
import time
import logging
>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import bcrypt
from dotenv import load_dotenv
<<<<<<< HEAD
from flask_migrate import Migrate  # <-- Make sure to import Migrate

# Load environment variables from .env file
=======
from flask_migrate import Migrate
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

# Load environment variables
>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
load_dotenv()

app = Flask(__name__)
CORS(app)

<<<<<<< HEAD
# Load configuration from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)  # <-- Initialize Migrate
=======
# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency', ['endpoint'])
>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable=False)

# Initialize products
def initialize_products():
    if not Product.query.first():
        products = [
            Product(name='Product 1', description='Description of product 1', price=19.99),
            Product(name='Product 2', description='Description of product 2', price=29.99),
            Product(name='Product 3', description='Description of product 3', price=39.99)
        ]
        db.session.add_all(products)
        db.session.commit()

<<<<<<< HEAD
=======
@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def log_request(response):
    request_latency = time.time() - request.start_time
    endpoint = request.path
    status = response.status_code

    # Log request details
    logging.info(f"{request.method} {endpoint} {status} - {request_latency:.4f}s")

    # Update Prometheus metrics
    REQUEST_COUNT.labels(method=request.method, endpoint=endpoint, status=status).inc()
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(request_latency)

    return response

>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
# API Routes
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
<<<<<<< HEAD
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
=======
    if not data or 'password' not in data or 'email' not in data or 'username' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)

    db.session.add(new_user)
    db.session.commit()
    logging.info(f"New user registered: {data['email']}")

>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
    return jsonify({'message': 'User registered successfully!'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
<<<<<<< HEAD
    user = User.query.filter_by(email=data['email']).first()
    if not user or not bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
        return jsonify({'message': 'Invalid email or password!'}), 401
=======
    if not data or 'password' not in data or 'email' not in data:
        return jsonify({'message': 'Missing required fields'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if not user or not bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
        return jsonify({'message': 'Invalid email or password!'}), 401

    logging.info(f"User logged in: {data['email']}")
>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
    return jsonify({'message': f'Welcome, {user.username}!'})

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = [{'name': product.name, 'description': product.description, 'price': product.price} for product in products]
    return jsonify(products_list)

<<<<<<< HEAD
# Entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This will create tables if they do not exist
        initialize_products()  # This initializes products if they are not in the database
=======
# Prometheus metrics endpoint
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

# Entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        initialize_products()
>>>>>>> 45e8187e96b4861ef302eccb3bf70626916f00f2
    app.run(host='0.0.0.0', port=5000, debug=True)
