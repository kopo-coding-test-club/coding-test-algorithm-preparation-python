def solution(n):
    prime_number_set = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in prime_number_set:
            prime_number_set -= set(range(2 * i, n + 1 , i));
    return len(prime_number_set)