class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows = len(grid)
        cols = len(grid[0])
        lands = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1": lands.add((i, j))
        ans = 0
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        surrounded = lambda l: lands & set([(l[0] + i, l[1] + j) for i, j in steps])
        while lands:
            island = {lands.pop()}
            ans += 1
            while island:
                land = island.pop()
                for other_land in surrounded(land):
                    x = abs(land[0] - other_land[0])
                    y = abs(land[1] - other_land[1])
                    if x == 1 and y == 0 or x == 0 and y == 1:
                        island.add(other_land)
                        lands.remove(other_land)
        return ans
