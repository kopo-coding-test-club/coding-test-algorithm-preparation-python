def solution(n):
    answer = 0
    str = div(n)
    answer = int(str, 3)
    return answer

def div(n):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    
    return rev_base
    
