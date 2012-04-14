def robot_puzzle(string, min_moves, max_moves, width, height):
    board_list = list(string)
    # adds goal spaces to the right side of the board
    for elem in range(0, height):
        board_list.insert(((width * elem) + (width + elem)), 'o')
    # adds goal spaces to the bottom of the board
    for elem in range (0, width + 1):
        board_list.append('o')
    print board_list
    # turns the original string into tuples of (x-coord, y-coord, type of space (., x, or o)
    board = []

    for index, elem in enumerate(board_list):
        x = index % (width + 1) # x coordinate
        y = index /(width + 1) # y coordinate
        z = elem # actual element (. or x or o)
        board.append((x, y, z))
    for tuple in board:
        print tuple
    
        
    def move_robot_x(location, x):
        new_x = location[0] + x
        new_location_index = location[1] * (width + 1) + new_x # the index of the new location in 'board'
        new_location = (new_x, location[1], board[new_location_index][2]) # should be the same as new_location_index, assuming that 
        # everything has looped correctly (current_location currently has the potential to be off the board)
        print "The robot has moved from", location, x, "space/s to the right to the new location", new_location
        return new_location
        
    def move_robot_y(location, y):
        new_y = location[1] + y
        new_location_index = new_y * (width + 1) + location[0] # the index of the new location in 'board'
        new_location = (location[0], new_y, board[new_location_index][2]) # should be the same as new_location_index, assuming that 
        # everything has looped correctly (current_location currently has the potential to be off the board)
        print "The robot has moved from", location, y, "space/s down to the new location", new_location
        return new_location

    
    def move_robot_multiple(location, x, y):
        new_location = location
        for i in range(0, x):
            new_location = move_robot_x(new_location, 1)
        for j in range (0, y):
            new_location = move_robot_y(new_location, 1)
        print new_location
    
    
       
    start_location = board[0]
#    move_robot_multiple(start_location, 0, 0)
#    move_robot_multiple(start_location, 1, 0)
#    move_robot_multiple(start_location, 1, 1)
    move_robot_multiple(start_location, 2, 2)
    
                
                
# Testing
robot_puzzle('..xx.....', 1, 2, 3, 3)
robot_puzzle('...xxx.x', 1, 2, 4, 2)