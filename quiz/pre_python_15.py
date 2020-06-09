"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""

reg = input("주민등록번호 : ")
def MaleOrFemale(reg):
    split = reg.split('-')
    front = str(split[0])
    back = str(split[1])
    # 20C 출생은 주민등록번호 뒷자리수가 1과 2로 시작
    if front[0] == "0":
        if back[0] == "3":
            return "남자"
        elif back[0] == "4":
            return "여자"
    # 21C 출생은 주민등록번호 뒷자리수가 3과 4로 시작
    else:
        if back[0] == "1":
            return "남자"
        elif back[0] == "2":
            return "여자"
    return "올바른 입력이 아닙니다."
print(MaleOrFemale(reg))