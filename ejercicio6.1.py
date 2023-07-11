"""
Escribir funciones que dada una cadena de caracteres:
    a) Imprima los dos primeros caracteres.
    b) Imprima los tres últimos caracteres.
    c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
    d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'
    e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
    'reflejoojelfer'.
"""


def imprimir_primeros_dos_caracteres(cadena):
    # Imprime los dos primeros caracteres de una cadena.

    print(f"Cadena: {cadena}")
    print(f"Cadena primeros dos caracteres: {cadena[:2]}")
    print()


print()
# imprimir_primeros_dos_caracteres("perro")
# imprimir_primeros_dos_caracteres("película")
# imprimir_primeros_dos_caracteres("Belén")
# imprimir_primeros_dos_caracteres("pájaro")

def imprimir_ultimos_tres_caracteres(cadena):
    # Imprime los ultimos tres caracteres de una cadena.

    inicio = len(cadena) - 3

    print(f"Cadena: {cadena}")
    print(f"Cadena ultimos tres caracteres: {cadena[inicio:]}")
    print()

# imprimir_ultimos_tres_caracteres("perro")
# imprimir_ultimos_tres_caracteres("película")
# imprimir_ultimos_tres_caracteres("Belén")
# imprimir_ultimos_tres_caracteres("pájaro")


def imprimir_cadena_cada_dos_caracteres(cadena):
    # Imprime dicha cadena cada dos caracteres. Ej: "recta" debería imprimir "rca".

    print(f"Cadena: {cadena}")
    print(f"Cadena cada dos caracteres: {cadena[::2]}")
    print()

# imprimir_cadena_cada_dos_caracteres("perro")
# imprimir_cadena_cada_dos_caracteres("película")
# imprimir_cadena_cada_dos_caracteres("Belén")
# imprimir_cadena_cada_dos_caracteres("pájaro")


def inverso_cadena(cadena):
    # Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'

    print(f"Cadena: {cadena}")
    print(f"Inverso cadena: {cadena[::-1]}")
    print()

# inverso_cadena("perro")
# inverso_cadena("película")
# inverso_cadena("Belén")
# inverso_cadena("pájaro")


def reflejo_cadena(cadena):
    #  Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime 'reflejoojelfer'.   

    print(f"Cadena: {cadena}")
    print(f"Reflejo cadena: {cadena}{cadena[::-1]}")
    print()

reflejo_cadena("perro")
reflejo_cadena("película")
reflejo_cadena("Belén")
reflejo_cadena("pájaro")