def longest_common_subsequence(s1: str, s2: str) -> int:
    len_s1, len_s2 = len(s1), len(s2)
    lcs = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    
    return lcs[-1][-1]

# 입력 받기
s1 = input().strip()
s2 = input().strip()
print(longest_common_subsequence(s1, s2))
