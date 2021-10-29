lengte = float(input("Voer je lengte in(meters) "))
gewicht = float(input("Voer je gewicht in(kilo's) "))

# nieuwe formule:
bmi = round((gewicht * 1.3) / (pow(lengte, 2.5)), 1)

print("Je BMI is", bmi, ", dat betekent dat je ", end="")
if bmi < 18:
    print("ondergewicht hebt")
elif bmi < 25:
    print("gezond bent")
elif bmi < 30:
    print("overgewicht hebt")
elif bmi < 40:
    print("obesitas hebt")
else:
    print("een zwart gat bent geloof ik")
