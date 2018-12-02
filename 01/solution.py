inputs = open('input.txt').read().split('\n')

# First
print(sum([int(i) for i in inputs]))

# Second
numbers = set()
index = 0
while True:
    for i in inputs:
        index += int(i)
        if index in numbers:
            print(index)
            exit()
        else:
            numbers.add(index)
            continue
