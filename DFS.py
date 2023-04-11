graph = {
    'start': {'A': 6,
              'B': 2},
    'A': {'end': 1},
    'B': {'A': 3,
          'end': 5},
    'end': {}
}

infinity = float('inf')
costs = {'A': 6,
         'B': 2,
         'end': infinity}

parents = {'A': 'start',
           'B': 'start',
           'end': None}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: #Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost # он назначается новым
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    for neighbour_name in neighbours.keys():
        new_cost = cost + neighbours[neighbour_name]
        if costs[neighbour_name] > new_cost:
            costs[neighbour_name] = new_cost
            parents[neighbour_name] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print(processed)