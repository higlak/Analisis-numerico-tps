from math import sin, cos, e, pi, log10

MAX_ITERACIONES = 100

def g(x):
    return 0.001*x*(x-1000)**2 - 25000

def g_punto_fijo(x):
    return x + ((-x)/1000000) * g(x)

def g_prima(x):
    return (x-1000)*(3*x-1000)/1000

def g_2_prima(x):
    return (3*x-2000)/500

def _biseccion(a, b, iteraciones, tolerancia, lista_iteraciones):
    p = (a + b) / 2
    g_p = g(p)
    lista_iteraciones.append(p)
    print(f'{iteraciones}_) a: {a}, b: {b}, p: {p}, f(p): {g_p}')

    if g_p == 0 or (b - p) < tolerancia:
        print(f"La raíz aproximada con un error menor a {tolerancia} es {p} y se consiguio despues de {iteraciones + 1} iteraciones.")
        return lista_iteraciones

    if g_p * g(a) == abs(g_p * g(a)):   
        return _biseccion(p, b, iteraciones + 1, tolerancia, lista_iteraciones)
    return _biseccion(a, p, iteraciones + 1, tolerancia, lista_iteraciones)

def biseccion(a, b, tolerancia):
    return _biseccion(a, b, 0, tolerancia, [])

def prueba_existencia_de_punto_fijo(limite_inf, limite_sup, g):
	if(g(limite_inf) <= g(limite_sup)):
		if((g(limite_inf) >= limite_inf) and (g(limite_inf) <= limite_sup) and (g(limite_sup) >= limite_inf) and (g(limite_sup) <= limite_sup)):
			return True
	print("No pude probar la existencia de un punto fijo \n")
	return False

def prueba_unicidad_de_punto_fijo(limite_inf, limite_sup, gPrima):
	if(gPrima(limite_inf) <= gPrima(limite_sup)):
		if gPrima(limite_sup) < 1 and gPrima(limite_inf) > -1:
			return True
	print("No pude probar la unicidad del punto fijo \n")
	return False

def punto_fijo(semilla, tolerancia):
    p_anterior = semilla
    p_actual = g_punto_fijo(p_anterior)
    cantidad_de_iteraciones = 0
    lista_iteraciones = []
    lista_iteraciones.append(p_actual)

    while (abs(p_actual - p_anterior) > tolerancia and g_punto_fijo(p_actual) != 0) :
        print(f"{cantidad_de_iteraciones}: p_0: {p_anterior}, p: {p_actual}, diferencia: {abs(p_actual-p_anterior)}")
        p_anterior = p_actual
        p_actual = g_punto_fijo(p_anterior)
        lista_iteraciones.append(p_actual)
        cantidad_de_iteraciones += 1
    print(f"La raíz aproximada con un error menor a {tolerancia} es {p_actual} y se consiguio despues de {cantidad_de_iteraciones} iteraciones.")
    return lista_iteraciones

def calcular_p_newton_raphson(p, multiple):
    return p - (g(p) * g_prima(p))/(g_prima(p)**2 - g(p) * g_2_prima(p)) if multiple else p - g(p) / g_prima(p)

def newton_raphson(semilla, tolerancia, multiple= False):
    lista_iteraciones = []
    p_anterior = semilla
    tolerancia_tope = 100
    p_actual = calcular_p_newton_raphson(p_anterior, multiple)
    cantidad_de_iteraciones = 0
    lista_iteraciones.append(p_actual)

    while abs(p_anterior - p_actual) > tolerancia:
        print(f"{cantidad_de_iteraciones}: p_0: {p_anterior}, p: {p_actual}, diferencia: {abs(p_actual-p_anterior)}")
        p_anterior = p_actual
        p_actual = calcular_p_newton_raphson(p_anterior, multiple)
        cantidad_de_iteraciones += 1
        lista_iteraciones.append(p_actual)
        if abs(p_anterior - p_actual) > tolerancia_tope:
            print('El metodo no converge a la raiz')
            return

    print(f"La raíz aproximada con un error menor a {tolerancia} es {p_actual} y se consiguio despues de {cantidad_de_iteraciones} iteraciones.")
    return lista_iteraciones

# newton_raphson(1100, 1e-13)
# newton_raphson(1100,1e-13,True)

def _metodo_secante(p_0, p_1, tolerancia, iteraciones, lista_iteraciones):
    if iteraciones > MAX_ITERACIONES:
        print('El método no converge')
        return
    p_actual = p_1 - (g(p_1)*(p_1 - p_0))/(g(p_1)-g(p_0))
    print(f'{iteraciones}_) p: {p_actual}, f(p): {g(p_actual)}')
    lista_iteraciones.append(p_actual)
    
    if abs(p_actual - p_1) < tolerancia:
        print(f"La raíz aproximada con un error menor a {tolerancia} es {p_actual} y se consiguio despues de {iteraciones + 1} iteraciones.")
        return lista_iteraciones 
    return _metodo_secante(p_1, p_actual, tolerancia, iteraciones + 1, lista_iteraciones)

def metodo_secante(p_0, p_1, tolerancia):
    return _metodo_secante(p_0, p_1, tolerancia, 0, [])

# metodo_secante(1000,1100, 1e-13)

def orden_de_convergencia(iteraciones):
    ordenes_de_convergencia = []
    for i in range(0, len(iteraciones)-1):
        if i < 2:
            ordenes_de_convergencia.append(0)
        else:

            e_nMas1 = abs(iteraciones[i+1] - iteraciones[i])
            e_n = abs(iteraciones[i] - iteraciones[i-1])
            e_nMenos1 = abs(iteraciones[i-1] - iteraciones[i-2])
            alfa = ordenes_de_convergencia[i-1]

            if(e_nMas1 != 0 and e_n != 0 and e_nMenos1 != 0):
                log_numerador = log10((e_nMas1)/(e_n))
                log_denominador = log10((e_n)/(e_nMenos1))
                alfa = log_numerador/log_denominador
            ordenes_de_convergencia.append(alfa)

    return ordenes_de_convergencia

def calculo_de_constante_asintotica(iteraciones, alfa):
    constantes_asintoticas = []
    for i in range(0, len(iteraciones)-1):
        if i < 1:
            constantes_asintoticas.append(0)
        else:
            e_nMas1 = abs(iteraciones[i+1] - iteraciones[i])
            e_n = abs(iteraciones[i] - iteraciones[i-1])
            constante = e_nMas1 / e_n**alfa
            constantes_asintoticas.append(constante)
    return constantes_asintoticas

for cst in calculo_de_constante_asintotica(punto_fijo(1100, 1e-10), 2):
    print(cst) 

for orden in orden_de_convergencia(punto_fijo(1100, 1e-10)):
    print(orden) 

biseccion(1000, 1200, 1e-11)