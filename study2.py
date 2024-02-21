def solution(s):
# s가 문자열임을 나타내주기? str(s)
# 문자열의 길이가 4 나 6인지 함수를 써서 나타내보기
# if 뒤에는 반드시 불문으로
    if s.isdigit():
        if len(str(s)) == 4 \
            or len(str(s)) == 6:
                return True
        else:
            return False
    else:
        return False
    #위의 두 4,6번 길이가 참일 때

    # 새로운 이프함수로 숫자로만 구성된걸 나타내는 식?
    # GPT한테 물어본 숫자만 있는지 알아보는 함수 isdigit(), isnumeric(), isdecimal()
    # 위 함수를 제외한 방법으로는 try-except

#    answer=s.isdigit()
#    return answer

# 마지막에 숫자열임을 판단하는 if문과 길이 4,6을 판단하는 if문의 순서를 바꿔서 일단 정답처리받음..
