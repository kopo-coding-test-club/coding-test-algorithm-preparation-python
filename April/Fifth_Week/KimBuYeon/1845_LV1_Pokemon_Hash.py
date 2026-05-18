def solution(nums):
    m = len(nums) // 2
    count_dict = {}
    for num in nums:
        if num in count_dict:
            continue
        else:
            count_dict[num] = 1
    return min(len(count_dict), m)