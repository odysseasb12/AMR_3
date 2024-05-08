This code implements the A* (A-star) pathfinding algorithm to find the shortest path from a start point to an end point on a grid. Here's a breakdown of what the code does: A* uses two cost functions for each node:
    g(n): The actual cost of reaching node n from the starting node.
    f(n): The sum of g(n) and h(n). This represents the estimated total cost of the cheapest path from the starting node to the goal node through node n.
    A* repeatedly selects the node from the open list with the lowest f(n) value for evaluation.
    It moves this node from the open list to the closed list.
    Then, it examines all the neighboring nodes (also known as "successors") of the current node.
    For each neighbor:
        If it is not already in the closed list, A* calculates its g(n) value (the cost of reaching that node from the starting node).
        If the neighbor is not in the open list, it is added to it.
        If the neighbor is already in the open list, A* checks if the new path to that node is cheaper than the previous one. If it is, A* updates the cost and parent information.
    The process continues until either the goal node is reached or the open list is empty (indicating that there is no path to the goal).
    If the goal node is reached, the algorithm reconstructs the path from the starting node to the goal node by following the parent pointers from the goal node back to the starting node.
    If the open list becomes empty without reaching the goal node, then there is no path from the starting node to the goal node.
