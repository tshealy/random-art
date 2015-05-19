import random
from math import *

class ExpressionGen:

    def __init__(self):
        self.starter = ["(x * y)", "(x * x)", "(y * y)", "(x/2)", "(y/2)", "(x+y)/2", "(x-y)/2"]
        self.functions = ["sin(", "cos(", "sin(pi*", "cos(pi*", "extreme(", "cos(x*",\
                          "sin(x*", "exp(", "expm1(", "square("]
        self.two_args_func = ["avg(", "power_abs("]

    def generate(self):
        gen_str = random.choice(self.starter)
        length = random.randint(5,30)
        while length > 0:
            num_of_args = random.choice([1, 2])
            if num_of_args == 1:
                rand_func = random.choice(self.functions)
                gen_str = rand_func +  gen_str + ")"
                length -= 1
            else:
                rand_func = random.choice(self.two_args_func)
                gen_str = rand_func +  random.choice(self.starter) + ", " + gen_str + ")"
                length -= 1
        self.expression = gen_str


    def evaluate(self, x, y):
        return eval(self.expression)

    def __str__(self):
        return self.expression

def avg(x, y):
    return (x +y)/2

def log_abs(x):
    return log(abs(x))

def square(x):
    return sqrt(abs(x))

def power_abs(x, y):
    return pow(abs(x), abs(y))

def extreme(x):
    if x > 0:
        return -1
    elif x < 0:
        return 1
    else:
        return 0

def multi_square_pow(x, y):
    return pow(pow(pow(sqrt(abs(x)), abs(y)), abs(x)), sqrt(abs(y)))

def negative(x):
    return -x

def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    gen = ExpressionGen()
    gen.generate()
    return gen

    # expr1 = lambda x, y: (x + y)/2
    # expr2 = lambda x, y: (x - y)/2
    # expr3 = lambda x, y: x * y
    # return random.choice([expr1, expr2, expr3])

def run_expression(gen, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return gen.evaluate(x, y)
