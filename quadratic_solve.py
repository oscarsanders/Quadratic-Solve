# this function check input values
def criteria():
  global a,b,c
  while True:
    try:
      # valor = input("Ingresa un número: ")
      a = float(input("Write the value of a: "))
      b = float(input("Write the value of b: "))
      c = float(input("Write the value of c: "))

      # discriminant b²-4ac
      dis = b**2 - 4*a*c

      if dis > 0:
        print("Dos soluciones reales")
      elif dis == 0:
        print("Soluciones repetidas")
      elif dis < 0:
        print("Soluciones complejas")

      # x1 = (-b + dis**0.5)/2*a # solucion 1
      # x2 = (-b - dis**0.5)/2*a # solucion 2
      # print solution on screen
      # print(f"Las soluciones son x =  {x1:.2f}; x = {x2:.2f}")

      return dis
    except ValueError:
      # if valor.upper() == 'F':
      #   break
      print("Error: El valor ingresado no es un número válido. Intenta de nuevo.")
      
# main program
print("==================================================")
while True:
    print("This program solve a quadratic")
    print("equation of the form ax² + bx + c = 0")
    
    dis = criteria()

    x1 = (-b + dis**0.5)/2*a # solucion 1
    x2 = (-b - dis**0.5)/2*a # solucion 2
    # print solution on screen
    print(f"Las soluciones son x =  {x1:.2f}; x = {x2:.2f}")
    print("==================================================")
    finish = input("Presiona F para terminar ó \
                   \ncualquier tecla para continuar: ")
    # close the program
    if finish.upper() == 'F':
        break
    print("==================================================")