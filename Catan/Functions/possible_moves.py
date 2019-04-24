def get_possible_settlements(player):
    possible_settlements = []
    for x in range(5):
        for y in range(5):
            if player.board.if_can_build("settlement", x, y, player.player_id):
                new_settlement = ('s', (x,y))
                possible_settlements.append(new_settlement)
    return possible_settlements

def get_possible_roads(player):
    possible_roads = []
    for x in range(5):
        for y in range(4):
            v1 = player.board.get_vertex_number(x, y)
            v2 = player.board.get_vertex_number(x, y+1)
            if player.board.if_can_build_road(v1, v2, player.player_id):
                new_road = ('r', (x,y), (x,y+1))
                possible_roads.append(new_road)
    for y in range(5):
        for x in range(4):
            v1 = player.board.get_vertex_number(x, y)
            v2 = player.board.get_vertex_number(x+1, y)
            if player.board.if_can_build_road(v1, v2, player.player_id):
                new_road = ('r', (x,y), (x+1,y))
                possible_roads.append(new_road)
    return possible_roads


def possible_moves(player):
    moves = [[], [], []]
    if player.if_can_buy("settlement"):
        for move in get_possible_settlements(player):
            moves[0].append(move)
    if player.if_can_buy("road"):
        for move in get_possible_roads(player):
            moves[1].append(move)
    if player.if_can_buy("card"):
        moves[2].append(('v'))

    return moves

def can_build_settlement(player):
    for x in range(5):
        for y in range(5):
            if player.board.if_can_build("settlement", x, y, player.player_id):
                return True
    return False
