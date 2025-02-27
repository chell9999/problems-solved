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

    answer = ''.join(str_numbers)

    if answer[0] == '0':
        answer = '0'

    return answer
