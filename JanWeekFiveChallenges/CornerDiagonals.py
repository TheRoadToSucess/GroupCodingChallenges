# You are given an integer n representing the length of an n by n board.
#  Remove all cells that are diagonal to one of the four corners (top left, 
# top right, bottom right, and bottom left) and return the number of empty cells leftover.

#  n represents the length of a board

n = 4

if n % 2 == 0:
    print((n - 2) * n)
else:
    print ((n - 2) * n + 1)