
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
