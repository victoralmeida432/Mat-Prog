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
