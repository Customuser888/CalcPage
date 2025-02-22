from flask import Flask, render_template, request

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

def add(N1, N2):
    result = N1 + N2
    return result
def substract(N1, N2):
    result = N1 - N2
    return result
def multiply(N1, N2):
    result = N1 * N2
    return result
def divide(N1, N2):
    if(N1==0 and N2==0):
        result = 0
    else:
        result = N1 / N2
    return result
def degree(N1, N2):
    result = N1 ** N2
    return result
def maximum(N1, N2):
    if(N1 > N2):
        result = N1
    else:
        result = N2
    return result
def minimum(N1, N2):
    if(N1 < N2):
        result = N1
    else:
        result = N2
    return result

@app.route('/', methods=['POST'])
def result():
    var_1 = request.form.get("var_1", type=int, default=0)
    var_2 = request.form.get("var_2", type=int, default=0)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = add(var_1, var_2)
    elif(operation == 'Subtraction'):
        result = substract(var_1, var_2)
    elif(operation == 'Multiplication'):
        result = multiply(var_1, var_2)
    elif(operation == 'Division'):
        result = divide(var_1, var_2)
    elif(operation == 'Degree'):
        result = degree(var_1, var_2)
    elif(operation == 'Max'):
        result = maximum(var_1, var_2)
    elif(operation == 'Min'):
        result = minimum(var_1, var_2)
    else:
        result = 0
    entry = result
    return render_template('form.html', entry=entry)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
