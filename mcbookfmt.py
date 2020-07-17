#!/bin/env python3

input = open('./in.txt', 'r')
data = input.read().replace('\n\n', '\n')

lines = []

i = 0
line = ''
for l in data.split('\n'):
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
    lines.append('')


input.close()

output = open('./out.txt', 'w')
for i in range(len(lines)):
    output.write(lines[i] + '\n')
    if (i+1) % 14 == 0:
        output.write('\n\n----------\n\n\n')
output.close()
