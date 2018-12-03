import re

inputs = open('../input.txt').read().strip().split('\n')


def draw_fabric():
    out = []
    for i in range(0, 1000):
        out.append(['.' for j in range(1000)])
    return out


def draw_claim(fabric, claim):
    x = claim.left_space
    y = claim.top_space
    for i in range(claim.width):
        for j in range(claim.height):
            if fabric[x + i][y + j] == 'O' or fabric[x + i][y + j] == 'X':
                fabric[x + i][y + j] = 'X'
            else:
                fabric[x + i][y + j] = 'O'
    return fabric


def claim_from_input(input):
    _id = re.findall(r"(?<=#)\d+", input)[0]
    left_space = re.findall(r"(?<=@ )\d+", input)[0]
    top_space = re.findall(r"(?<=,)\d+", input)[0]
    width = re.findall(r"(?<=: )\d+", input)[0]
    height = re.findall(r"(?<=x)\d+", input)[0]
    return Claim(_id, left_space, top_space, width, height)


class Claim:
    def __init__(self, id, left_space, top_space, width, height):
        self.left_space = int(left_space)
        self.top_space = int(top_space)
        self.width = int(width)
        self.height = int(height)
        self.id = int(id)


def claim_is_overlapping(fabric, claim):
    boolean = False
    x = claim.left_space
    y = claim.top_space
    for i in range(claim.width):
        for j in range(claim.height):
            if fabric[x + i][y + j] == 'X':
                boolean = True
    return boolean


claims = []
fabric = draw_fabric()

for i in inputs:
    claim = claim_from_input(i)
    claims.append(claim)
    fabric = draw_claim(fabric, claim)

# open('../fabric.txt', 'w').write('\n'.join([''.join(i) for i in fabric]))

# Part one

count = 0
for i in range(1000):
    for j in range(1000):
        if fabric[i][j] == 'X':
            count += 1
print(f'Overlaping inches: {count}')

print('---------------------------------')

# Part two
for c in claims:
    if claim_is_overlapping(fabric, c) is False:
        print(f'Claim that doesn\'t overlap: {c.id}')
