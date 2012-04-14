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