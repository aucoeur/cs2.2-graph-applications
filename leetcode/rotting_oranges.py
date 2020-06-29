class Solution:
    def orangesRotten(self, grid:List[List[int]]) -> int:
        # make queue of (row, col, timestamp)
        queue = collections.deque()

        # store highest timestamp, start at 0
        highest_timestamp = 0
        rows = len(grid)
        cols = len(grid[0])

        # put all rotten oranges (2s) into the queue
        # with timestamp of 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        # while queue not empty
        while queue:
            
            # pop from queue
            (row, col, timestamp) =  queue.popleft()

            # infect neighbors
            if row > 0 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                queue.append((row-1, col, timestamp + 1))
            if row < rows - 1 and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                queue.append((row+1, col, timestamp + 1))
            
            # update highest timestamp

        # if there are any fresh oranges
        # return -1

        # return highest timestamp