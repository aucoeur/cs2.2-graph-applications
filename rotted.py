from collections import deque

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

if __name__ == "__main__":

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

    print(timeToRot(oranges3))