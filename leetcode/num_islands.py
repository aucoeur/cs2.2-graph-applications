'''https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        vertex_dict = {}    
        edges = []
        
        # loop through array
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                cell_type = grid[x][y]
                if cell_type == 1:
                    new_vertex = Vertex(f'{x},{y}')
                    
                    if x > 0 and grid[x -1][y] == 1:
                        edges.append((f'{x},{y}'),(f'{x-1},{y}'))
                    if y > 0 and grid[x][y - 1] == 1:
                        edges.append((f'{x},{y}'),(f'{x},{y - 1}'))
                    if x < len(grid[x]) -1 and grid[x + 1][y] == 1:
                        edges.append((f'{x},{y}'),(f'{x+1},{y}'))
                    if y > 0 and grid[x][y - 1] == 1:
                        edges.append((f'{x},{y}'),(f'{x},{y - 1}'))
                        
  # 0, 0 -> 0, 1
  # 1, 0  
        
class Vertex(object):
    def __init__(self, vertex_id):
        self.__id = vertex_id
        self.__neighbors = {}
        
    def add_neighbor(self, vertex_obj):
        self.__neighbors[vertex_obj.__id] = vertex_obj
        
    def get_neighbors(self):
        return list(self.__neighbors.values())
    
    def get_id(self):
        return self.__id


            