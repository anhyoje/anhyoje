

def gugu():

    try:
        first = int(input("몇 단을 출력하시겠습니까?"))
        if first < 2 or first > 9:
            print("2와 9사이의 정수를 입력해주세요")
            gugu()
        else:
            for second in range(1,10):
                A = f"{first} * {second} = {first*second}"
                print(A)
    except ValueError:
        print("정수만 입력해주세요.")
        gugu()
    except:
        print("고객센터에 문의하세요.")
        gugu()
gugu()
