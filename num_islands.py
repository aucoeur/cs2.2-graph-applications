from graph import Graph

def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""

    graph = Graph(is_directed=False)

    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            index = (x * len(row)) + y

            # col = row[x]
            if col == 1:
                graph.add_vertex(f'{index}')

                # check for previous one so as not to try edge to vertex that doesn't exist yet

                # grid[x-1][y] is north adj item
                if x > 0 and grid[x-1][y] == 1:
                    adjacent = f'{(((x-1) * len(grid[x-1])) + y)}'
                    graph.add_edge(f'{index}', f'{adjacent}')
                    # print(f'{index} connects up to {adjacent}')

                # grid[x][y-1] is previous horizontal adj item
                if y > 0 and grid[x][y-1] == 1:
                    adjacent = f'{((x * len(grid[x])) + (y-1))}'
                    graph.add_edge(f'{index}', f'{adjacent}')
                    # print(f'{index} connects up to {adjacent}')

    
    # return graph.find_connected_components()
    return len(graph.find_connected_components())

if __name__ == "__main__":

    # Test Cases

    # map1 = [
    #     [1, 1, 1, 1, 0],
    #     [1, 1, 0, 1, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0]
    # ]
    # assert numIslands(map1) == 1

    map2 = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    assert numIslands(map2) == 3

    print(numIslands(map2))
