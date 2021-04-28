import random

ROCK = "바위"
SICSSOR = "가위"
PAPER = "보"
computer_list = [ROCK, SICSSOR, PAPER]


h_score = 0
c_score = 0

# while h_score < 3 and c_score < 3:
#     computer_choice = random.choice(computer_list)
#     user_choice = input("{}, {}, {} 중 고르시오.". format(ROCK, SICSSOR, PAPER))
#     if user_choice == computer_choice:
#         print("비겼습니다.")
#     elif user_choice not in computer_list:
#         print("잘못 입력되었습니다.")
#     elif ((user_choice == ROCK and computer_choice == SICSSOR)
#         or (user_choice == SICSSOR and computer_choice == PAPER)
#         or (user_choice == PAPER and computer_choice == ROCK)):
#             h_score = h_score + 1
#             print("이겼습니다.")
#     else:
#         c_score = c_score + 1
#         print("졌습니다.")
# if h_score == 3:
#     print("최종승리")
# else:
#     print("lose")





while h_score < 3 and c_score < 3:
    game = input("가위, 바위, 보 중 하나를 내시오.")
    c_game = ["가위", "바위", "보"]
    A = random.choice(c_game)
    if game=="바위":
        if A == "바위":
            print("컴퓨터가 {}를 내어 비겼습니다.". format(A))
        elif A == "보":
            c_score = c_score + 1
            print("컴퓨터가 {}를 내어 졌습니다.". format(A))
        else:
            h_score = h_score + 1
            print("컴퓨터가 {}를 내어 이겼습니다.". format(A))
    elif game=="보":
        if A == "보":
            print("컴퓨터가 {}를 내어 비겼습니다.". format(A))
        elif A == "가위":
            c_score = c_score + 1
            print("컴퓨터가 {}를 내어 졌습니다.". format(A))
        else:
            h_score = h_score + 1
            print("컴퓨터가 {}를 내어 이겼습니다.". format(A))
    else:
        print("잘못된 값을 입력하였습니다.")

if h_score == 3:
    print("최종승리")
else:
    print("최종패")
