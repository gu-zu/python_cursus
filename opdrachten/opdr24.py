str = input("Geef een woord ")

print(str, "achterstevoren is ", end="")
for v in reversed(str):
    print(v, end="")
print()
