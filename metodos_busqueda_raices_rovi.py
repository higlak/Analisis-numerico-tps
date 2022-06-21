from math import sin, cos, e, pi

MAX_ITERACIONES = 100

def g(x):
    return -2500+x*(0.001*((387/x)-1000)**2)

def g_prima(x):
    return 6*x

def g_2_prima(x):
    return e**x + sin(x)

def _biseccion(a, b, iteraciones, tolerancia):
    p = (a + b) / 2
    g_p = g(p)
    print(f'{iteraciones}_) a: {a}, b: {b}, p: {p}, f(p): {g_p}')
    if abs(g_p) < tolerancia or g_p == 0:
        print(f"La raíz aproximada con un error menor a {tolerancia} es {p} y se consiguio despues de {iteraciones + 1} iteraciones.")
        return
    if g_p * g(a) == abs(g_p * g(a)):
        return _biseccion(p, b, iteraciones + 1, tolerancia)
    return _biseccion(a, p, iteraciones + 1, tolerancia)

def biseccion(a, b, tolerancia):
    return _biseccion(a, b, 0, tolerancia)


def punto_fijo(semilla, tolerancia):
    p_anterior = semilla
    p_actual = g(p_anterior)
    cantidad_de_iteraciones = 0

    while (abs(p_actual - p_anterior) > tolerancia and g(p_actual) != 0) :
        print(f"{cantidad_de_iteraciones}: p_0: {p_anterior}, p: {p_actual}, diferencia: {abs(p_actual-p_anterior)}")
        p_anterior = p_actual
        p_actual = g(p_anterior)
        cantidad_de_iteraciones += 1
    print(f"La raíz aproximada con un error menor a {tolerancia} es {p_actual} y se consiguio despues de {cantidad_de_iteraciones} iteraciones.")

def calcular_p_newton_raphson(p, multiple):
    return p - (g(p) * g_prima(p))/(g_prima(p)**2 - g(p) * g_2_prima(p)) if multiple else p - g(p) / g_prima(p)

def newton_raphson(semilla, tolerancia, multiple= False):
    p_anterior = semilla
    tolerancia_tope = 100
    p_actual = calcular_p_newton_raphson(p_anterior, multiple)
    cantidad_de_iteraciones = 0

    while abs(p_anterior - p_actual) > tolerancia:
        print(f"{cantidad_de_iteraciones}: p_0: {p_anterior}, p: {p_actual}, diferencia: {abs(p_actual-p_anterior)}")
        p_anterior = p_actual
        p_actual = calcular_p_newton_raphson(p_anterior, multiple)
        cantidad_de_iteraciones += 1
        if abs(p_anterior - p_actual) > tolerancia_tope:
            print('El metodo no converge a la raiz')
            return

    print(f"La raíz aproximada con un error menor a {tolerancia} es {p_actual} y se consiguio despues de {cantidad_de_iteraciones} iteraciones.")

def _metodo_secante(p_0, p_1, tolerancia, iteraciones):
    if iteraciones > MAX_ITERACIONES:
        print('El método no converge')
        return
    p_actual = p_1 - (g(p_1)*(p_1 - p_0))/(g(p_1)-g(p_0))
    print(f'{iteraciones}_) p: {p_actual}, f(p): {g(p_actual)}')
    if abs(p_actual - p_1) < tolerancia:
        print(f"La raíz aproximada con un error menor a {tolerancia} es {p_actual} y se consiguio despues de {iteraciones + 1} iteraciones.")
        return
    return _metodo_secante(p_1, p_actual, tolerancia, iteraciones + 1)

def metodo_secante(p_0, p_1, tolerancia):
    return _metodo_secante(p_0, p_1, tolerancia, 0)