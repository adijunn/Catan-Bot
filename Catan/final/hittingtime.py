def hitting_time(player, cost, vertex=-1):
    global vals
    epsilon = .01
    settlement_expected_resources = [0, 0, 0]
    expected_resources = expected_player_resources(player)

    if vertex != -1:
        width, height = player.board.get_vertex_location(player)
        settlement_expected_resources = vals[height][width]

    expected_resources = [settlement_expected_resources[i] + expected_resources[i] + epsilon for i in range(3)]

    without_trade_ht = [cost[i]/expected_resources[i] for i in range(3)]

    ht = np.max(expected_resources)

    return ht


def expected_player_resources(player):
    probabilities = [1/36, 2/36, 3/36, 4/36, 5/36, 0, 5/36, 4/36, 3/36, 2/36, 1/36]
    possible_outcomes = player.board.get_resources(player.player_id)
    prob_vector = np.array([probabilities])
    expected_resources_vector = np.dot(prob_vector, possible_outcomes)

    return expected_resources_vector
