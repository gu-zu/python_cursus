from math import sqrt

zijde1 = int(input("Voer de lengte van de eerste zijde in "))
zijde2 = int(input("Voer de lengte van de tweede zijde in "))


def sqr(getal):
    return getal * getal


def pythagoras(zijde1, zijde2):
    return sqrt(sqr(zijde1) + sqr(zijde2))


print("Lengte van de schuine zijde is", pythagoras(zijde1, zijde2))
