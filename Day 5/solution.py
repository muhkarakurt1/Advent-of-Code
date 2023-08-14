
# Reading the input files
nr_of_stacks = 9

with open('input.txt') as f:
    
    all_lines = [line.rstrip() for line in f.readlines()]
    initial_setup, rearrangement_steps = all_lines[:nr_of_stacks-1], all_lines[nr_of_stacks+1:]

    # Preparing the list for initial setup
    initial_setup_seperated = [[line[i * 4:(i + 1) * 4].strip() for i in range((len(line) + 4 - 1) // 4 )] for line in initial_setup]
    crates_per_stack = [[row[stack_no].translate({ord(c): None for c in '[]'}) for row in initial_setup_seperated][::-1] for stack_no in range(nr_of_stacks)]
    filtered_crates_per_stack = [list(filter(None, stack)) for stack in crates_per_stack]

    # Preparing the moves list
    moves = [[int(step.split(' ')[1]), int(step.split(' ')[3]), int(step.split(' ')[5])] for step in rearrangement_steps]

# Function to execute a move for PART 1
def Move1(starting_setup, move):

    final_setup = starting_setup

    from_stack_index = move[1] - 1
    to_stack_index = move[2] - 1

    for i in range(move[0]):

        moved_crate = final_setup[from_stack_index][-1]
        final_setup[from_stack_index].pop()
        final_setup[to_stack_index].append(moved_crate)

    return final_setup

# Function to execute a move for PART 2
def Move2(starting_setup, move):

    final_setup = starting_setup

    from_stack_index = move[1] - 1
    to_stack_index = move[2] - 1

    moved_crates = final_setup[from_stack_index][-move[0]:]
    final_setup[from_stack_index] = final_setup[from_stack_index][:-move[0]]
    final_setup[to_stack_index].extend(moved_crates)

    return final_setup

# Example set of moves

# example_moves = [[1,2,1],[3,1,3],[2,2,1],[1,1,2]]
# example_starting_setup = [['Z','N'],['M','C','D'],['P']]
# example_final_setup = example_starting_setup

# for move in example_moves:

#     example_final_setup = Move2(example_final_setup, move)

# print(example_final_setup)

# Moves of the input
final_setup = filtered_crates_per_stack
for move in moves:

    # Movement logic for PART 1
    # final_setup = Move1(final_setup, move)
    
    # Movement logic for PART 2
    final_setup = Move2(final_setup, move)

top_of_stacks = ''.join([stack[-1] for stack in final_setup])
print(final_setup)
print(top_of_stacks)

    







