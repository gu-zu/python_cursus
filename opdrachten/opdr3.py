prijs = 24.95
inkoop = prijs * 0.6
verzending = 0.75  # 3 voor eerste
winst = prijs - inkoop - verzending
verkocht = 60

print(winst * verkocht - (3 - verzending))
