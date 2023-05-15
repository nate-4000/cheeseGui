def get_legal_moves(board, x, y):
    piece = board[x][y]
    if piece is None:
        return []
    
    # Get the color of the piece (w for white, b for black)
    color = piece[0]
    
    # Get the type of the piece (p for pawn, r for rook, n for knight, b for bishop, q for queen, k for king)
    ptype = piece[1]
    
    # List to store legal moves
    legal_moves = []
    
    # Pawn moves
    if ptype == "p":
        # White pawn
        if color == "w":
            # Move one square forward
            if x > 0 and board[x-1][y] is None:
                legal_moves.append((x-1, y))
            
            # Move two squares forward (only on the pawn's starting square)
            if x == 6 and board[x-1][y] is None and board[x-2][y] is None:
                legal_moves.append((x-2, y))
            
            # Capture diagonally to the left
            if x > 0 and y > 0 and board[x-1][y-1] is not None and board[x-1][y-1][0] == "b":
                legal_moves.append((x-1, y-1))
            
            # Capture diagonally to the right
            if x > 0 and y < 7 and board[x-1][y+1] is not None and board[x-1][y+1][0] == "b":
                legal_moves.append((x-1, y+1))
        
        # Black pawn
        else:
            # Move one square forward
            if x < 7 and board[x+1][y] is None:
                legal_moves.append((x+1, y))
            
            # Move two squares forward (only on the pawn's starting square)
            if x == 1 and board[x+1][y] is None and board[x+2][y] is None:
                legal_moves.append((x+2, y))
            
            # Capture diagonally to the left
            if x < 7 and y > 0 and board[x+1][y-1] is not None and board[x+1][y-1][0] == "w":
                legal_moves.append((x+1, y-1))
            
            # Capture diagonally to the right
            if x < 7 and y < 7 and board[x+1][y+1] is not None and board[x+1][y+1][0] == "w":
                legal_moves.append((x+1, y+1))
    elif ptype == "r":
        # Check horizontally to the left
        for i in range(x-1, -1, -1):
            if board[i][y] is None:
                legal_moves.append((i, y))
            elif board[i][y][0] != color:
                legal_moves.append((i, y))
                break
            else:
                break
        
        # Check horizontally to the right
        for i in range(x+1, 8):
            if board[i][y] is None:
                legal_moves.append((i, y))
            elif board[i][y][0] != color:
                legal_moves.append((i, y))
                break
            else:
                break
        
        # Check vertically upwards
        for j in range(y-1, -1, -1):
            if board[x][j] is None:
                legal_moves.append((x, j))
            elif board[x][j][0] != color:
                legal_moves.append((x, j))
                break
            else:
                break
        
        # Check vertically downwards
        for j in range(y+1, 8):
            if board[x][j] is None:
                legal_moves.append((x, j))
            elif board[x][j][0] != color:
                legal_moves.append((x, j))
                break
            else:
                break
    
    # Knight moves
    elif ptype == "n":
        # Check all 8 possible knight moves
        knight_moves = [(x-2, y-1), (x-2, y+1), (x-1, y-2), (x-1, y+2), (x+1, y-2), (x+1, y+2), (x+2, y-1), (x+2, y+1)]
        for move in knight_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                if board[move[0]][move[1]] is None or board[move[0]][move[1]][0] != color:
                    legal_moves.append(move)
    
    # Bishop moves
    elif ptype == "b":
        # Check diagonally up and to the left
        i, j = x-1, y-1
        while i >= 0 and j >= 0:
            if board[i][j] is None:
                legal_moves.append((i, j))
            elif board[i][j][0] != color:
                legal_moves.append((i, j))
                break
            else:
                break
            i -= 1
            j -= 1
        
        # Check diagonally up and to the right
        i, j = x-1, y+1
        while i >= 0 and j < 8:
            if board[i][j] is None:
                legal_moves.append((i, j))
            elif board[i][j][0] != color:
                legal_moves.append((i, j))
                break
            else:
                break
            i -= 1
            j += 1
        
        # Check diagonally down and to the left
        i, j = x+1, y-1
        while i < 8 and j >= 0:
            if board[i][j] is None:
                legal_moves.append((i, j))
            elif board[i][j][0] != color:
                legal_moves.append((i, j))
                break
            else:
                break
            i += 1
            j -= 1
        
        # Check diagonally down and to the right
        i, j = x+1, y+1
        while i < 8 and j < 8:
            if board[i][j] is None:
                legal_moves.append((i, j))
            elif board[i][j][0] != color:
                legal_moves.append((i, j))
                break
            else:
                break
            i += 1
            j += 1
    
    # Queen moves
    elif ptype == "q":
        # Combine bishop and rook moves
        # Check diagonally up and to the left
        i, j = x-1, y-1
        while i >= 0 and j >= 0:
            if board[i][j] is None:
                legal_moves.append((i, j))
            elif board[i][j][0] != color:
                legal_moves.append((i, j))
                break
            else:
                break
            i -= 1
            j -= 1
        
        # Check diagonally up and to the right
        i, j = x-1, y+1
        while i >= 0 and j < 8:
            if board[i][j] is None:
                legal_moves.append((i, j))
            elif board[i][j][0] != color:
                legal_moves.append((i, j))
                break
            else:
                break
            i -= 1
            j += 1
        
        # Check diagonally down and to the left
        i, j = x+1, y-1
        while i < 8 and j >= 0:
            if board[i][j] is None:
                legal_moves.append((i, j))
            elif board[i][j][0] != color:
                legal_moves.append((i, j))
                break
            else:
                break
            i += 1
            j -= 1
        
        # Check diagonally down and to the right
        i, j = x+1, y+1
        while i < 8 and j < 8:
            if board[i][j] is None:
                legal_moves.append((i, j))
            elif board[i][j][0] != color:
                legal_moves.append((i, j))
                break
            else:
                break
            i += 1
            j += 1
        # Check horizontally to the left
        for i in range(x-1, -1, -1):
            if board[i][y] is None:
                legal_moves.append((i, y))
            elif board[i][y][0] != color:
                legal_moves.append((i, y))
                break
            else:
                break
        
        # Check horizontally to the right
        for i in range(x+1, 8):
            if board[i][y] is None:
                legal_moves.append((i, y))
            elif board[i][y][0] != color:
                legal_moves.append((i, y))
                break
            else:
                break
        
        # Check vertically upwards
        for j in range(y-1, -1, -1):
            if board[x][j] is None:
                legal_moves.append((x, j))
            elif board[x][j][0] != color:
                legal_moves.append((x, j))
                break
            else:
                break
        
        # Check vertically downwards
        for j in range(y+1, 8):
            if board[x][j] is None:
                legal_moves.append((x, j))
            elif board[x][j][0] != color:
                legal_moves.append((x, j))
                break
            else:
                break
    
    elif ptype == "k":
        # Check all 8 possible king moves
        king_moves = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
        for move in king_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                if board[move[0]][move[1]] is None or board[move[0]][move[1]][0] != color:
                    legal_moves.append(move)
    return legal_moves