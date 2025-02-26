import heapq
import numpy as np

def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):
        x1, y1 = np.where(state == num)
        x2, y2 = np.where(goal == num)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance[0]

def get_neighbors(state):
    neighbors = []
    x, y = np.where(state == 0)
    x, y = x[0], y[0]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy 
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = state.copy()
            new_state[x, y], new_state[nx, ny] = new_state[nx, ny], new_state[x, y]
            neighbors.append(new_state)
    
    return neighbors

def a_star(start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start.tolist()))
    visited = set()
    parent_map = {}
    g_score = {tuple(map(tuple, start)): 0}
    
    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        current = np.array(current)
        
        if np.array_equal(current, goal):
            path = []
            while tuple(map(tuple, current)) in parent_map:
                path.append(current)
                current = parent_map[tuple(map(tuple, current))]
            path.append(start)
            path.reverse()
            return path
        
        visited.add(tuple(map(tuple, current)))
        
        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple in visited:
                continue
            
            tentative_g_score = g_score[tuple(map(tuple, current))] + 1
            
            if neighbor_tuple not in g_score or tentative_g_score < g_score[neighbor_tuple]:
                g_score[neighbor_tuple] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor, goal)
                heapq.heappush(priority_queue, (f_score, neighbor.tolist()))
                parent_map[neighbor_tuple] = current
    
    return None  # No solution found

if __name__ == "__main__":
    start_state = np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]])  # Initial state
    goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])  # Goal state
    
    solution = a_star(start_state, goal_state)
    
    if solution:
        print("Solution found in {} steps:".format(len(solution) - 1))
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print(state, "\n")
    else:
        print("No solution found.")
