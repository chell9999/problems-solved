def solution(numbers):

    str_numbers = list(map(str, numbers))

    from functools import cmp_to_key

    def compare(x, y):
        if x + y > y + x:
            return -1  
        elif x + y < y + x:
            return 1  
        else:
            return 0  

    str_numbers.sort(key=cmp_to_key(compare))

    # 4. 정렬된 배열을 이어붙이기
    answer = ''.join(str_numbers)

    # 5. 모든 숫자가 0인 경우 처리 (ex. [0, 0, 0] -> "0")
    if answer[0] == '0':
        answer = '0'

    return answer
