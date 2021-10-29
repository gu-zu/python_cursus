getal1 = int(input("Voer het eerste getal in "))
getal2 = int(input("Voer het tweede getal in "))
getal3 = int(input("Voer het derde getal in "))

print(
    "het grootste getal is",
    max(getal1, getal2, getal3),
    ", de klienste",
    min(getal1, getal2, getal3),
    "en het gemiddelde is",
    (getal1 + getal2 + getal3) / 3,
)
