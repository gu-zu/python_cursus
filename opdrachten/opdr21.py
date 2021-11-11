# == NIET OPDR 21 ==
"""
s1 = "appel"
s2 = "banaan"
print(s1)
print(s2)
print(s1 + s2)
print(3 * s1)
print(s2 * 3)
print(2 * s1 + 2 * s2)
"""

str = input("Geef een woord ")

print("met for ... in loop")

for letter in str:
    print(letter)

print("met range en len:")

for i in range(len(str)):
    print(str[i])
