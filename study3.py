def solution(price, money, count):
   # answer = -1   < 처음 문제 켤 때 있는건데 왜 -1이 명시되어있는지 모르겠음.

#탈 때마다 달라지는 가격의 합산을 요약?해보기
    total = 0
    for i in range(1,count+1):
        total += price * i

#소지금에서 이용료를  뺀 가격을 0과 비교하기 if문?
    if money < total:
        return total-money
    else:
         return 0


#money에서 count마다마다 달라지는 price들을 모두 더해서 빼주기.
