"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★

예시
<입력>
숫자를 입력하세요 : 5

<출력>
    ★
   ★★
  ★★★
 ★★★★
★★★★★  
 ★★★★
  ★★★
   ★★
    ★


"""
num = int(input("숫자를 입력하세요 : "))

# 공백 만들기
def make_space(time):
    add_space = ""
    for i in range(0, time - 1):
        add_space = " " + add_space
    return add_space

# 별 만들기
def make_star(time):
    star = ""
    for i in range(0, time):
        star = "★" + star
    return star

# 반복문 이용 다이아몬드 만들기
## 공백과 별은 반비례 관계
## 별의 갯수가 입력된 숫자 수를 기준으로 대칭
def draw_star(num):
    for i in range(0, num):
        print(make_space(num - i) + make_star(i + 1))
    for j in range(0, num - 1):
        print(make_space(j+2) + make_star(((num-1) - j)))
    return
draw_star(num)