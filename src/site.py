from ast import pattern
import code
from crypt import methods
from urllib import response
from flask import Flask, render_template, request
from math import sqrt
from operator import add, sub, mul, pow
import re

app = Flask(__name__)

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

@app.route('/conta/<string:operacao>', methods=["POST"])
def receive(operacao):
    print(operacao)
    pattern = r'(\w+)'
    l = re.split(pattern, operacao)
    l = re.sub(r"^\s+|\s+$", "", operacao)
    print(l)
    valor1 = float(l[0])
    operacao_final = l[1]
    valor2 = float(l[2])
    if operacao_final in operacoes:
        final = operacoes[operacao_final](valor1, valor2)
        print(final)
        return final

if __name__ == '__main__':
    app.run(debug=True)