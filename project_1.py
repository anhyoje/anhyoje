import random



han = ["한식1", "한식2", "한식3"]
il = ["일식1", "일식2", "일식3"]
jung = ["중식1", "중식2", "중식3"]

def bab():
    lunch = input("한식, 중식, 일식 중 하나를 선택하세요.")
    if lunch == "한식":
        print(f"{lunch} 중에서 {random.choice(han)}이 선택되었습니다.")
    elif lunch == "일식":
        print(f"{lunch} 중에서 {random.choice(il)}이 선택되었습니다.")
    elif lunch == "중식":
        print(f"{lunch} 중에서 {random.choice(jung)}이 선택되었습니다.")
    else:
        print("선택지에 없습니다.")
        bab()
bab()
