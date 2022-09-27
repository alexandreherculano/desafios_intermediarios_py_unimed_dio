letra = input()

import string

alfabeto = string.ascii_uppercase
alfabeto_lista = list(alfabeto)

print(alfabeto_lista.index(letra)+1)