from sympy import *
from math import *

def newton_Raphson():
	
	x=Symbol('x')
	fx=sympify(input('Digite função F(x): '))
	precisao = float(input('Digite a precisão da resposta: '))
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
def LU():
	import scipy.linalg as linalg 
	import numpy as np
	import scipy

	nums = input("Escreva os valores da primeira linha separado por espaco:").split()
	num = [] 
	for i in nums: num.append(int(i))

	nums1 = input("Escreva os valores da segunda linha separado por espaco:").split() 
	nu = [] 
	for i in nums1: nu.append(int(i))

	nums2 = input("Escreva os valores da terceira linha separado por espaco:").split() 
	n = [] 
	for i in nums2: n.append(int(i))


	A = np.array([[num],[nu],[n]])
	A =np.reshape(A, (3, 3))


	y= input("Escreva os valores da coluna separado por espaco:").split()  
	z = [] 
	for i in y: z.append(int(i))


	B = np.array([y])
	B = np.reshape(B,(3,1))
	 


	LU = linalg.lu_factor(A) 

	x = linalg.lu_solve(LU, B) 
	print("Solutions:\n",x) 

	P, L, U = scipy.linalg.lu(A)
	print("A= ",A)
	print("\n")

	print ("P= ",P)
	print("\n")

	print ("L= ",L)
	print("\n")

	print ("U= ",U)
	print("\n")

def La_Grange():
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
def Jacobi():
	#input do número de interações que o usuário deseja
	n = int(input('número de interações: '))

	#input da matriz "y"
	y1 = float(input('y1: '))
	y2 = float(input('y2: '))
	y3 = float(input('y3: '))

	#input da matriz principal
	a11 = float(input('a11: '))
	a12 = float(input('a12: '))
	a13 = float(input('a13: '))
	a21 = float(input('a21: '))
	a22 = float(input('a22: '))
	a23 = float(input('a23: '))
	a31 = float(input('a31: '))
	a32 = float(input('a32: '))
	a33 = float(input('a33: '))

	k = 0 #variavel que será usada nas interações

	while True: #loop para se fazer as equações de acordo com o número de interações que o usuário deseja

	    X1 = (y1 - (a12*k) - (a13*k)) / a11
	    X2 = (y2 - (a22*k) - (a23*k)) / a21
	    X3 = (y3 - (a32*k) - (a33*k)) / a31
	    print("X{} = ({};{};{})".format(k, X1, X2, X3))
	    #variavel que irá ficar checando se chegou ao número de interações que o usuário colocou
	    k = k + 1
	    #se chegar ao número o loop para de rodar
	    if k == n:
	        break

def main():
	user_choice = int(input('Digite o metodo desejado: \n [1](Interpolação) \n [2](Zeros de Funcao Real) \n [3](Sistemas Lineares)\n \n'))
	if user_choice == 1:
		userchoice = int(input('Quais metodos voce deseja ver \n [1]La_Grange \n [2]Newton \n'))
		if userchoice == 1:
			La_Grange()
		else:
			print('Erro, Metodo nao abordado pelo grupo')

	elif user_choice == 2:
		userchoice = int(input('Quais metodos voce deseja ver \n [1]Bissecao \n [2]Newton-Raphson \n'))
		if userchoice == 1:
			print('Erro, Metodo nao abordado pelo grupo')
		if userchoice ==2:
			newton_Raphson()
	elif user_choice == 3:
		userchoice = int(input('Quais metodos voce deseja ver \n [1]LU \n [2]Jacobi \n'))
		if userchoice == 1:
   			LU()
		if userchoice == 2:
			Jacobi()	
	else:
		print('Erro, Metodo nao abordado pelo grupo')	
if __name__ == "__main__":
	main()
