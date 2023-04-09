# solicitamos al usuario los valores
# de los coeficientes a, b y c.
print("==================================================")
initial = True
while initial:
    print("Escribe C para terminar y salir")
    print("Este programa resuelve una ecuación")
    print("cuadratica de la forma ax² + bx + c = 0")
    a = float(input("Escribe el valor de a: "))
    b = float(input("Escribe el valor de b: "))
    c = float(input("Escribe el valor de c: "))

    # discriminante b²-4ac
    dis = b**2 - 4*a*c

    if dis > 0:
        print("Dos soluciones reales")
    elif dis == 0:
        print("Soluciones repetidas")
    else:
        print("Soluciones complejas")

    x1 = (-b + dis**0.5)/2*a # solucion 1
    x2 = (-b - dis**0.5)/2*a # solucion 2
    # se imprimen en pantalla los resultados
    print(f"Las soluciones son x =  {x1:.2f}; x = {x2:.2f}")
    print("==================================================")
    finish = input("Presiona F para terminar ó \
                   \ncualquier tecla para continuar: ")
    # close the program
    if finish.upper() == 'F':
        break
    print("==================================================")