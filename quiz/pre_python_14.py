"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오.

예시
<입력>
EAST
<출력>
east

<입력>
hello
<출력>
HELLO

<입력>
안녕
<출력>
입력 형식이 잘못되었습니다.

"""
pd_str = str(input())

def pd_upper(pd_str):
    for i in range(0, len(pd_str)):
        if ((pd_str[i] >= chr(65)) & (pd_str[i] <= chr(90))): # 대문자
            pd_str = pd_str.lower() # 대문자 => 소문자
            return pd_str
        elif ((pd_str[i]  >= chr(97)) & (pd_str[i] <= chr(122))): # 소문자
            pd_str = pd_str.upper() # 대문자 => 소문자
            return pd_str
    return "입력 형식이 잘못되었습니다."
print(pd_upper(pd_str))

