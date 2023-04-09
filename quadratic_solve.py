# solicitamos al usuario los valores
# de los coeficientes a, b y c.
print("Este programa resuelve una ecuación")
print("cuadratica de la forma ax² + bx + c = 0")
a = float(input("Escribe el valor de a: "))
b = float(input("Escribe el valor de b: "))
c = float(input("Escribe el valor de c: "))

# discriminante b²-4ac
dis = b**2 - 4*a*c

x1 = (-b + dis**0.5)/2*a # solucion 1
x2 = (-b - dis**0.5)/2*a # solucion 2
# se imprimen en pantalla los resultados
print("Las soluciones son x = ", x1, "; x = ", x2)