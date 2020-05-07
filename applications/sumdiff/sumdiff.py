"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# TODO: Implement me.
vals = {}
sums = {}
difs = {}
for num in q:
    vals[f'f({num})'] = f(num) 

for val1 in vals:
    for val2 in vals:
        sums[f'{val1} + {val2}'] = ((vals[val1] + vals[val2]), f'{vals[val1]} + {vals[val2]}')
        if vals[val1] >= vals[val2]:
            difs[f'{val1} - {val2}'] = ((vals[val1] - vals[val2]), f'{vals[val1]} - {vals[val2]}')

for sum_ in sums:
    for dif in difs:
        if sums[sum_][0] == difs[dif][0]:
            print(f'{sum_} = {dif}  {sums[sum_][1]} = {difs[dif][1]}')