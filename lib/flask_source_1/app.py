from pprint import pprint
from flask import Flask, render_template, request
from faker import Faker
import random

app_version = "1.1.0"
app = Flask(__name__)

class User:
    name = "default"
    age = "defalt"
    address = "defalt"
    phone = "defalt"
    email = "defalt"

    def __init__(self, name, age, address, phone, email):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email


list_of_users = []

fake = Faker()
for _ in range(50):
    list_of_users.append(User(
        name=fake.name(),
        age=random.randint(0,100),
        address=fake.address(),
        phone="",
        email=fake.email()
    ))



@app.route("/")
def root():
    return render_template("basic_table.html", users=list_of_users)

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        page_result = request.form
        json_result = dict(page_result)
        print(json_result)
        pprint(json_result)
        return render_template("result.html", result=page_result, app_version=app_version)

def bootstrap():
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    bootstrap()