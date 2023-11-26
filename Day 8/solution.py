import numpy as np
from itertools import groupby

# Creating a numpy array from the input txt
with open("input.txt", "r") as f:
    input_array = np.stack([np.fromiter(list(line.strip()), dtype=np.int64) for line in f])


# Function to find if a specific tree(within interior) is visible
def is_visible(input_array, row_number, column_number):
    tree_height = input_array[row_number, column_number]

    # Relevant tree heights
    left_values = input_array[row_number, :column_number]
    right_values = input_array[row_number, column_number + 1 :]
    top_values = input_array[:row_number, column_number]
    bottom_values = input_array[row_number + 1 :, column_number]

    if (left_values < tree_height).all() or (right_values < tree_height).all() or (top_values < tree_height).all() or (bottom_values < tree_height).all():
        return True
    else:
        return False


# Function to find the number of visible trees in the whole tree cover
def find_visible_tree_number(input_array):
    total_number_of_visible_trees = 0

    row_number, column_number = input_array.shape
    for row in range(row_number):
        for column in range(column_number):
            if row in [0, row_number - 1] or column in [0, column_number - 1]:
                total_number_of_visible_trees += 1
            else:
                if is_visible(input_array, row, column):
                    total_number_of_visible_trees += 1

    return total_number_of_visible_trees


# Function to find the scenic score of a specific tree(within interior)
def calculate_scenic_score(input_array, row_number, column_number):
    tree_height = input_array[row_number, column_number]

    # Relevant tree heights arrays
    left_values = np.flip(input_array[row_number, :column_number]) < tree_height
    right_values = input_array[row_number, column_number + 1 :] < tree_height
    top_values = np.flip(input_array[:row_number, column_number]) < tree_height
    bottom_values = input_array[row_number + 1 :, column_number] < tree_height

    # Scenic scores
    left_scenic_score = left_values.size if np.all(left_values) else np.argmax(left_values == False) + 1
    right_scenic_score = right_values.size if np.all(right_values) else np.argmax(right_values == False) + 1
    top_scenic_score = top_values.size if np.all(top_values) else np.argmax(top_values == False) + 1
    bottom_scenic_score = bottom_values.size if np.all(bottom_values) else np.argmax(bottom_values == False) + 1

    # print("Index:", row_number, column_number)
    # print("Left:", left_scenic_score)
    # print("Right:", right_scenic_score)
    # print("Top:", top_scenic_score)
    # print("Bottom:", bottom_scenic_score)
    # print("Total:", left_scenic_score * right_scenic_score * top_scenic_score * bottom_scenic_score)
    # print("------------------")
    return left_scenic_score * right_scenic_score * top_scenic_score * bottom_scenic_score


# Function to find the maximum scenic number in the whole tree cover
def find_maximum_scenic_number(input_array):
    maximum_scenic_number = 0

    row_number, column_number = input_array.shape
    for row in range(row_number):
        for column in range(column_number):
            if row in [0, row_number - 1] or column in [0, column_number - 1]:
                continue
            else:
                scenic_score = calculate_scenic_score(input_array, row, column)
                if scenic_score > maximum_scenic_number:
                    maximum_scenic_number = scenic_score

    return maximum_scenic_number


# ---------------------------------------------------------------------------- #
#                                  Question 1                                  #
# ---------------------------------------------------------------------------- #

print(find_visible_tree_number(input_array))

# ---------------------------------------------------------------------------- #
#                                  Question 2                                  #
# ---------------------------------------------------------------------------- #

print(find_maximum_scenic_number(input_array))
