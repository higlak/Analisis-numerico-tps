"""
matriz = [
	[1, 2, 4],
	[3, 6, 7],
	[2, 9, 8]
]

"""

def descomposicion_LU(A, b):
	U = A.copy()
	L = esqueleto_para_L(A)

	for i in range(len(A) - 1):
		for j in range(1, len(A)):
			if j != i:
				m = U[j][i] / U[i][i]
				L[j][i] = m
				for k in range(len(A)):
					U[j][k] = U[j][k] - m * U[i][k]
	
	return L, U


def esqueleto_para_L(A):
	L = []
	for i in range(len(A)):
		fila = []
		for j in range(len(A)):
			if j == i:
				fila.append(1)
			else:
				fila.append(0)
		L.append(fila)
	return L


#print(esqueleto_para_L([1,2,3, 4]))
#print(descomposicion_LU([[3,1,0],[-9,-2,-1],[0,-1,0]], [12, -49, 3]))
#print(descomposicion_LU([[8,1,0],[-48,-5,-10],[8,2,-7]], [12, -49, 3]))
print(descomposicion_LU([[4,4,2],[4,5,0],[2,0,14]], [12, -49, 3]))


