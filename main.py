# battleship game contains ROW(A-J)  and COLUMN (1-10) = 10X10 grid. there are two grids of ROW and COLUMN,
# lower to arrange self-ships, and upper to defeat enemy's ships. each gets 5 ships containing: 1 ship of 2 dots + 2
# ships of 3 dots + 1 ship of 4 dots + 1 ship of 5 dots. no diagonal or overlapping ships when placed on grid.
# player 1 begins using a letter and number. example: A1 if there is no ship, player2 says miss. then player1 puts '-'
# on there. else 'S' as strike and player2 places X on his ship. ship on terminal grid could look like this [....] or
# [..] dots as the length of the ship and if hit then a ship of 3 dots such as [...] will look like [..X] and so on [
# .XX] depends on where is has been hit
# if the ship has eliminated, the opponent says "you sunk my ship"

def get_shot(guesses):
    ok = "n"
    while ok == "n":
        try:
            shot = int(input("please enter your guess: "))
            if shot < 0 or shot > 99:
                print("your guess is not between 0 and 99")
            elif shot in guesses:
                print("this number has been used")
            else:
                ok = "y"
                break
        except ValueError:  # Catch only ValueError for invalid input
            print("only numbers please")
    return shot

ship_lengths = {2: [20, 21], 3: [45, 46, 47], 4: [0, 1, 2, 3], 5: [60, 61, 62, 63, 64]}

def show_board(hit, miss, strike, boat1):
    print("             BattleShips    ")
    print("     0  1  2  3  4  5  6  7  8  9")
    place = 0
    for x in range(10):
        row = ""
        for y in range(10):
            ch = " _ "
            if place in miss:
                ch = " x "
            elif place in hit:
                ch = " o "
            elif place in strike:
                ch = " O "
            row += ch
            place += 1
        print(x, " ", row)
    print()

def check_shot(shot, boat1, boat2, hit, miss, strike):  # Added missing comma after boat2
    if shot in boat1:
        boat1.remove(shot)
        if len(boat1) > 0:
            hit.append(shot)
        else:
            strike.append(shot)
    elif shot in boat2:  # Use 'elif' to avoid checking both boat1 and boat2 for the same shot
        boat2.remove(shot)
        if len(boat2) > 0:
            hit.append(shot)
        else:
            strike.append(shot)
    else:
        miss.append(shot)

    return boat1, boat2, hit, miss, strike

# Initial setup
boat1 = [45, 46, 47]
boat2 = [6, 16, 26]
hit = []
miss = []
strike = []

# Main game loop
show_board(hit, miss, strike, boat1)

for i in range(10):
    guesses = hit + miss + strike
    shot = get_shot(guesses)
    boat1, boat2, hit, miss, strike = check_shot(shot, boat1, boat2, hit, miss, strike)  # Added boat2
    show_board(hit, miss, strike, boat1)

    if len(boat1) < 1 and len(boat2) < 1:
        print("you've won")
        break

print("finished")
