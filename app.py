#the entry & exit point to our application
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/search/<car>")
def searchCar(car):
    return "Hello to " + car

if __name__ == '__main__':
    app.run(debug=True)