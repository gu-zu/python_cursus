a = float(input("Geef de waarde van a "))
b = float(input("Geef de waarde van b "))
c = float(input("Geef de waarde van c "))

d = b * b - 4 * a * c
print("De discriminant is ", b, "^2 - 4 * ", a, " * ", c, " = ", d, sep="")
# minder dan nul is geen uiktkomsten, 0 is 1 uitkomst meer dan nul is meer uitkomsten
if d < 0:
    print("Geen uitkomsten")
elif d == 0:
    print("1 uitkomst")
else:
    print("Meerdere uitkomsten")
