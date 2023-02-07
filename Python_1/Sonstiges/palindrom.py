def is_palindrom(value: str) -> bool:
  value = value.lower()
  list_1 = list(value)
  list_2 = list_1[::-1]

  if list_1 == list_2:
    return True
  else:
    return False

# def euler_number(x: int) -> float:
#   e = 1.0
#   while x > 0:
#     e = 1 + (e / x)
#     x = x - 1
#   return e

value = str(input("Eingabe Palindrom: "))
print(is_palindrom(value))

# value = int(input("Eingabe Euler: "))
# print(euler_number(value))