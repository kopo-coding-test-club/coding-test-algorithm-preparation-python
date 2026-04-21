def solution(n, m):
    answer = []
    large_number = min(n, m)
    small_number = max(n, m)
    gcd = 0
    lcm = 0
    while small_number > 0:
        large_number , small_number = small_number, large_number % small_number
    gcd = large_number
    lcm = n * m / gcd
            
    return [gcd, lcm]