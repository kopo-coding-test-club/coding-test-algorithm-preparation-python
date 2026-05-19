def solution(nums):
    # N마리 중 N/2 가져가
    # 번호가 존재한대
    # 3번 1번 2번 3번 => 3번이 2마리
    # 최대한 많은 종류의 폰켓몬을 포함해서 N/2마리 선택
    a = len(set(nums))
    n = len(nums)/2
    return n if a > n else a