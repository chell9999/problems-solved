def solution(citations):
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations):
        print(f"{i}, {c} if {c} < {i+1}")
        # 조건 1: h 번 이상 인용된 논문이 h 편 이상
        # 조건 2: 나머지 논문이 h 번 이하 인용
        if c <= i:
            return i
        
    return len(citations) 