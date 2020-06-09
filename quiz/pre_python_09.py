"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F

예시
<입력>
score : 88

<출력>
A

"""
score = int(input("score : "))

def grade(score):
    if (score <= 100) & (score >= 81): # 81 ~ 100
        print("A")
    elif (score <= 80) & (score >= 61): # 61 ~ 80
        print("B")
    elif (score <= 60) & (score >= 41): # 41 ~ 60
        print("C")
    elif (score <= 40) & (score >= 21): # 21 ~ 40
        print("D")
    elif (score <= 20) & (score >= 0): # 0 ~ 20
        print("F")
    return

grade(score)
