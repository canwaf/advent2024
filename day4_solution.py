# Read in the file
search = list()
with open('day4_input.txt', 'r') as f:
    for line in f:
        search.append([char for char in line.strip()])

def matrix(x, y, max_x, max_y):
    directions = [
        ((x, y), (x+1, y), (x+2, y), (x+3, y)),
        ((x, y), (x-1, y), (x-2, y), (x-3, y)),
        ((x, y), (x, y-1), (x, y-2), (x, y-3)),
        ((x, y), (x, y+1), (x, y+2), (x, y+3)),
        ((x, y), (x+1, y-1), (x+2, y-2), (x+3, y-3)),
        ((x, y), (x-1, y-1), (x-2, y-2), (x-3, y-3)),
        ((x, y), (x+1, y+1), (x+2, y+2), (x+3, y+3)),
        ((x, y), (x-1, y+1), (x-2, y+2), (x-3, y+3))
    ]
    
    filtered_directions = []
    for direction in directions:
        if all(0 <= coord[0] < max_x and 0 <= coord[1] < max_y for coord in direction):
            filtered_directions.append(direction)
    
    return filtered_directions

def cross(x, y, max_x, max_y):
    directions = [((x-1, y+1), (x,y), (x+1, y-1)),
                  ((x+1, y+1), (x, y), (x-1, y-1))]

    filtered_directions = []
    for direction in directions:
        if all([0 <= coord[0] < max_x and 0 <= coord[1] < max_y for coord in direction]):
            filtered_directions.append(direction)
    
    if len(filtered_directions) == 2:
        return filtered_directions
    else:
        return None

def xmas(search) -> int:
    x = 0
    y = 0
    tally = 0
    jolly = ["X", "M", "A", "S"]
    max_x = len(search[0])
    max_y = len(search)

    print(f"max_x: {max_x}, max_y: {max_y}")

    for y in range(0, max_x):
        for x in range(0, max_y):
        
            for direction in matrix(x=x, y=y, max_x=max_x, max_y=max_y):

                # print(direction)

                # print([search[coord[0]][coord[1]] for coord in direction], direction)
                result = [search[coord[0]][coord[1]] for coord in direction]
                if result == jolly:
                    tally += 1
                    # print(f"Found a jolly at {x}, {y}")
                else:
                    continue
                    
    return tally

def crossmas(search) -> int:
    x = 0
    y = 0
    tally = 0
    jolly = ["M", "A", "S"]
    max_x = len(search[0])
    max_y = len(search)

    print(f"max_x: {max_x}, max_y: {max_y}")

    for y in range(0, max_x):
        for x in range(0, max_y):
            
            mas = 0

            diagonals = cross(x=x, y=y, max_x=max_x, max_y=max_y)

            if diagonals is None:
                continue

            for direction in diagonals:

                # print(direction)

                result = [search[coord[0]][coord[1]] for coord in direction]
                print(result, direction, result==["S", "A", "M"] or result==["M", "A", "S"])

                if result==["S", "A", "M"] or result==["M", "A", "S"]:
                    mas += 1
                    print(f"Found a jolly at {x}, {y}")
                else:
                    break

            if mas == 2:
                tally += 1

                    
    return tally

print(f"The count of XMAS is {xmas(search)}.")
print(f"The count of crosses of MAS is {crossmas(search)}.")
      

            
