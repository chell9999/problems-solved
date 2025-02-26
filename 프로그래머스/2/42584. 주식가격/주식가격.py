def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            top_idx = stack.pop()
            answer[top_idx] = i - top_idx

        stack.append(i)

    while stack:
        top_idx = stack.pop()
        answer[top_idx] = n - top_idx - 1

    return answer
