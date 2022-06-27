import numpy as np
e = 2.7182

class Spline:

    def __init__(self, a, b, c, d, x_i, inicio, fin):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x_i = x_i
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        if self.x_i < 0:
            return f'{self.a} + {self.b}(x+{abs(self.x_i)}) + {self.c}(x+{abs(self.x_i)})² + {self.d}(x+{abs(self.x_i)})³, {self.inicio} <= x <= {self.fin}'
        return f'{self.a} + {self.b}(x-{self.x_i}) + {self.c}(x-{self.x_i})² + {self.d}(x-{self.x_i})³, {self.inicio} <= x <= {self.fin}'

    def inicio(self):
        return self.inicio

    def fin(self):
        return self.fin

    def esta_dentro_del_intervalo(self, x):
        return self.inicio <= x <= self.fin    

    def evaluar_en(self, x):
        if self.esta_dentro_del_intervalo(x):
            return self.a + self.b*(x-self.x_i) + self.c*(x-self.x_i)**2 + self.d*(x-self.x_i)**3
        raise ValueError(f'El punto {x} no esta dentro del intervalo [{self.inicio}, {self.fin}]')


def spline_matricial(cant_nodos, nodo, func, derivada_0, derivada_n):
	n = cant_nodos - 1
	h = []
	b = []
	for i in range(n):
		h.append(nodo[i + 1] - nodo[i])
	
	b.append(3 * ( func[1] - func[0] ) / h[0] - 3 * derivada_0)
	for i in range(1, n):
		b.append(3 * ( func[i + 1] - func[i] ) / h[i] - 3 * ( func[i] - func[i - 1] ) / h[i - 1])
	b.append(-3 * ( func[n] - func[n - 1] ) / h[n - 1] + 3 * derivada_n) 

	A = armar_matriz_nula(cant_nodos)
	#Armamos la primer y ultima fila
	A[0][0] = 2 * h[0]
	A[0][1] = h[0]
	A[n][n - 1] = h[n - 1]
	A[n][n] = 2 * h[n - 1]

	#Armamos las demas filas
	for i in range(1, n):
		A[i][i - 1] = h[i - 1]
		A[i][i] = 2 * ( h[i - 1] + h[i] )
		A[i][i + 1] = h[i]

	return np.linalg.solve(A, b), h
		
def armar_matriz_nula(n):
	A = []
	for i in range(n):
		fila = []
		for j in range(n):
			fila.append(0)
		A.append(fila)
	return A

def coeficientes_de_splines(cant_nodos, nodo, func, derivada_0, derivada_n):
	vector_c, h = spline_matricial(cant_nodos, nodo, func, derivada_0, derivada_n)
	vector_a = func[:]
	vector_d = []
	for i in range(cant_nodos - 1):
		vector_d.append(( vector_c[i + 1] - vector_c[i] ) / 3 * h[i])
	vector_b = []
	for i in range(cant_nodos - 1):
		vector_b.append( ( vector_a[i + 1] - vector_a[i] ) / h[i] - h[i] * ( 2 * vector_c[i] + vector_c[i + 1] ) / 3 )
	
	return vector_a, vector_b, vector_c, vector_d
	
def crear_splines(vector_dominio, vector_imagen, derivada_0, derivada_n):
    vector_splines = []
    cant_nodos = len(vector_dominio)
    a, b, c, d = coeficientes_de_splines(cant_nodos, vector_dominio, vector_imagen, derivada_0, derivada_n)
    for i in range(cant_nodos - 1):
        vector_splines.append(Spline(a[i], b[i], c[i], d[i], vector_dominio[i], vector_dominio[i], vector_dominio[i+1]))
    return vector_splines
#print(spline(4, [1,2,3,4], [2,4,6,8], 2, 2))
#a, b = spline(4, [0,1,2,3], [1, e, e ** 2, e ** 3], 1, e ** 3)
#print(a)
#print(b)
#print(np.linalg.solve(a, b))
#print(spline(4, [1,2,3,4], [2,4,6,8], 2, 2))
#print(spline(4, [27.7, 28, 29, 30], [4.1, 4.3, 4.1, 3], 1/3, -3/2))
print(spline(4, [-1, 0, 1, 2], [0, -3, 2, 21], -5, 28))








