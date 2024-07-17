def solution(n):
    
    answer = 0 # 선언과 동시에 초기화
    
    for i in range(n + 1): # for 변수 i range():
        if i % 2 == 0: # if i%2 == 0 짝수 % = 몫
            answer += i # answer = answer + 1  
    
    return answer