# --------------------------
# Dozent:  Jannik Wiessler
# Modul:  Python
# Kurs:   WWI22A
# --------------------------



# -------------------------
# --- Dienstag 15.11.22 ---
# -------------------------


# --- Variable ---
a = 5
b = 10


# --- Datatypes ---
# Numeric
c = 5                   # int         -   integer
d = 1.5                 # float

# Text
e = "Hello World"       # string
f = " wie gehts?"

# Boolean
g = True                # bool        -   boolean


# --- Calculate ---
a + b                   # calculate   -   rechen
e + f                   # compile     -   kompelieren


# --- Functions ---
input()                 # input
print(e)                # output


# ---------------------------
# --- Donnerstag 17.11.22 ---
# ---------------------------

def my_func(**kwargs):  # erstellt direkt dict
  print(kwargs) #output = {'a': 1, 'b': 'hallo', 'c': 4, 'h': [2, 3, 4]}

my_func(a=1, b="hallo", c=4, h=[2,3,4])