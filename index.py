import sympy, js
x= sympy.symbols('x', real=True)
js.document.querySelector('math').innerHTML = sympy.mathml(sympy.Integral(sympy.sqrt(1/x), x))
