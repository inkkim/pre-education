'''
4.
다중상속을 이용하여 카드사의 클래스를 만들고
영화카드는 20% 할인
마트카드는 10% 할인
교통은 10%할인을 받는 카드 class를 구현하시오


테스트코드
<입력>
multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

<출력>
카드가 발급 되었습니다.
20000이 충전되었습니다.
마트에서 4500.0원을 사용했습니다.
영화관에서 8000.0원을 사용했습니다.
교통에서 1800.0원을 사용했습니다.
잔액이 5700.0원 입니다
'''


class Card():

    # 충전 기능
    ## 다시 충전하려면 ?
    def charge(self, charge):
        self.charge = charge
        print("{}원이 충전되었습니다.".format(self.charge))

    # 소비 기능
    ## 영화관에서 카드 사용 시 20% 할인
    def consume(self, con, place):
        if place == '영화관':
            con *= 0.8
            con = int(con)
        if self.charge < con:
            print("잔액이 부족합니다.")
            return
        self.charge = self.charge - con
        self.place = place
        print("{}에서 {}원 사용했습니다.".format(place, con))

    # 잔액출력 기능
    def print(self):
        print("잔액이 {}원 입니다.".format(self.charge))

# Card() 클래스로부터 상속받는 자식 클래스
class Multi_card(Card):

    # 생성자
    def __init__(self):
        print('카드가 발급 되었습니다.')

    # 마트와 교통 부문 10% 할인 기능 추가
    def consume(self, con, place):
        if (place == '마트') | (place == '교통'):
            con *= 0.9
        Card.consume(self, con, place)

multi_card=Multi_card()
multi_card.charge(20000)
multi_card.consume(5000,'마트')
multi_card.consume(10000,'영화관')
multi_card.consume(2000,'교통')
multi_card.print()

