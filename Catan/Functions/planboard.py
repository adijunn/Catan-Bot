def planBoard(baseBoard):
    # prefer middle of the board over edges
    big_x = 0
    big_y = 0
    max_val = 0
    for x in range(baseBoard.width+1):
        for y in range(baseBoard.height+1):
            if vals[x][y] > max_val:
                big_x = x
                big_y = y
                max_val = vals[x][y]

    optSettlementLoc = (big_y, big_x)
    
    return optSettlementLoc
