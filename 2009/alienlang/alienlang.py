import re

def matcher(pattern):
    r = re.compile(pattern.replace('(', '[').replace(')', ']'))
    return len(list(filter(r.match, known_words)))

L, D, N = [int(c) for c in input().strip().split(' ')]
known_words = [input().strip() for i in range(0,D) ]
for i in range(1, N + 1):
    print('Case #{}: {}'.format(i, matcher(input().strip())))

