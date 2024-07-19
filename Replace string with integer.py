def solution(s):
    answer = 0
    if s[1] == '-':
        return int(s[:-1])
    else:
        return int(s)

    return answer