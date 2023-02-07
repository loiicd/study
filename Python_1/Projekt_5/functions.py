def print_ux_star(header: str, value: str):
  border = ""
  for i in range(len(value) + 8):
    border += "*"

  print()
  print(header)
  print(border)
  print(f"*** {value} ***")
  print(border)