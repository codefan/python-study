import sympy 

x,a,b,c = sympy.symbols('x a b c')

print(sympy.solve( (x-(x-(x-4)/3)/2)/5-x/4, x))

print(sympy.solve(a*x**2+b*x+c, x))