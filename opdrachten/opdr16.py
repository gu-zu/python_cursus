getal = int(input("Geef een getal "))

print(getal, end="")
while getal > 0:
    getal -= 1
    print(",", getal, sep="", end="")

print()
