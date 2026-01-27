# GET /api/coupons/<int:id> endpoint that returns a coupon by id or 404 if not found.
@app.route('/api/coupons/<int:id>', methods=['GET'])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify({
                "success": True,
                "message": "Coupon retrieved successfully",
                "data": coupon
            }), 200
    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), 404
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


@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully.",
        "products": products
    }), 200

# GET /api/products/<int:product_id> endpoint that returns a single product or 'Not found'
@app.route('/api/products/<int:product_id>', methods=['GET'])


# GET /api/products/3
@app.route("/api/products/<int:product_id>")
def get_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), 200 # OK
    return jsonify({
        "success": False,
        "message": "Product not found"
    }), 404 # Not found


# POST /api/products
@app.route('/api/products', methods=['POST'])
def create_product():
    new_product = request.get_json()
    print(new_product)
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Product successfully created",
        "data": new_product
    }), 201 # CREATED

# ---------- COUPONS ----------
coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]




# GET /api/coupons endpoint that returns a list of coupons.
@app.route('/api/coupons', methods=['GET'])
def get_coupons():
    return coupons

# POST /api/coupons endpoint that adds a new coupon to the coupons list.
@app.route('/api/coupons', methods=['POST'])
def add_coupon():
    new_coupon = request.get_json()
    if not new_coupon or '_id' not in new_coupon or 'code' not in new_coupon or 'discount' not in new_coupon:
        return jsonify({
            "success": False,
            "message": "Invalid coupon data. '_id', 'code', and 'discount' are required."
        }), 400
    coupons.append(new_coupon)
    return jsonify({
        "success": True,
        "message": "Coupon successfully created",
        "data": new_coupon
    }), 201

# GET /api/coupons/count returns the number of coupons in the system.
@app.route('/api/coupons/count', methods=['GET'])
def get_coupons_count():
    return {"count": len(coupons)}

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
