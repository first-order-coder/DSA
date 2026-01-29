def is_multiple(n,m):
    if m == 0: #must think about edge cases
        return n == 0
    return n % m == 0

tests = [
    (12, 3, True),
    (12, 5, False),
    (0, 7, True),
    (7, 0, False),
    (0, 0, True)
]

for n,m,expected in tests:
    result = is_multiple(n, m)
    print(f'is_multiple({n}, {m}), = {result} and expected result:{expected}')
