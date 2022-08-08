from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from math import sqrt
from operator import add, sub, mul, pow
import re

app = Flask(__name__)
CORS(app)
operacoes = {
    "+": add,
    "-": sub,
    "*": mul,
    "**": pow,
    "/": lambda x, y: x / y if y > 0 else "It can't be divided by zero",
    "s": lambda x: sqrt(x),
    "ss": lambda x, y: x ** (1/y) if y > 0 else "It can't be zero"
}

@app.route('/', methods=["GET", "POST"])
def main() -> None:
    if request.method == "GET":
        return render_template("index.html")

@app.route('/conta/<string:operacao>', methods=["GET"])
def receive(operacao):
    resposta = jsonify({"resultado": "erro", "detalhes": "erro"})
    aux =  0
    for op in operacoes:
        if op in operacao:
            operacao_final = op
            aux += 1

    if aux > 1: return resposta

    pattern = r'(\{})'.format(operacao_final)
    l = re.split(pattern, operacao)
    print(l)
    valor1 = float(l[0])
    valor2 = float(l[2])
    final = operacoes[operacao_final](valor1, valor2)
    resposta = jsonify({"resultado": "erro", "detalhes": final})
    return resposta

if __name__ == '__main__':
    app.run(debug=True)