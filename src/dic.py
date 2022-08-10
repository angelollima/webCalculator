from operator import add, sub, mul, pow
from math import sqrt

operacoes = {
    "+": add,
    "-": sub,
    "×": mul,
    #"**": pow,
    "÷": lambda x, y: x / y if y > 0 else "It can't be divided by zero",
    #"s": lambda x: sqrt(x),
    #"ss": lambda x, y: x ** (1/y) if y > 0 else "It can't be zero"
}