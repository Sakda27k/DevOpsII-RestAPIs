from flask import Flask, request, jsonify

app = Flask(__name__)

items_list = [
    {"name": "Potato", "category": 1, "price": 20.5, "instock": 200},
    {"name": "Papaya", "category": 2, "price": 25, "instock": 250},
    {"name": "Pomegranate", "category": 3, "price": 30, "instock": 150},
    {"name": "Tangerine", "category": 4, "price": 35, "instock": 300},
]

def _find_next_name(name):
    data = [x for x in items_list if x['name'] == name]
    return data

#REST API
@app.route('/item/<name>', methods=["DELETE"])
def delete_item(name: str):
    data = _find_next_name(name)
    if not data:
        return {"error": "item not found"}, 404
    else:
        items_list.remove(data[0])
        return "item deleted successfully", 200

@app.route('/item', methods=["GET"])
def get_items():
    return jsonify(items_list)

@app.route('/item/<name>', methods=["GET"])
def get_items_name(name):
    data = _find_next_name(name)
    if not data:
        return {"error": "item not found"}, 404
    else:
        return jsonify(data)

@app.route('/item', methods=["POST"])
def post_items():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock":instock,
    }

    if _find_next_name(name):
        return {"error": "item already exists"}, 400
    else:
        items_list.append(new_data)
        return jsonify(items_list)

@app.route('/item/<name>', methods=["PUT"])
def update_item(name):
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    data = _find_next_name(name)
    if not data:
        return {"error": "item not found"}, 404
    else:
        item = data[0]



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
