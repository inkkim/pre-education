"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']

예시
<입력>
print(new_list)

<출력>
['exit', 'hi', 'playdata', 'intro']

"""
file = ['exit.py','hi.py','playdata.hwp','intro.jpg']

# file 요소를 " " 구분자로 str1의 문자열 형태로 반환
str1 = " ".join(file)
print("1", str1)

name = []
# str1 요소 1개당 name 리스트의 요소로 반환
for i in str1:
    name.append(i)
name.append(" ")
print("2", name)

# '.'을 포함한 확장자명 제거
for k in name:
    if k == ".":
        index = name.index(k)
        del (name[index])
        while name[index] != " ":
            del (name[index])
print("3", name)

# " " 구분자를 기준으로 문자열로 반환
a = ""
a = " ".join(name)
print('4', a)

# 불필요한 띄어쓰기 제거
b = a.replace("  ", "-")
c = b.replace(" ", "")
print('5', c)

# "-" 구분자를 기준으로 리스트로 반환
new_list = []
new_list = c.split("-")
del new_list[len(new_list) - 1]
print(new_list)