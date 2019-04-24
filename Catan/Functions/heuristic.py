
def heuristic(l_resources, vp, flag):
    resource_weight = 100 #np.array([1, 1, 1])
    victory_point_weight = 0
    made_move_weight = 0.3


    #return np.dot(l_resources, resource_weight.T) + vp*victory_point_weight + flag*made_move_weight
    return resource_weight*l_resources + vp*victory_point_weight + flag*made_move_weight
