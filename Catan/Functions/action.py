def action(self):
    flag = True
    max_score = 0
    best_move = ('n')

    if self.get_settlements() == []:
        (x, y) = self.preComp
        self.buy("settlement", x, y)
        return


    while flag:
        flag = False
        moves = possible_moves(self)

        for settlement in moves[0]:
            score = heuristic(vals[settlement[1][0]][settlement[1][1]], 1, 1)
            if score > max_score:
                best_move = settlement
                max_score = score

        for road in moves[1]:
            score = heuristic(0, 0, 1)
            if score > max_score:
                best_move = road
                max_score = score

        for victorypoint in moves[2]:
            score = heuristic(0, 1, 1)
            if score > max_score:
                best_move = victorypoint
                max_score = score

        if best_move == ('n'):
            if self.resources[np.argmax(self.resources)] >= 4:
                rmax, rmin = np.argmax(self.resources), np.argmin(self.resources)
                self.trade(rmax,rmin)
                flag = True
            else:
                return
        elif best_move[0] == 's':
            self.buy("settlement", best_move[1][0], best_move[1][1])
        elif best_move[0] == 'r':
            if can_build_settlement(self):
                return
            self.buy("road", best_move[1], best_move[2])
            flag = True
            max_score = 0
            best_move = ('n')
        elif best_move[0] == 'v':
            self.buy("card")

    return
