def solution(nums):
    answer = 0
    n = len(nums) // 2;
    s = len(set(nums))
    answer = min(n, s);
    return answer
