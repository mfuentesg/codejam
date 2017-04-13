import re

def to_regex(pattern):
    pr = pattern

    for pi in re.findall(r'\(\w+\)', pattern):
        pr = pr.replace(pi, '({})'.format('|'.join(pi[1:-1])))

    return pr

def matcher(pattern):
    r = re.compile(to_regex(pattern))
    return len(list(filter(r.match, known_words)))

L, D, N = [int(c) for c in input().strip().split(' ')]
known_words = [input().strip() for i in range(0,D) ]
for i in range(1, N + 1):
    print('Case #{}: {}'.format(i, matcher(input().strip())))

