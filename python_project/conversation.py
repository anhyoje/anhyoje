# 화면에 데이터 출력하기
print(1 + 2)

# 사용자로부터 값 받기
# 변수활용
name = input("당신의 이름은 무엇입니까?")
print(name + "안녕하세요")
print("주소라 사랑해")

# 효제 연습
name = ["aaa", "bbb", 123, 123.45, ['aaa', 'ddd']]
print(name)
print(type(name))
for names in name:
    if type(names) == str:
        print("안녕하세요," + names)
    elif type(names) == int:
        print(str(names) + "은(는) 존재하지 않는 이름입니다.")
    else:
        print(str(names) + "잘못된 이름입니다.")
