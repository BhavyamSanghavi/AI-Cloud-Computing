import copy
import heapq
n = 3
row = [1, 0, -1, 0]  # Directions for movement
col = [0, -1, 0, 1]

# h(n)
def calculateCost(mat, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] != 0 and mat[i][j] != final[i][j]:
                count += 1
    return count

# Function to create a new node
def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final) -> tuple:
    # Copy data from parent matrix to current matrix
    new_mat = copy.deepcopy(mat)
    
    # Move tile by 1 position
    x1, y1 = empty_tile_pos
    x2, y2 = new_empty_tile_pos
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

    # Calculate number of misplaced tiles
    cost = calculateCost(new_mat, final)
    #x,y=y,x
    # Return a tuple of (cost, level, mat, empty_tile_pos, parent)
    return (cost + level, level, new_mat, new_empty_tile_pos, parent)

# Function to print the N x N matrix
def printMatrix(mat):
    for i in range(n):
        for j in range(n):
            print("%d " % (mat[i][j]), end=" ")
        print()

# Function to check if (x, y) is a valid matrix coordinate
def isSafe(x, y):
    return 0 <= x < n and 0 <= y < n

# Print path from root node to destination node
def printPath(root):
    if root is None:
        return
    printPath(root[4])  # Recursively print the parent node
    printMatrix(root[2])  # Print the matrix
    print("Level=",root[1], " Cost=",root[0]-root[1], "F(n)=",root[0])      # print level(g(n)) and h(n)
    print()

# Function to solve N*N - 1 puzzle algorithm using Branch and Bound
def solve(initial, empty_tile_pos, final):
    pq = []

    # Create the root node (cost, level, matrix, empty_tile_pos, parent)
    cost = calculateCost(initial, final)
    root = (cost, 0, initial, empty_tile_pos, None)

    heapq.heappush(pq, root)
    
    while pq:
        minimum = heapq.heappop(pq)

        if minimum[0] == minimum[1]:
            printPath(minimum)
            return
        # Generate all possible children (cost, level, matrix, empty_tile_pos, parent)
        for i in range(4):
            new_tile_pos = [minimum[3][0] + row[i], minimum[3][1] + col[i]]

            if isSafe(new_tile_pos[0], new_tile_pos[1]):
                child = newNode(minimum[2], minimum[3], new_tile_pos, minimum[1] + 1, minimum, final)
                heapq.heappush(pq, child)

initial = [[1, 2, 3],
           [5, 6, 0],
           [7, 8, 4]]

final = [[1, 2, 3],
         [5, 8, 6],
         [0, 7, 4]]
empty_tile_pos = [1, 2]
solve(initial, empty_tile_pos, final)