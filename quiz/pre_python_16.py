"""16. 1부터 50 까지의 숫자 중에서 3의 배수를 공백으로 구분하여 출력하시오.



<출력>
3  6  9  12  15  18  21  24  27  30  33  36  39  42  45  48  

"""
result = ""
for k in range(50, 1, -1):
    if k % 3 == 0:
        a = str(k) + " "
        result = a + result
print(result)