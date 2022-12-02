from pprint import pprint
from flask import Flask, render_template, request

app_version = "1.1.0"
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("form.html")

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