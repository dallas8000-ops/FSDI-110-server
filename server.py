from flask import Flask, jsonify, request
app = Flask(__name__)

# Path Parameter
# Is a dynamic part of the URL used to identify a specific item or resource within an API.
#http://127.0.0.1:5000/greet/john

@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    print(name)
    print(f"this is the name {name}")
    return jsonify({"message": f"Hello {name}"}), 200 # OK

# ---------- PRODUCTS ----------
products = [
    {
        "_id": 1,
        "title": "Nintendo Switch",
        "price": 499.99,
        "category": "Electronics",
        "image": "https://picsum.photos/seed/1/300/300"
    },
    {
        "_id": 2,
        "title": "Smart Refrigerator",
        "price": 999.99,
        "category": "Kitchen",
        "image": "https://picsum.photos/seed/2/300/300"
    },
    {
        "_id": 3,
        "title": "Bluetooth Speaker",
        "price": 149.99,
        "category": "Audio",
        "image": "https://picsum.photos/seed/3/300/300"
    }
]
# GET /api/products, endpoint that returns a list of products



# GET    http://127.0.0.1:5000/api/products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully.",
        "products": products
    }), 200

# GET /api/products/<int:product_id> endpoint that returns a single product or 'Not found'

# GET /api/products/<int:product_id> endpoint that returns a single product or 'Not found'

# GET    http://127.0.0.1:5000/api/products/<int:product_id>
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((p for p in products if p["_id"] == product_id), None)
    if product is None:
        return jsonify({
            "success": False,
            "message": "Product not found"
        }), 404
    return jsonify({
        "success": True,
        "message": "Product retrieved successfully",
        "data": product
    }), 200


# POST /api/products

# POST   http://127.0.0.1:5000/api/products
@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or 'title' not in data or 'price' not in data or 'category' not in data or 'image' not in data:
        return jsonify({
            "success": False,
            "message": "Missing product data."
        }), 400
    new_id = max([p["_id"] for p in products], default=0) + 1
    product = {
        "_id": new_id,
        "title": data["title"],
        "price": data["price"],
        "category": data["category"],
        "image": data["image"]
    }
    products.append(product)
    return jsonify({
        "success": True,
        "message": "Product successfully created",
        "data": product
    }), 201


# PUT /api/products/<int:product_id>

# PUT    http://127.0.0.1:5000/api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    product = next((p for p in products if p["_id"] == product_id), None)
    if product is None:
        return jsonify({
            "success": False,
            "message": "Product not found"
        }), 404
    if not data:
        return jsonify({
            "success": False,
            "message": "Missing product data."
        }), 400
    product["title"] = data.get("title", product["title"])
    product["price"] = data.get("price", product["price"])
    product["category"] = data.get("category", product["category"])
    product["image"] = data.get("image", product["image"])
    return jsonify({
        "success": True,
        "message": "Product updated successfully",
        "data": product
    }), 200


## PUT /api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    for product in products:
        if product["_id"] == product_id:
            product["title"] = data["title"]
    print(data)
    return "xxxxx"


# DELETE /api/products/<int:product_id> endpoint that allows deleting an existing product by its id.
# DELETE http://127.0.0.1:5000/api/products/<int:product_id>
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product = next((p for p in products if p["_id"] == product_id), None)
    if product is None:
        return jsonify({
            "success": False,
            "message": "Product not found"
        }), 404
    products = [p for p in products if p["_id"] != product_id]
    return '', 204

# ---------- COUPONS ----------
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]





# GET /api/coupons endpoint that returns a list of coupons.
# GET    http://127.0.0.1:5000/api/coupons
@app.route('/api/coupons', methods=['GET'])
def get_coupons():
    return jsonify(coupons), 200

# GET /api/coupons/count returns the number of coupons in the system.
# GET    http://127.0.0.1:5000/api/coupons/count
@app.route('/api/coupons/count', methods=['GET'])
def get_coupons_count():
    return jsonify({"count": len(coupons)}), 200

