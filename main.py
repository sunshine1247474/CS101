# battleship game contains ROW(A-J)  and COLUMN (1-10) = 10X10 grid. there are two grids of ROW and COLUMN,
# lower to arrange self ships, and upper to defeat enemy's ships. each gets 5 ships containing: 1 ship of 2 dots + 2
# ships of 3 dots + 1 ship of 4 dots + 1 ship of 5 dots. no diagonal or overlapping ships when placing on grid.
# player 1 begins using letter and number. example: A1 if there is no ship player2 says miss. then player1 puts '-'
# on there. else 'S' as strike and player2 places X on his ship. ship on terminal grid could look like this [....] or
# [..] dots as the length of the ship and if hit then a ship of 3 dots such as [...] will look like [..X] and so on [
# .XX] depends on where is has been hit
# if the ship has eliminated, the opponent says "you sunk my ship"

# CREATING FUNCTION OF HIT MISS STRIKE
def show_board(hit, miss, strike):
    print("             BattleShips    ")   # our title game
    print("     0  1  2  3  4  5  6  7  8  9")   # our number for navigation


hit = [8, 21, 22]  # hit positions
miss = [20, 24, 12, 13]  # miss positions
strike = [23]  # strike positions

show_board(hit, miss, strike)  # retrieving the board with the information of hit miss and strike / not build yet

place = 0  # would be used to locate hit, miss, strike
for x in range(10):
    row = ""  # like a reset button every time we get to another row
    for y in range(10):
        ch = " _ "  # this is how we mark a positions in the game
        if place in miss:  # at the button of this for loop we see place adds +1. so place checks in miss if the
            # coordinates matches. and changes the mark of the position to the appropriate.
            ch = " x "
        elif place in hit:
            ch = " o "
        elif place in strike:
            ch = " O "
        row += ch  # at the top for loop we see it runs 10 times. row adds "_" / ch 10 times and then resets once we
        # approach another row like I mentioned at the top of this loop
        place += 1  # every time we add "_" we have to know what position it has 1,4,21, etc. and it also helps us
        # locate hits, miss, and strikes.
    print(x, " ", row)  # at the top for loop x is 0 and goes on until reaches 9. 0-9 = 10 interation. print row
    # number, space, and the whole "_" *10 and before getting to second for loop row resets.
