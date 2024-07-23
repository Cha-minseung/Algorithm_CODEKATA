def solution(n):
    if int(n**0.5) == n**0.5: # n이 제곱수 인지 판별
        return ((n**0.5)+1)**2 # n이 제곱수라면, n+1의 제곱수 반환
    else :
        return -1 #제곱수가 아니면, -1반환