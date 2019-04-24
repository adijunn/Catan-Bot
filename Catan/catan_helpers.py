


def action(self):
    flag = True
    max_score = 0
    best_move = ('n')

    while flag:
        flag = False
        possible_moves = possible_actions(board)

        for move in possible_moves:

            #if it's a settlement
            if move[0] == 's':
                score = 'something'

            #if it's a road
            if move[0] == 'r':
                score = 'something'

            if move[0] == 'vp':
                score = 'something'

    return


















# calculates expected resources for each point on the board
# returns a WxH array of all the resources!
def calculate_expected_resources(board):
    dice = board.dice
    resources = board.resources
    values = np.zeros((board.height+1, board.width+1))

    probabilities = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 0, 5/36, 4/36, 3/36, 2/36, 1/36]

    for x in range(board.width):
        for y in range(board.height):
            tile_number = dice[x][y]
            r = probabilities[tile_number]
            if x == 3 and y == 1:
                print(tile_number)

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

    return values