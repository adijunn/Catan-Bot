def planBoard(baseBoard):

    height = 0
    width = 0
    min_val = 0
    count = 0

    cost = [2, 1, 1] # default for settlement

    for i in range(baseBoard.height+1):
        for j in range(baseBoard.width+1):
            vertex = baseBoard.get_vertex_number(i, j)
            ht = hitting_time_board(baseBoard, cost, vertex)
            print(ht)
            if count == 0:
                min_val = ht
                height = j
                width = i
                count += 1

            if ht < min_val:
                min_val = ht
                height = j
                width = i
    print(min_val)
    #TODO make sure that the height/width is CORRECT!!!!!!!
    optSettlementLocation = (height, width)

    return optSettlementLocation
