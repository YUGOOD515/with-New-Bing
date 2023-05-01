from sympy import Symbol, Derivative, sympify, pprint

def derivative(f):
    x = Symbol('x')
    f = sympify(f)
    d = Derivative(f, x)
    return d.doit()

f = input('输入一个函数: ')
df = derivative(f)

print('导函数为: ')
pprint(df)