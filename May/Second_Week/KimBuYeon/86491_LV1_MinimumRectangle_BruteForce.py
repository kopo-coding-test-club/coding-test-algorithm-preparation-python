def solution(sizes):
    big_numbers = []
    small_numbers = []
    for size in sizes:
        width , height = size
        big_num, small_num = (width, height) if width > height else (height , width)
        big_numbers.append(big_num)
        small_numbers.append(small_num)
        
    return max(big_numbers) * max(small_numbers)