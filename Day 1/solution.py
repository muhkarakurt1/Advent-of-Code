from collections import Counter

# Reading the input and calculating total calory for each elf
calory_dict = {}
with open('input.txt') as f:
    elf_number = 1
    calory_dict[elf_number] = 0

    for line in f:
        if line == '\n':
            elf_number += 1
            calory_dict[elf_number] = 0
            continue
        calory_dict[elf_number] += int(line.strip())

# Part 1 Answer
ans1 = max(calory_dict.values())

# Part 2 Answer
counter = Counter(calory_dict)
top_3_elves = dict(counter.most_common(3))
ans2 = sum(top_3_elves.values())