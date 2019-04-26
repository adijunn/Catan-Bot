vals = calculate_expected_resources(board)

def hitting_time_board(board, cost, vertex):
    global vals

    width, height = board.get_vertex_location(vertex)
    epsilon = .01

    expected_resources = [vals[height][width][i] + epsilon for i in range(3)]

    without_trade_ht = [cost[i]/expected_resources[i] for i in range(3)]

    # TODO: include trades?
    # trade_for_wood = [(4/expected_resources[i])*cost[0] for i in [1, 2]]
    # trade_for_brick = [(4/expected_resources[i])*cost[1] for i in [0, 2]]
    # trade_for_grain = [(4/expected_resources[i])*cost[2] for i in [0, 1]]
    #
    # best_trades = [min(trade_for_wood), min(trade_for_brick), min(trade_for_grain)]
    #
    # for i in range(3):
    #     if without_trade_ht[i] > best_trades[i]:
    #         without_trade_ht[i] = best_trades[i]

    ht = np.max(without_trade_ht)

    return ht


# TODO make sure that this works
def calculate_expected_resources(board):
    dice = board.dice
    resources = board.resources
    values = [[] for i in range(board.width+1)]

    for i in range(board.width+1):
        for j in range(board.height+1):
            values[i].append([0, 0, 0])

    probabilities = [0, 0, 1/36, 2/36, 3/36, 4/36, 5/36, 0, 5/36, 4/36, 3/36, 2/36, 1/36]

    for x in range(board.width):
        for y in range(board.height):
            tile_number = dice[x][y]
            r = probabilities[tile_number]

            z = resources[x][y]

            values[x][y][z] += r
            values[x+1][y][z] += r
            values[x][y+1][z] += r
            values[x+1][y+1][z] += r

    return values
