
# TODO: modify this so that it has all three resources SEPARATE
def calculate_expected_resources(board):
    dice = board.dice
    resources = board.resources
    values = np.zeros((board.height+1, board.width+1))
    discount_rate = 0.1

    probabilities = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 0, 5/36, 4/36, 3/36, 2/36, 1/36]

    for x in range(board.width):
        for y in range(board.height):
            tile_number = dice[x][y]
            r = probabilities[tile_number]

            #z = resources[x][y]
            # for later when we want to calculate different resources

            #bottom left point
            values[x][y] += r

            #bottom right point
            values[x+1][y] += r

            #top left point
            values[x][y+1] += r

            #top right point
            values[x+1][y+1] += r

    #values /= (1 - discount_rate)
    return values

# TODO write this function
# returns a vector for the expected resource production for a player on a single turn
def expected_player_resources(player):
    return
