# Funcion perimetro del circulo
def percir(r):
    from math import pi
    P=2*pi*r
    return P

# Funcion area del circulo
def areacir(r):
    from math import pi
    A=pi*(r**2)
    return A

# Programa que calcula area y perimetro de un circulo
r=int(input('Ingresa el radio del circulo : ' ))
print('el area del circulo es : ' + str(areacir(r)))
print('El perimetro del circulo es : ' + str(percir(r)))