from time import time

start = time()


with open("day04input.txt", "r") as file_in:
    bingo = [x.strip("\n") for x in file_in.readlines()]
    bingo_numbers = [int(x) for x in bingo[0].split(",")]
    bingo_boards = list()
    state_boards = list()
    new_board = list()
    for line in bingo[2:]:
        if line:
            new_board.append([int(x) for x in line.split()])
        else:
            bingo_boards.append(new_board)
            new_board = list()
    bingo_boards.append(new_board)
    for board in bingo_boards:
        state_boards.append([[0, 0, 0, 0, 0] for x in range(5)])


def mark_boards(boards, marked_boards, number):
    for i_board in range(len(boards)):
        for i_row in range(len(boards[i_board])):
            for i_column in range(len(boards[i_board][i_row])):
                if boards[i_board][i_row][i_column] == number:
                    marked_boards[i_board][i_row][i_column] = 1
    return marked_boards


def check_boards_for_bingo(marked_boards, completed=[]):
    finished_boards = list()
    for i_board in range(len(marked_boards)):
        if i_board not in completed:
            for i_row in range(len(marked_boards[i_board])):
                if sum([marked_boards[i_board][i_row][x] for x in range(5)]) == 5:
                    finished_boards.append(i_board)
                    continue
                for i_column in range(len(marked_boards[i_board][i_row])):
                    if sum([marked_boards[i_board][x][i_column] for x in range(5)]) == 5:
                        finished_boards.append(i_board)
                        continue
    return finished_boards


def count_unmarked(marked_board, number_board):
    total = 0
    for i_row in range(len(marked_board)):
        for i_column in range(len(marked_board[i_row])):
            if marked_board[i_row][i_column] == 0:
                total += number_board[i_row][i_column]
    return total


def part_one():
    global state_boards
    for number in bingo_numbers:
        state_boards = mark_boards(bingo_boards, state_boards, number)
        bingo = check_boards_for_bingo(state_boards)
        if bingo:
            unmarked_sum = count_unmarked(
                state_boards[bingo[0]], bingo_boards[bingo[0]])
            break
    return unmarked_sum*number


def part_two():
    finished_boards = list()
    state_boards = list()
    for board in bingo_boards:
        state_boards.append([[0, 0, 0, 0, 0] for x in range(5)])
    for number in bingo_numbers:
        state_boards = mark_boards(
            bingo_boards, state_boards, number)
        new_finished_boards = check_boards_for_bingo(
            state_boards, finished_boards)
        if new_finished_boards:
            for item in new_finished_boards:
                if item not in finished_boards:
                    finished_boards.append(item)
            if len(finished_boards) == len(bingo_boards):
                unmarked_sum = count_unmarked(
                    state_boards[finished_boards[-1]], bingo_boards[finished_boards[-1]])
                return unmarked_sum*number


print(part_one())

print(part_two())

print("computed in " + str(time() - start) + " seconds")
