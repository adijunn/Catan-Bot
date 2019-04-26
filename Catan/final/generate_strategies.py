

def generate_new_strategy(player):
    strategies = possible_strategies(player)
    best_strategy = pick_best_strategy(player, strategies)

    return strategies


def possible_strategies(player):
    strategies = []

    for i in range(player.board.height+1):
        for j in range(player.board.width+1):
            vertex = player.board.get_vertex_number(i, j)
            if is_valid_settlement(player, vertex):
                roads = generate_path(player, vertex)
                new_strategy = Strategy(player, "settlement", vertex, roads)

    return strategies

def pick_best_strategy(player, strategies):
    min_ht = -1
    best_strat = 0
    for strat in strategies:
        c = [2+strat.cost[0], 1+strat.cost[1], 1+strat.cost[1]]
        ht = hitting_time(player, c, strat.vertex)
        if min_ht < 0 or ht < min_ht:
            min_ht = ht
            best_strat = strat

    return best_strat

def is_valid_settlement(player, vertex):
    for s in player.get_settlements():
        if dist(player, s, vertex) < 2:
            return False
    return True

#returns distance between two vertices
def dist(player, v1, v2):
    x1, y1 = player.board.get_vertex_location(v1)
    x2, y2 = player.board.get_vertex_location(v2)

    x_dist = abs(x1 - x2)
    y_dist = abs(y1 - y2)

    return x_dist + y_dist

def generate_path(player, vertex):
    min_dist = 5000
    min_settlement = -1
    roads = []

    for s in player.get_settlements():
        if dist(player, s, vertex) < min_dist:
            min_settlement = s

    x1, y1 = player.board.get_vertex_location(s)
    x2, y2 = player.board.get_vertex_location(vertex)

    prev = (x1, y1)

    if x1 < x2:
        diff = x2 - x1
        while diff > 0:
            roads.append(('r', prev, (prev[0], prev[1] + 1)))
            diff -= 1
            prev = (prev[0], prev[1] + 1)
    elif x1 > x2:
        diff = x1 - x2
        while diff > 0:
            roads.append(('r', prev, (prev[0], prev[1] - 1)))
            diff -= 1
            prev = (prev[0], prev[1] - 1)

    if y1 < y2:
        diff = y2 - y1
        while diff > 0:
            roads.append(('r', prev, (prev[0] + 1, prev[1])))
            diff -= 1
            prev = (prev[0] + 1, prev[1])
    elif y1 > y2:
        diff = y1 - y2
        while diff > 0:
            roads.append(('r', prev, (prev[0] - 1, prev[1])))
            diff -= 1
            prev = (prev[0] - 1, prev[1])

    return roads
