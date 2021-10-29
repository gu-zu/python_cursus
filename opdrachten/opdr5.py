# comments gebasseerd op originele waarden voor nr 1 en nr 2:
# nr1=5
# nr2=4

nr1 = 11
nr2 = 10
nr3 = 5
print(nr3 / (nr1 % nr2))  # 5 / 1
nr1 = nr1 + 1  # 6
print(nr3 / (nr1 % nr2))  # 5 / 2
nr1 = nr1 + 1  # 7
print(nr3 / (nr1 % nr2))  # 5 / 3
nr1 = nr1 + 1  # 8
print(nr3 / (nr1 % nr2))  # 5 / 0 (8%4=0) geeft divide by 0 error
