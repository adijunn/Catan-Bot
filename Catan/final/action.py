
strategy = 0


def action(self):
    global strategy
    flag = True

    if self.get_settlements() == []:
        (x, y) = self.preComp
        self.buy("settlement", x, y)

    if strategy == 0 or len(strategy.moves) > 0:
        strategy = generate_new_strategy(player)

    while flag:
        if len(strategy.moves) > 0 and execute_purchase(player, strategy):
            continue
        elif execute_trade(player):
            continue
        else:
            flag = False


def execute_purchase(player, strategy):
    if strategy.type == "settlement":
        move = strategy.moves[0]
        if move[0] == 'r' and player.if_can_buy("road"):
            player.buy("road", move[1], move[2])
            strategy.moves.pop(0)
            return True
        elif move[0] == 's' and player.if_can_buy("settlement"):
            player.buy("settlement", move[1])
            strategy.moves.pop(0)
            return True
    return False

def execute_trade(player):
    if player.resources[np.argmax(player.resources)] >= 5:
        rmax, rmin = np.argmax(player.resources), np.argmin(player.resources)
        self.trade(rmax,rmin)
        return True
    return False
