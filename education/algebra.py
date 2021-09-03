import sympy 

x,y,z = sympy.symbols('x y z')

def equationX(symbol):
    return sympy.solve(symbol, x)

print(equationX( (x-(x-(x-4)/3)/2)/5-x/4))