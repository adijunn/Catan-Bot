
def heuristic(l_resources, vp, flag):
	resource_weight = np.array([1, 1, 1])
	victory_point_weight = 5
	made_move_weight = 0.3

	return np.dot(l_resources, resource_weight.T) + vp*victory_point_weight + flag*made_move_weight	
