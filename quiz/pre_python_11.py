"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""
# 유클리드 호제법
def gcd(a, b):
    # a > b 전제
    if a < b:
        a, b = b, a
    # 재귀함수의 b(a%b)가 0이면 a(b)가 최대공약수
    if b == 0:
        return a
    # a가 b로 나누어 떨어지면 b가 최대공약수
    if (a % b) == 0:
        return b
    # 아니면 a를 b로 나눈 나머지값으로 b를 나눔
    else:
        return gcd(b, a%b)
print(gcd(12, 6))