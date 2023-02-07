import functions as f
# from functions import my_add, ... (Für einzelne Funktionen)
# from functions import *

x = float(input("Erste Zahl: "))
y = float(input("Zweite Zahl: "))
operator = input("(+ - * /) Rechenart: ")

match operator:
  case "+":
    print(f.add(x,y))
  case "-":
    print(f.sub(x,y))
  case "*":
    print(f.mult(x,y))
  case "/":
    print(f.div(x,y))
  case other:
    print("Rechenart nicht möglich!")