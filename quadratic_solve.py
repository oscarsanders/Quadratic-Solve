# this function check input values
def criteria():
  global a,b,c
  while True:
    try:
      a = float(input("Write the value of a: "))
      b = float(input("Write the value of b: "))
      c = float(input("Write the value of c: "))

      # discriminant b²-4ac
      dis = b**2 - 4*a*c

      if dis > 0:
        print("Two real solutions")
      elif dis == 0:
        print("Repeated solutions")
      elif dis < 0:
        print("Complex solutions")

      return dis
    except ValueError:
      print("Error: The input value must be a number. Try again.")
      
# main program
print("==================================================")
while True:
    print("This program solve a quadratic")
    print("equation of the form ax² + bx + c = 0")
    
    dis = criteria()

    x1 = (-b + dis**0.5)/2*a # solution 1
    x2 = (-b - dis**0.5)/2*a # solution 2
    # print solution on screen
    print(f"The solutions are x =  {x1:.2f}; x = {x2:.2f}")
    print("==================================================")
    finish = input("Press F to finish or \
                   \npress any key to continue: ")
    # close the program
    if finish.upper() == 'F':
        break
    print("==================================================")