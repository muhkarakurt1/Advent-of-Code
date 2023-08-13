import string

# Read the Rucksack input into a list - PART 1
rucksack_info1 = []
with open('input.txt') as f:
    for rucksack in f:
        stripped_rucksack = rucksack.strip()
        firstpart, secondpart = stripped_rucksack[:len(stripped_rucksack)//2], stripped_rucksack[len(stripped_rucksack)//2:]
        common_character = ''.join(set(firstpart).intersection(secondpart))
        rucksack_info1.append([firstpart, secondpart, common_character])

# Read the Rucksack input into a list - PART 2
with open('input.txt') as f:
    stripped_rucksacks = [rucksack.strip() for rucksack in f.readlines()]
    rucksack_groups = [stripped_rucksacks[x:x+3] for x in range(0, len(stripped_rucksacks), 3)]
    rucksack_group_priorities = [''.join(set(rucksack_group[0]).intersection(rucksack_group[1]).intersection(rucksack_group[2])) for rucksack_group in rucksack_groups]
    rucksack_info2 = [rucksack_groups[i] + [rucksack_group_priorities[i]] for i in range(len(rucksack_groups))]

# Creating the priority dictionary
priority_lowercase = {val : (1 * (idx + 1)) for idx, val in enumerate(list(string.ascii_lowercase))}
priority_uppercase = {val : 26 + (1 * (idx + 1)) for idx, val in enumerate(list(string.ascii_uppercase))}
priority = priority_lowercase | priority_uppercase

sum_priority = 0

# Sum of priorities - PART 1
# for rucksack in rucksack_info1:

#     sum_priority += priority[rucksack[2]]

# Sum of priorities - PART 2
for rucksack in rucksack_group_priorities:

    sum_priority += priority[rucksack]

print(sum_priority)