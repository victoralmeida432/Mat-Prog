import sympy

#Symbols permite o uso de uma variável ainda não determinada no programa
x = sympy.symbols('x')

#Pede o input dos pontos
print('Digite os pontos:')
x1 = float(input('X1='))
x2 = float(input('X2='))
x3 = float(input('X3='))

print('Insira as funções correspondentes aos pontos digitados:')
fx1 = float(input('F(X1)='))
fx2 = float(input('F(X2)='))
fx3 = float(input('F(X3)='))

#Simplifica a visualização do polinômio
L1 = sympy.expand(((x-x2)/(x1-x2))*((x-x3)/(x1-x3)))
L2 = sympy.expand(((x-x1)/(x2-x1))*((x-x3)/(x2-x3)))
L3 = sympy.expand(((x-x1)/(x3-x1))*((x-x2)/(x3-x2)))

#Fórmula
Px = fx1*L1+fx2*L2+fx3*L3

#Mostra o Resultado
print(Px)
