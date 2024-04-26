# Heuristic Function to calculate the euclidean distance between the current and end cell
def euclidean_distance(cell, end):
    return (((end[0]-cell[0])**2 + (end[1]-cell[1])**2)**0.5)

# Function to calculate the minimum cost f
def min_f_cost(list, f_cost):
    minimum_cost = float('inf')
    # Calculating the f cost for every cell in the list 
    for cell in list: 
         # If the f cost of the cell that is currently being checked is lower than the previous one then update both of their values
         if f_cost.get(cell) < minimum_cost:
              min_cell = cell
              minimum_cost = f_cost[cell]
    # Return the cell with the minimum f_cost
    return min_cell

# Function to find the adjacent cells
def finding_neighbors(cell, grid, COL, ROW):
    # List to store adjacent cells
    neighbors = []
    #From the current cell calculate and find the cells that are located up, down, left, and right 
    for neighbor_pos in [(0,-1),(0,1),(-1,0),(1,0)]:
                new_position = (cell[0]+neighbor_pos[0],cell[1]+neighbor_pos[1])
                # If the adjacent cell is inside the defined boundaries and if there are not any obstacles then append it to the list
                if (new_position[0]>=0) and (new_position[0]<COL) and (new_position[1]>=0) and (new_position[1]<ROW):
                    if grid[new_position[0]][new_position[1]] == 1:
                        neighbors.append(new_position)
    return neighbors


# The main path planning function. Additional functions, classes, 
# variables, libraries, etc. can be added to the file, but this
# function must always be defined with these arguments and must 
# return an array ('list') of coordinates (col,row).
#DO NOT EDIT THIS FUNCTION DECLARATION
def do_a_star(grid, start, end, display_message):
    #EDIT ANYTHING BELOW HERE

    # Get the size of the grid
    COL = len(grid)
    ROW = len(grid[0])

    # Defining the open, closed and path lists
    open_list = [start]
    closed_list = []
    path = []

    # Defining the necessary dictionaries 
    # Initialise the dictionaries with appropriate values
    g_cost = {start:0}
    h_cost = {start: euclidean_distance(start,end)}
    f_cost = {start:g_cost[start] + h_cost[start]}
    parent = {start:None}

    while open_list:
        # Calling the min_f_cost function and setting the next cell as the one with the min f cost
        current_cell = min_f_cost(open_list,f_cost)

        # If the end cell is found do these:  
        if current_cell == end:
            while current_cell is not None:
                path.append(current_cell)
                current_cell = parent[current_cell]
            # Returning the path reversed otherwise the path would start from the end and finish at the start 
            # Send the path points back to the gui to be displayed
            #FUNCTION MUST ALWAYS RETURN A LIST OF (col,row) COORDINATES
            return path[::-1]
        
        #Remove the cell that its neighbors have been already found and append it to the closed list 
        open_list.remove(current_cell)
        closed_list.append(current_cell)

        # Calling the function to find the neighbors and checking if these cells are in the closed list and have been evaluated
        for neighbor in finding_neighbors(current_cell,grid,COL,ROW):
            if neighbor in closed_list:
                continue 
            
            # Updating the overall g cost from the start up until the current cell 
            overall_g_cost = g_cost[current_cell] + 1

            # Checks if the neighbor node is already in the closed_list, and if it is there is no need to evaluate it again, so we skip this neighbor.
            # If the overall_g_cost to reach this neighbor is less than the previous one, then a better path has been found.
            if neighbor in closed_list or overall_g_cost < g_cost.get(neighbor, float('inf')):
                # Updates the parent of the neighbor node to the current next_node
                parent[neighbor] = current_cell
                # Updates the g_cost of the neighbor node with the newly calculated overall_g_cost
                g_cost[neighbor] = overall_g_cost
                # Calculates the h_cost from the neighbor node to the end node. 
                h_cost[neighbor] = euclidean_distance(neighbor, end)
                # Calculates the total estimated cost
                f_cost[neighbor] = g_cost[neighbor] + h_cost[neighbor]
                # If the neighbor is not already in the open list we append it to ensure further exploration 
                if neighbor not in open_list:
                    open_list.append(neighbor)    
    # Send the path points back to the gui to be displayed
    #FUNCTION MUST ALWAYS RETURN A LIST OF (col,row) COORDINATES
    return path

#end of file 
