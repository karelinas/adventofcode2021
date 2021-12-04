from sys import stdin
from typing import IO, Optional, NamedTuple, List, Tuple

BOARD_COLUMN_COUNT = 5
BOARD_ROW_LENGTH = 5
BOARD_SIZE = BOARD_ROW_LENGTH * BOARD_COLUMN_COUNT

Cell = NamedTuple("Cell", [("number", int), ("marked", bool)])
Board = List[List[Cell]]
Numbers = List[int]


def board_from_ints(data: List[str]) -> Board:
    cells = [Cell(number=int(number), marked=False) for number in data]
    return list(zip(*[iter(cells)] * BOARD_ROW_LENGTH))


def parse_input_data(io: IO[str]) -> Tuple[Numbers, List[Board]]:
    numbers = [int(num) for num in io.readline().split(",")]
    board_data = io.read().split()
    boards = [
        board_from_ints(board_data)
        for board_data in zip(*[iter(board_data)] * BOARD_SIZE)
    ]
    return numbers, boards


def is_winning(board: Board) -> bool:
    any_row_wins = any(all(cell.marked for cell in row) for row in board)
    any_column_wins = any(
        all(cell.marked for cell in column) for column in map(list, zip(*board))
    )
    return any_row_wins or any_column_wins


def mark_number(board: Board, number: int) -> Board:
    return [
        [Cell(number, True) if cell.number == number else cell for cell in row]
        for row in board
    ]


def play_one_round(boards: List[Board], number: int) -> List[Board]:
    return [mark_number(board, number) for board in boards]


def find_winning(boards: List[Board]) -> Optional[Board]:
    return next((board for board in boards if is_winning(board)), None)


def play_bingo(
    boards: List[Board], numbers: Numbers
) -> Tuple[Optional[Board], Optional[int]]:
    for number in numbers:
        boards = play_one_round(boards, number)
        if winning_board := find_winning(boards):
            return winning_board, number
    return None, None


def play_handicap_bingo(
    boards: List[Board], numbers: Numbers
) -> Tuple[Optional[Board], Optional[int]]:
    last_winner = None
    last_number = None
    for number in numbers:
        boards = play_one_round(boards, number)
        if winning_board := find_winning(boards):
            last_winner = winning_board
            last_number = number
            boards = [board for board in boards if not is_winning(board)]
    return last_winner, last_number


numbers, boards = parse_input_data(stdin)

winning_board, winning_number = play_bingo(boards, numbers)
sum_of_unmarked = sum(
    cell.number for row in winning_board for cell in row if not cell.marked
)
print(winning_number * sum_of_unmarked)

losing_board, losing_number = play_handicap_bingo(boards, numbers)
sum_of_unmarked = sum(
    cell.number for row in losing_board for cell in row if not cell.marked
)
print(losing_number * sum_of_unmarked)
