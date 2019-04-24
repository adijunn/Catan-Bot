
#This function takes as input a vertex on the board (x and y coord) and returns a list of tuples where each tuple is of the form: (resource_id, probability) (0 is wood, 1 is brick, and 2 is grain)
#Parameters: coord --> tuple of x and y coord
def get_neighbors(coord):
	x_coord = coord[0]	 
	y_coord = coord[1]
	



def calculate_value(node):
	#node.neighbors should return a list of tuples where each tuple is of the form: (resource_id, probability) --> resource type is ant int {0, 1, 2}
	discount_rate = 0.1
	initial_expectation_value = [0, 0, 0] 
	for resource_id,prob in node.neighbors:
		initial_expectation_value[resource] += prob
		
	#We could sum up the expected resources as follows (which implies that all resources have equal weight at any given point in the game)  or weight different resources differently which we can talk about later

	node_value = sum(initial_expectation_value)

	#Using the geometric sum here to account for the discount rate and give the node a lifetime static value
	lifetime_value = node_value / (1 - discount_rate)

	return lifetime_value 
	
		
	
