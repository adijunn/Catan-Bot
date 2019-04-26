import numpy as np

SETTLEMENT = 0
CARD = 1
CITY = 2
ROAD = 3
MAX_POINTS = 10
ROBBER_MAX_RESOURCES = 7
START_RESOURCES = 3

costs = np.array([[2, 1, 1],
                  [1, 2, 2],
                  [0, 3, 3],
                  [1, 1, 0]])


# compute estimated hitting time to things
# TODO finish this method: possible issue, how to incorporate trading?
def hitting_time(player, goal):
    # output of this is [w, b, g]
    expected_resources = expected_player_resources(player)
    settlement_cost = [2, 1, 1]
    road_cost = [1, 1, 0]
    card_cost = [1, 2, 2]
    city_cost = [0, 3, 3]

    if goal == "road":
        g = road_cost
    elif goal == "settlement":
        g = settlement_cost
    elif goal == "vp":
        g = card_cost

    individual_resource_hitting_time = [g[i] / expected_resources[i] for i in range(3)]
    

    trade_for_wood = [(4/expected_resources[i])*g[0] for i in [2, 3]]
    trade_for_brick = [(4/expected_resources[i])*g[1] for i in [1, 3]]
    trade_for_grain = [(4/expected_resources[i])*g[2] for i in [1, 2]]

    best_trades = [min(trade_for_wood), min(trade_for_brick), min(trade_for_grain)]

    for i in range(3):
	if individual_resource_hitting_time[i] > best_trades[i]:
		individual_resource_hitting_time[i] = best_trades[i]

    hitting_time = max(individual_resource_hitting_time)
    #return np.max(np.divide(costs[g], expected_resources))
    return hitting_time


def find_strategies(player, road_cap):
    # this is for settlements we have already explored to avoid searching duplicates
    possible_settlements = []

    # this is what we'll return; it's an array of strategy objects that we will choose from
    strategies = []

    for settlement in player.get_settlements():
        # this will get all the road combinations that can be extended from our current settlements
        # all road combos have to be valid, ie no roads that we already own etc.
        possible_strategies = get_road_enumerations()

        for s in possible_strategies:
            # check if it's a valid place for us to buy a settlement
            # if it's not already in possible settlements [] then put it there
            # and add a strategy to strategies with the roads to get there and then the settlement object itself

    return strategies




# this function returns all possible road combinations for a player from a given x, y coordinate
# subject to the road_cap maximum, and removes combos that duplicate roads/contains roads that we already own!
def get_road_enumerations(player, v, road_cap):


    return


class Strategy:
    def __init__(self):
        self.moves = []
