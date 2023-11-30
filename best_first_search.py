def best_first_search(graph, start, goal, heuristic):
    open_list = [(start, heuristic[start])]
    closed_list = set()
    parent = {}
    distance = {start: 0}

    while open_list:
        open_list.sort(key=lambda x: x[1])
        current_node, _ = open_list.pop(0)

        if current_node == goal:
            path = []
            total_distance = 0
            while current_node is not None:
                path.insert(0, current_node)
                if parent.get(current_node):
                    total_distance += graph[current_node][parent[current_node]]
                current_node = parent.get(current_node)
            return path, total_distance

        if current_node not in closed_list:
            closed_list.add(current_node)
            for neighbor, dist in graph[current_node].items():
                if neighbor not in closed_list:
                    parent[neighbor] = current_node
                    distance[neighbor] = distance[current_node] + dist
                    open_list.append((neighbor, distance[neighbor] + heuristic[neighbor]))

    return None, 0

romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 178,
    'Pitesti': 98,
    'Bucharest': 0
}

start_city = 'Arad'
goal_city = 'Bucharest'
path, total_distance = best_first_search(romania_map, start_city, goal_city, heuristic)

if path:
    print(f"Shortest path from {start_city} to {goal_city}: {' -> '.join(path)}")
    print(f"Total distance: {total_distance} km")
else:
    print(f"No path found from {start_city} to {goal_city}.")
