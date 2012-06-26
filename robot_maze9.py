# clean up move_multiple -- build hit_trap function that returns False if the robot hits a trap, so that only have one loop to break out of?
#                        -- or build detect_type function that filters the type of space and tells the program to do something accordingly?
# add in min and max moves
# make removing paths more efficient (eg if there is a trap on (0, 2), remove the paths (1, 2), (2, 2) etc)


import re, itertools

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
        '''creates a board with sublists [x-coord, y-coord, space-type] and returns a list of the sublists
        space type must be ., x, or o (empty, trap, goal space)'''
        
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
    
    board = create_board()
    print board
        
    def paths():
        "returns a list of possible paths the robot can take across the board (eg 1 space across and 1 space down)"
        
        paths = [i for i in itertools.product(range(height + 1), range(width + 1))]
        # the robot must move at least one space
        paths.remove((0, 0))
        return paths
        
    paths = paths()
        
    def move_x(location):
        "moves the robot 1 space to the right and returns the new location"
        
        new_x = location[0] + 1
        new_index = location[1] * (width + 1) + new_x # index of the new location in [board]
        new_location = [new_x, location[1], board[new_index][2]]
        assert new_location in board, "new location must be on the board"
        print "The robot has moved from", location, "1 space to the right to the new location", new_location
        return new_location
        
    def move_y(location):
        "moves the robot 1 space down and returns the new location"
    
        new_y = location[1] + 1
        new_index = new_y * (width + 1) + location[0] # index of the new location in [board]
        new_location = [location[0], new_y, board[new_index][2]]
        assert new_location in board, "new location must be on the board"
        print "The robot has moved from", location, "1 space down to the new location", new_location
        return new_location
        
#    def move_multiple(location, path):
#        new_location = location
#        while new_location[2] is not 'o':
#            for x in range(path[0]):
#                print 'old location', new_location
#                new_location = move_x(new_location)
#                print 'new location', new_location
#                if new_location[2] is 'x':
#                    for i in range(width):
#                        if (path[0] + i + 1, path[1]) in paths:
#                            paths.remove((path[0] + i + 1, path[1]))
#                            print 'removed', (path[0] + i + 1, path[1])
#                            print paths
#                    return True
#                if new_location[2] is 'o':
#                    break
#            for y in range(path[1]):
#                new_location = move_y(new_location)
#                print new_location
#                if new_location[2] is 'x':
#                    for i in range(height):
#                        if (path[0], path[1] + i + 1) in paths:
#                            paths.remove((path[0], path[1] + i + 1))
#                            print 'removed', (path[0], path[1] + i + 1)
#                            print paths
#                    return True
#                if new_location[2] is 'o':
#                    break
#            print new_location
#        print "the robot has reached the goal space!"
#        print new_location
#        return False


        
        
    def type_of_space(space):
        if space[2] is 'x':
            print 'The robot has hit a trap!'
            return False
        elif space[2] is 'o':
            print 'The robot has reached a goal space!'
            return True
        else:
            pass
            
    def move_multiple(location, path):
        new_location = location
        while True:
            for x in range(path[0]):
                print 'old location:', new_location
                new_location = move_x(new_location)
                if type_of_space(new_location) is False:
                    break
                elif type_of_space(new_location) is True:
                    return path
                print 'new location:', new_location
            for y in range(path[1]):
                print 'old location:', new_location
                new_location = move_y(new_location)
                if type_of_space(new_location) is False:
                    break
                elif type_of_space(new_location) is True:
                    return path
                print 'new location:', new_location
    
    
    
    
    
    
    
    
#        if space[2] is 'x' and axis is 'x':
#            print 'The robot has hit a trap along the x-axis!'
#            if space[0] is 0:
#                for x in range(space[0], width + 2):
#                    for y in range(height + 2):
#                        print 'about to remove', (x, y)
#                        remove_paths((x, y))
#                return False
#            else:
#                for i in range(height - space[1] + 2):
#                    remove_paths(space[0], i)
#                return False
#
#        elif space[2] is 'x' and axis is 'y':
#            print 'The robot has hit a trap along the y-axis!'
#            if space[1] is 0:
#                for y in range(space[1], height + 2):
#                    for x in range(width + 2):
#                        print 'about to remove', (x, y)
#                        remove_paths((x, y))
#                return False
#                
#                
#    def remove_paths(badpath):
#        if badpath in paths:
#            paths.remove(badpath)
#            print 'removed', badpath, 'from the list of possible paths'
#            print paths
        
    
        

    create_board()
    print paths
    for path in paths:
        move_multiple(board[0], path)
        print '\n\n'    
    
        
robot_puzzle('..xx.....', 1, 2, 3, 3)