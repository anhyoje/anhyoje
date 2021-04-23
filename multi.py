first = int(input("몇 단을 출력하시겠습니까?"))

for second in range(1,10):
    if second <= 5:
        print(f"포맷 1번 {first} * {second} = {first*second}" )
    else :
        print("포맷 2번 {} * {} = {}". format(first, second, first*second))
