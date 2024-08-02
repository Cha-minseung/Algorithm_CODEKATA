def solution(s):
    center = int(len(s)/2)
    if len(s) % 2 != 0:     # s의 문자열 길이가 홀수라면,
        return s[center]    # s의 중간에 있는 문자를 반환
    else:                   # s의 문자열 길이가 짝수라면,
        return s[center-1:center+1]     # 중간에서 양 옆으로 반환