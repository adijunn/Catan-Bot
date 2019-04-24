def get_possible_settlements(board):
    possible_settlements = []
    for x in range(5):
        for y in range(5):
            if board.if_can_build("settlement", x, y, 0):
                new_settlement = ('s', (x,y))
                possible_settlements.append(new_settlement)
    return possible_settlements

def get_possible_roads(board):
    possible_roads = []
    for x in range(5):
        for y in range(4):
            v1 = board.get_vertex_number(x, y)
            v2 = board.get_vertex_number(x, y+1)
            if board.if_can_build_road(v1, v2, 0):
                new_road = ('r', (x,y), (x,y+1))
                possible_roads.append(new_road)
    for y in range(5):
        for x in range(4):
            v1 = board.get_vertex_number(x, y)
            v2 = board.get_vertex_number(x+1, y)
            if board.if_can_build_road(v1, v2, 0):
                new_road = ('r', (x,y), (x+1,y))
                possible_roads.append(new_road)
    return possible_roads


def possible_moves(board, player):
    moves = [[], [], []]
    if player.if_can_buy("settlement"):
        for move in get_possible_settlements(board):
            moves[0].append(move)
    if player.if_can_buy("road"):
        for move in get_possible_roads(board):
            moves[1].append(move)
    if player.if_can_buy("card"):
        moves[2].append(('v'))

    return moves
