import code
from urllib import response
from flask import Flask, render_template, request
from math import sqrt
from operator import add, sub, mul, pow

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
    else:
        valor1 = int(request.form.get())
        operacao = request.form.get()
        valor2 = int(request.form.get())
        if operacao in operacoes:
            final = operacoes[operacao](valor1, valor2)
            return render_template("index.html", final=final)

if __name__ == '__main__':
    app.run(debug=True)