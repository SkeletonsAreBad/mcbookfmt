#!/bin/env python3

input = open('./in.txt', 'r')
data = input.readlines()

lines = []

i = 0
line = ''
for l in data:
    for w in l.split(' '):
        if i + len(w) + 1 <= 20:
            i += len(w) + 1
            line += w + ' '
        else:
            lines.append(line.strip())
            line = w + ' '
            i = len(w) + 1
    lines.append(line.strip())
    i = 0
    line = ''

print(lines)


input.close()

output = open('./out.txt', 'w')
for i in range(len(lines)):
    output.write(lines[i] + '\n')
    if (i+1) % 14 == 0:
        output.write('\n\n----------\n\n\n')
output.close()
