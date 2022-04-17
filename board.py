board = [
  ['-','-','-'],
  ['-','-','-'],
  ['-','-','-',]
]

def print_board(board):
  for row in board:
    for slot in row:
      print(f"{slot} ", end='')
    print()

def check_mark(row, col):...

def place_mark(row, col, player):...

def check_win(player):...


print_board(board)