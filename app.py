from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/hello/<name>')
def name(name):
    return "Hey there {}".format(name)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "main":
    app.run(DEBUG=True)
