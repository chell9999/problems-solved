import sys

N = int(sys.stdin.readline().strip())
scores = list(map(int, sys.stdin.readline().strip().split()))


def fabricate_score(score, best_score):
    return score / best_score * 100


best_score = max(scores)

scores_fabricated = []

for score in scores:
    scores_fabricated.append(fabricate_score(score, best_score))

print(sum(scores_fabricated) / len(scores_fabricated))
