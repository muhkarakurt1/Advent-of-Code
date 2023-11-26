# Read the strategy input into a list
strategy_input = []
with open("input.txt") as f:
    for strategy in f:
        strategy_input.append([strategy[0], strategy[2]])


# Function to calculate Win/Draw/Lose - PART 1
def Result(strategy):
    if strategy in [["A", "X"], ["B", "Y"], ["C", "Z"]]:
        return 1
    elif strategy in [["C", "X"], ["A", "Y"], ["B", "Z"]]:
        return 2
    else:
        return 0


# Function to calculate total points for the given strategy - PART 1
def Point1(strategy):
    your_strategy = strategy[1]

    # Points from the result
    point_result = Result(strategy) * 3

    # Point from the move
    point_move = 1 if your_strategy == "X" else 2 if your_strategy == "Y" else 3

    return point_result + point_move


# Function to find the required move - PART 2
def FindMove(strategy):
    if strategy in [["A", "X"], ["B", "Z"], ["C", "Y"]]:
        return "Scissors"

    elif strategy in [["C", "X"], ["A", "Z"], ["B", "Y"]]:
        return "Paper"

    else:
        return "Rock"


# Function to calculate total points for the given strategy - PART 2


def Point2(strategy):
    move_you_need = FindMove(strategy)

    # Points from the result
    point_result = 0 if strategy[1] == "X" else 3 if strategy[1] == "Y" else 6

    # Point from the move
    point_move = 1 if move_you_need == "Rock" else 2 if move_you_need == "Paper" else 3

    return point_result + point_move


# Go through each strategy to calculate the total points
total_point = 0

for strategy in strategy_input:
    total_point += Point2(strategy)
    # total_point += Point1(strategy)

print(total_point)
