num = 1
lastnum = 0

print("1", end="")

while num < 1000:
    new = num + lastnum
    if new > 1000:
        print()
        break
    lastnum = num
    num = new
    print(",", num, sep="", end="")
