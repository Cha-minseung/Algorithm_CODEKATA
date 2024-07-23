def solution(n):
    x = list(str(int(n)))
    x.sort(reverse=True)
    
    return int("".join(x))