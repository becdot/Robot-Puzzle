# make removing paths more efficient (eg if there is a trap on (0, 2), remove the paths (1, 2), (2, 2) etc)


import itertools

def robot_puzzle(string, min_moves, max_moves, width, height):

    def add_goals():
        "adds goal spaces along the right side and bottom of the board, and returns board_list"
        # turns the original string into a list for ease of modifying
        board_list = list(string)
        # adds goal spaces to the right side of the board
        for elem in range(0, height):
            board_list.insert(((width * elem) + (width + elem)), 'o')
        # adds goal spaces to the bottom of the board
        for elem in range (0, width + 1):
            board_list.append('o')
        return board_list
        
    def create_board():
        "creates a board with sublists [x-coord, y-coord, space-type] and returns a list of the sublists\
        space type must be ., x, or o (empty, trap, goal space)"
        
        board_list = add_goals()
        board = []
        for index, elem in enumerate(board_list):
            x = index % (width + 1) # x coordinate
            y = index /(width + 1) # y coordinate
            z = elem # actual element (. or x or o)
            board.append([x, y, z])
        for list in board:
            print list
        print "\nThis is a %d by %d board\n" % (width, height)
        return board
            
    def paths():
        "returns a list of possible paths the robot can take across the board (eg 1 space across and 1 space down)"
        paths = [i for i in itertools.product(range(height + 1), range(width + 1))]
        # the robot must move at least one space
        paths.remove((0, 0))
        return paths
        
    def minmax_moves():
        "removes any paths that are > max_moves or < min_moves"
        for path in paths[:]:
            if path[0] + path[1] > max_moves or path[0] + path[1] < min_moves:
                paths.remove(path)
                
    def move_x(location):
        "moves the robot 1 space to the right and returns the new location"
        new_x = location[0] + 1
        new_index = location[1] * (width + 1) + new_x # index of the new location in [board]
        new_location = [new_x, location[1], board[new_index][2]]
        assert new_location in board, "new location must be on the board"
        #print "The robot has moved from", location, "1 space to the right to the new location", new_location
        return new_location
        
    def move_y(location):
        "moves the robot 1 space down and returns the new location"
        new_y = location[1] + 1
        new_index = new_y * (width + 1) + location[0] # index of the new location in [board]
        new_location = [location[0], new_y, board[new_index][2]]
        assert new_location in board, "new location must be on the board"
        #print "The robot has moved from", location, "1 space down to the new location", new_location
        return new_location
        
    def move_multiple_x(location, path):
        "moves the robot the number of spaces right, as specified by path"
        new_location = location
        for x in range(path[0]):
            #print 'old location:', new_location
            new_location = move_x(new_location)
            if new_location[2] is not '.':
                return new_location[2]
            #print 'new location:', new_location
        return new_location
        
    def move_multiple_y(location, path):
        "moves robot the number of spaces down, as specified by path"
        new_location = location
        for y in range(path[1]):
            #print 'old location:', new_location
            new_location = move_y(new_location)
            if new_location[2] is not '.':
                return new_location[2]
            #print 'new location:', new_location
        return new_location
        
    def move_multiple_right(location, path):
        "moves the robot right and down of the specified path (1 set)"
        x_location = move_multiple_x(location, path)
        if x_location is 'x' or x_location is 'o':
            return x_location
        y_location = move_multiple_y(x_location, path)
        return y_location
        
    def move_multiple_down(location, path):
        "moves the robot down and right of the specified path (1 set)"
        y_location = move_multiple_y(location, path)
        if y_location is 'x' or y_location is 'o':
            return y_location
        x_location = move_multiple_x(y_location, path)
        return x_location
        
    def robot_movement(move_multiple, location, path):
        "loops the path until the robot hits either a goal or a trap"
        new_location = location
        while new_location is not 'o' or 'x':
            if isinstance(new_location, list):
                new_location = move_multiple(new_location, path)
            else:
                return new_location
                
        
    board = create_board()
    paths = paths()
    # modifies the list of paths to remove paths that are > # max_moves and < # min_moves
    minmax_moves()
    
    winning_paths_right = []   
    winning_paths_down = []
    for path in paths:
        #print path
        path_result_right = robot_movement(move_multiple_right, board[0], path)
        path_result_down = robot_movement(move_multiple_down, board[0], path)
        if path_result_right is 'o':
            winning_paths_right.append(path)
        elif path_result_down is 'o':
            winning_paths_down.append(path)
            
    print "The winning paths are:"
    for path in winning_paths_right: print path, ('R' * path[0] + 'D' * path[1])
    for path in winning_paths_down: print path, ('D' * path[1] + 'R' * path[0])
    
        
# Testing
robot_puzzle('..xx.....', 1, 2, 3, 3)    
print '\n\n'
robot_puzzle('..xxx.xxx..xxx.xxx..xxx.', 1, 3, 4, 6)
print '\n\n'
robot_puzzle('.x....x........xxxx.', 1, 6, 5, 4)
    

