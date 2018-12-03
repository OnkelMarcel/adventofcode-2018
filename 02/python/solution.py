from collections import defaultdict

inputs = open('../input.txt').read().strip().split('\n')

twice = 0
three = 0

# Part one

for i in inputs:
    letters = defaultdict(int)
    for c in i:
        try:
            letters[c] += 1
        except KeyError:
            letters[c] = 1
    if 2 in letters.values():
        twice += 1
    if 3 in letters.values():
        three += 1

print(f'Twice: {twice} | Three: {three} | Checksum: {twice * three}')

print('---------------------------------------------------')

# Part two


def different_chars_count(one, two):
    count = 0
    for i in range(len(one)):
        if one[i] == two[i]:
            count += 1
    return len(one) - count


def same_chars(one, two):
    chars = []
    for i in range(len(one)):
        if one[i] == two[i]:
            chars.append(one[i])
    return chars


for i in inputs:
    for j in inputs:
        count = different_chars_count(i, j)
        if count == 1:
            print(f'One: {i} | Two: {j}')
            print(f'Same chars: {"".join(same_chars(i, j))}')
            exit()
