import math


def prueba_existencia_de_punto_fijo(limite_inf, limite_sup, g):
	if(g(limite_inf) <= g(limite_sup)):
		if((g(limite_inf) >= limite_inf) and (g(limite_inf) <= limite_sup) and (g(limite_sup) >= limite_inf) and (g(limite_sup) <= limite_sup)):
			return True
	print("No pude probar la existencia de un punto fijo \n")
	return False

def prueba_unicidad_de_punto_fijo(limite_inf, limite_sup, gPrima):
	if(gPrima(limite_inf) <= gPrima(limite_sup)):
		if(gPrima(limite_sup) < 1):
			return True
	print("No pude probar la unicidad del punto fijo \n")
	return False

def raiz_punto_fijo(semilla, limite_inf, limite_sup, tolerancia):
	def g(x):
		resultado = x - math.sin(x) + 0.5*x**0.5
		print(f"g({x})={resultado}\n")
		return resultado
	def gPrima(x):
		return ((1/4)*g(x))

	if(not prueba_existencia_de_punto_fijo(limite_inf, limite_sup, g)):
		return
	if(not prueba_unicidad_de_punto_fijo(limite_inf,limite_sup,gPrima)):
		return

	print("Se cumplen las hipotesis\n\n")

	seguir_iterando = True
	i = 0
	p_anterior = semilla
	while(seguir_iterando):
		p_actual = g(p_anterior)
		if(abs(p_actual - p_anterior) <= tolerancia):
			seguir_iterando = False
		else:
			p_anterior = p_actual
		i += 1

	print(f"Se encontro una raiz en el intervalo de valor {p_actual} +- {tolerancia}, despues de {i} iteraciones")



def raiz_NewtonRapson(semilla, tolerancia):
	def f(x):
		return (3*x**2-3)
	def fPrima(x):
		return(6*x)
	##fPrima(x) debe ser distinto de 0
	def g(x):
		resultado = x - (f(x)/fPrima(x))
		print(f"g({x})={resultado}\n")
		return resultado

	raiz_NewtonRapson_rec(semilla,tolerancia, 0, f, fPrima, None, g)


def raiz_NewtonRapson_rec(semilla, tolerancia, iteracion, f, fPrima, f2Prima, g):
	iteracion += 1
	if(fPrima(semilla) == 0):
		print(f"f'({semilla}) = 0")
		return
	pn = g(semilla)
	if(abs(pn - semilla) <= tolerancia):
		print(f"Se encontro una raiz en el intervalo de valor {pn} +- {tolerancia}, despues de {iteracion} iteraciones")
		return
	raiz_NewtonRapson_rec(pn, tolerancia, iteracion, f, fPrima, f2Prima, g)



def raiz_NewtonRapson_raices_multiples(semilla, tolerancia):
	def f(x):
		return (3*x**2-3)
	def fPrima(x):
		return(6*x)
	def f2Prima(x):
		return(6*x-18)
	def g(x):
		resultado = x - ((f(x) * fPrima(x))/(fPrima(x)**2 - f(x)*f2Prima(x)))
		print(f"g({x})={resultado}\n")
		return resultado

	raiz_NewtonRapson_rec(semilla, tolerancia, 0, f, fPrima, f2Prima, g)



def raiz_secante(semilla0, semilla1, tolerancia):
	def f(x):
		return (3*x**2-3)
	def g(p0, p1):
		resultado = p0 - ((f(p0)*(p0-p1))/(f(p0) - f(p1)))
		print(f"g({p0},{p1})={resultado}\n")
		return resultado

	raiz_secante_rec(semilla0, semilla1, tolerancia, 0, f, g)

def raiz_secante_rec(semilla0, semilla1, tolerancia, iteracion, f, g):
	iteracion += 1
	pn = g(semilla0, semilla1)
	if(abs(pn - semilla1) <= tolerancia):
		print(f"Se encontro una raiz en el intervalo de valor {pn} +- {tolerancia}, despues de {iteracion} iteraciones")
		return
	raiz_secante_rec(semilla1, pn, tolerancia, iteracion, f, g)


raiz_punto_fijo(0.55, 0.1, 1, 0.0000000000000000000000000001)
#raiz_NewtonRapson(-1.25, 0.0001)
#raiz_NewtonRapson_raices_multiples(1.5, 0.001)
#raiz_secante(-1.25,-0.875,0.0001)




#f = x**3-1.9*x**2-1.05*x+2.745
#f'= 3*x**2-3.8*x-1.05
#raiz_NewtonRapson(-1, 0.000001)
