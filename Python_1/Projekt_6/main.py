class A:
  def __init__(self, x: int, y: str):
    self.x = x      # puplic
    self.__y = y    # private

if __name__ == "__main__":
  a = A(x = 3, y = "hi")
  print(a.x)

  a.x = 1
  print(a.x)


# Aufgaben
class Kreis:
  def __init__(self, radius: float, surface: float):
    self.__radius = radius
    self.surface = surface

  def calculate_surface(self, radius: float) -> float:
    surface = 2 * 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 * radius
    return surface

kreis = Kreis(radius = 3, surface = 0)
kreis.calculate_surface()
print(kreis.surface)
