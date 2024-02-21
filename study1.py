#두개의 행렬 arr1 /2를 입력받아,
#행렬덧셈의 결과를 반환하는 함수완성시키기

#arr1, arr2 리스트
arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
#입력으로 주어진 두 행렬의 크기가 같은지 확인합니다.
#결과 행렬을 저장할 빈 리스트를 생성합니다. def 아래 answer?
#이중 반복문을사용하여 각 위치의 값을 더한 후, 결과 행렬에 추가합니다.
#결과 행렬을 반환합니다.

#arr1,2를 매개로 한 solution 함수 정의
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        #위는 행의 갯수!
        blank = []
        for j in range(len(arr1[0])):
            #위는 열의 갯수
            plus=arr1[i][j]+arr2[i][j]
            blank.append(plus)
        answer.append(blank)

            #결과 행렬에 추가한다 = 리스트에 요소 추가를 한다. append?
    return answer
