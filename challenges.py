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

# Test Cases
map1 = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
assert numIslands(map1) == 1

map2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
assert numIslands(map2) == 3

def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number of minutes until all oranges rot.
    """

    rows = len(grid)
    cols = len(grid[0])

    time_to_rot = 0
    queue = deque()

    for row in range(rows):
        for col in range(cols):
            # position = (row * rows) + col
            position = grid[row][col]

            # add rotted oranges to queue with T minus 0
            if position == 2:
                queue.append((row, col, 0))
 
    while queue:
        row, col, tminus = queue.popleft()

        if tminus > time_to_rot:
            time_to_rot = tminus

        # infect neighbors
        north = row - 1
        south = row + 1
        west = col - 1
        east = col + 1

        if row > 0 and grid[north][col] == 1:
            grid[north][col] = 2
            queue.append((north, col, tminus+1))
        if row < rows-1 and grid[south][col] == 1:
            grid[south][col] = 2
            queue.append((south, col, tminus+1))
        if col > 0 and grid[row][west] == 1:
            grid[row][west] = 2
            queue.append((row, west, tminus+1))
        if col < cols-1 and grid[row][east] == 1:
            grid[row][east] = 2
            queue.append((row, east, tminus + 1))
    
    # if any fresh oranges remain after contagion(isolated)
    if [y for x in grid for y in x if y == 1]:
        return -1

    return time_to_rot

# Test Cases
oranges1 = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
assert timeToRot(oranges1) == 4

oranges2 = [
    [2,1,1],
    [0,1,1],
    [1,0,1]
]
assert timeToRot(oranges2) == -1

oranges3 = [
    [0,2]
]
assert timeToRot(oranges3) == 0

def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    pass

# Test Cases
courses1 = [ [1,0] ]
assert courseOrder(2, courses1) == [0, 1]

courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
assert courseOrder(4, courses2) in possibleSchedules

def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
    pass

# Test Cases
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

assert wordLadderLength(beginWord, endWord, wordList) == 5