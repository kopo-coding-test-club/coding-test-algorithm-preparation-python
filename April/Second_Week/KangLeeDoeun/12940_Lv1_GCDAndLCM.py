import math
def gcd(n, m):
    if n < m:
        n, m = m, n
        
    while m:
        n, m = m, n % m
    return n


def solution(n, m):
    answer = []
    # answer.append(math.gcd(n, m))
    answer.append(gcd(n, m))
    answer.append(n*m / gcd(n, m))
    # answer.append(n*m/math.gcd(n, m))
    return answer