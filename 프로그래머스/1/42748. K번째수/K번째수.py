def solution(array, commands):
    answers = []
    for i, j, k in commands:
        piece = sorted(array[i-1:j])

        if i == j:
            target_num = piece[-1]
        else:
            target_num = piece[k-1]
        answers.append(target_num)

    return answers
        
        