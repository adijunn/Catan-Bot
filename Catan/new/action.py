

strategy = 0

def action(self):
    global strategy

    flag = True
    # maybe not necessary?
    if self.get_settlements() == []:
        (x, y) = self.preComp
        self.buy("settlement", x, y)
        return

    # if we have no current strategy, find new ones
    # and choose the best one
    if strategy == 0:
        strategies = find_strategies(player, 2)
        strategy = pick_best_strategy(strategies)

    while flag:
        # take the first element from strategy, if we can buy it, buy it/remove from the queue and keep flag true so it runs again

        # if we can't buy it, then try trading using our bs trading policy, keep flag true as well
        # if neither of those two work, then clearly we just have to wait, so set flag = false, ending the turn

    return
