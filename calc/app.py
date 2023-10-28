# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home_page():
    return "HomePage"

@app.route('/add')
def do_add():
    a = int(request.args['a'])
    b = int(request.args['b'])

    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])

    result = sub(a, b)
    return str(result)

@app.route('/mult')
def do_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])

    result = mult(a, b)
    return str(result)

@app.route('/div')
def do_div():
    a = int(request.args['a'])
    b = int(request.args['b'])

    result = div(a, b)
    return str(result)

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}
@app.route('/math/<opera>')
def do_operation(opera):
    a = int(request.args['a'])
    b = int(request.args['b'])

    result = operations[opera](a,b)
    return str(result) 



if __name__ == "__main__":
    app.run(debug=True)