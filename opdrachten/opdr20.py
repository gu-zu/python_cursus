num = 5


def digit(num):
    if num < 10:
        return " " + str(num)
    else:
        return str(num)


print(". |", end="")
for x in range(num):
    print("", x + 1, "", end="")
print()
for x in range(num):
    print("---", end="")
print("---")

for i in range(num):  # loop voor y as
    i += 1
    print(i, "|", end="")
    for j in range(num):  # loop voor x as
        j += 1
        print(digit(i * j), "", end="")
    print()
