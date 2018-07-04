from sympy import *
from math import *
#define x como o symbol devido a biblioteca sympy
x=Symbol('x')
#pede o F(x)
fx=sympify(input('Digite função F(x): '))
#Pede o erro, ou precisão do usuario
precisao = float(input('Digite a precisão da resposta: '))
#pede a primeira estimativa do x0
x0=float(input('Digite o x0: '))

df=fx.diff(x)

while True:
	x1=x0-(fx.subs(x,x0)/df.subs(x,x0))
	x0=x1-(fx.subs(x,x1)/df.subs(x,x1))
	print('{} - {} = {}'.format(x1,x0,abs(x1-x0)))
	if abs(x1-x0) <= precisao:
		print('FIM!')
		print('O zero da função está em: {}'.format(x0))
		break
