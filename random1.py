import random

print(random.random())



list = []
for num in range(1, 10):
    list.append(num)

print(list)
test = int(random.choice(list))

if test > 5:
    print(f"UR num is {test} so lucky!")
else:
    print(f"UR num {test}, so Sad")