# POST /api/coupons endpoint that adds a new coupon to coupons list.
# POST   http://127.0.0.1:5000/api/coupons
@app.route('/api/coupons', methods=['POST'])
def add_coupon():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Missing JSON body."}), 400
    code = data.get('code')
    discount = data.get('discount')
    if not isinstance(code, str) or not code.strip():
        return jsonify({"success": False, "message": "Coupon code is required and must be a non-empty string."}), 400
    if not isinstance(discount, int) or discount < 0:
        return jsonify({"success": False, "message": "Discount must be a non-negative integer."}), 400
    new_id = max([c["_id"] for c in coupons], default=0) + 1
    coupon = {"_id": new_id, "code": code.strip(), "discount": discount}
    coupons.append(coupon)
    return jsonify({"success": True, "data": coupon}), 201

# GET /api/coupons/<int:id> endpoint that returns a coupon that matches the given id.
# GET    http://127.0.0.1:5000/api/coupons/<int:id>
@app.route('/api/coupons/<int:id>', methods=['GET'])
def get_coupon_by_id(id):
    coupon = next((c for c in coupons if c["_id"] == id), None)
    if coupon is None:
        return jsonify({"success": False, "message": "Coupon not found."}), 404
    return jsonify({"success": True, "data": coupon}), 200

# PUT /api/coupons/<int:id> endpoint that allows editing an existing coupon by its id.
# PUT    http://127.0.0.1:5000/api/coupons/<int:id>
@app.route('/api/coupons/<int:id>', methods=['PUT'])
def update_coupon(id):
    data = request.get_json()
    coupon = next((c for c in coupons if c["_id"] == id), None)
    if coupon is None:
        return jsonify({"success": False, "message": "Coupon not found."}), 404
    if not data:
        return jsonify({"success": False, "message": "Missing JSON body."}), 400
    code = data.get('code', coupon['code'])
    discount = data.get('discount', coupon['discount'])
    if not isinstance(code, str) or not code.strip():
        return jsonify({"success": False, "message": "Coupon code is required and must be a non-empty string."}), 400
    if not isinstance(discount, int) or discount < 0:
        return jsonify({"success": False, "message": "Discount must be a non-negative integer."}), 400
    coupon["code"] = code.strip()
    coupon["discount"] = discount
    return jsonify({"success": True, "data": coupon}), 200

# DELETE /api/coupons/<int:id> endpoint that allows deleting an existing coupon by its id.
# DELETE http://127.0.0.1:5000/api/coupons/<int:id>
@app.route('/api/coupons/<int:id>', methods=['DELETE'])
def delete_coupon(id):
    global coupons
    coupon = next((c for c in coupons if c["_id"] == id), None)
    if coupon is None:
        return jsonify({"success": False, "message": "Coupon not found."}), 404
    coupons = [c for c in coupons if c["_id"] != id]
    return '', 204

# GET /api/coupons/search (query parameters) endpoint that returns all coupons with a discount less than 30.
# GET    http://127.0.0.1:5000/api/coupons/search
@app.route('/api/coupons/search', methods=['GET'])
def search_coupons():
    filtered = [c for c in coupons if c["discount"] < 30]
    return jsonify({"success": True, "data": filtered}), 200

@app.route("/", methods=["GET"])
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask Framework"

@app.route("/hello",methods =["GET"])
def hello():
    return "Hello World from flask"

@app.route("/cohort-63", methods =["GET"])
def cohort63():
    student_list = ["Robert", "Barney", "Luis", "Lemuel", "Reece", "John", "Angel"]
    return student_list

@app.route("/cohort-99", methods =["GET"])
def cohort99():
    student_list = ["Pam", "Dwight", "Michael", "Angela"]
    return student_list

@app.route("/contact", methods =["GET"])
def contact():
    information = {
        "email": "dallas8000@hotmail.com",
        "phone": "123-456-7890"
    }
    return jsonify(information)

@app.route("/course-information", methods=["GET"])
def course_information():
    course_data = {
        "title": "Introduction Web API with Flask",
        "duration": "4 Sessions",
        "level": "Beginner"
    }
    return course_data

if __name__ == "__main__":
    app.run(debug=True)
#when this file is run directly: __name__=="__main__"
#when this file is imported as a module: __name__=="server.py"
