from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for products
products = []


@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({"error": "Bad request, missing required fields"}), 400

    product = {
        'name': data['name'],
        'description': data['description'],
        'price': data['price']
    }
    products.append(product)
    return jsonify(product), 201


@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200


if __name__ == '__main__':
    app.run(debug=True)
