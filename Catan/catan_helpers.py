def action(self):
    flag = True
    max_score = 0
    best_move = ('n')

    print(self.resources)
    while flag:
        flag = False
        moves = possible_moves(board, self)

        for settlement in moves[0]:
            score = heuristic(vals[settlement[1][0]][settlement[1][1]], 1, 1)
            if score > max_score:
                best_move = settlement
                max_score = score

        for road in moves[1]:
            score = score = heuristic(0, 0, 1)
            if score > max_score:
                best_move = road
                max_score = score
        for victorypoint in moves[2]:
            score = heuristic(0, 1, 1)
            if score > max_score:
                best_move = victorypoint
                max_score = score

        print(best_move)
        if best_move == ('n'):
            return
        elif best_move[0] == 's':
            self.buy("settlement", best_move[1][0], best_move[1][1])
        elif best_move[0] == 'r':
            self.buy("road", best_move[1], best_move[2])
            flag = True
            max_score = 0
            best_move = ('n')
        elif best_move[0] == 'v':
            self.buy("card")
    return





# calculates expected resources for each point on the board
# returns a WxH array of all the resources!
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
vals = calculate_expected_resources(board)
print(vals)
