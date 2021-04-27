#1
#11
#111
#1111
#11111
for a in range(1, 6):
    print("1"*a)

#10000
#11000
#11100
#11110
#11111
for a in range(1, 6):
    print("1"*a + "0"*(5-a))

#00100
#01110
#11111
#01110
#00100
for a in range(1, 6):
    a = a-3
    if a<0:
        a = -a
    else:
        a=a
    print("0"*a + "1"*(5-a*2) + "0"*a)
