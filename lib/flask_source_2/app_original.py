from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def table():
    return render_template("table.html",
                            title="Table"
    )


def bootstrap():
    app.run()


if __name__ == '__main__':
    bootstrap()