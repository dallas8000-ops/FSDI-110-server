from flask import Flask

app = Flask(__name__)  # instance of Flask

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

# GET /api/coupons/count returns the number of coupons in the system.
@app.route('/api/coupons/count', methods=['GET'])
def get_coupons_count():
    return {"count": len(coupons)}


#http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask Framework"

#http://127.0.0.1:5000/hello
@app.route("/hello",methods =["GET"])
def hello():
    return "Hello World from flask"



# http://127.0.0.1:5000/cohort-63
@app.route("/cohort-63", methods =["GET"])
def cohort63():
    student_list = ["Robert", "Barney", "Luis", "Lemuel", "Reece", "John", "Angel"]
    return student_list


# http://127.0.0.1:5000/cohort-99
@app.route("/cohort-99", methods =["GET"])
def cohort99():
    student_list = ["Pam", "Dwight", "Michael", "Angela"]
    return student_list




# http://127.0.0.1:5000/contact
@app.route("/contact", methods =["GET"])
def contact():
    information = "email:dallas8000@hotmail.com, phone:123-456-7890"
    return information


.
  

# http://127.0.0.1:5000/course-information
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
