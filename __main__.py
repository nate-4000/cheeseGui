import pygame
from getLegalMoves import get_legal_moves

pygame.init()

board = [
    ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]
]

ranks = ["a","b","c","d","e","f","g","h","wtf"]

screen = pygame.display.set_mode((800,800), pygame.RESIZABLE)

def iOWS(x, y):
    # if x+y is odd, the square is black; if it's even, the square is white
    if (x + y) % 2 == 1:
        return 0x7f7f7f  # white
    else:
        return 0xf7f7f7  # black

def boardToFen(board, player):
    fen = ''
    empty = 0
    for row in board:
        for piece in row:
            if piece is None:
                empty += 1
            else:
                if empty > 0:
                    fen += str(empty)
                    empty = 0
                if piece[0] == "w":
                    fen += piece[1].lower()
                else:
                    fen += piece[1].upper()
        if empty > 0:
            fen += str(empty)
            empty = 0
        fen += '/'
    fen = fen[:-1]  # remove last '/'
    fen += ' {} - - 0 1'.format(player)  # add remaining FEN fields
    return fen
    
def move_piece(selectedPiece, pos, board):
    x1, y1 = selectedPiece
    x2, y2 = pos
    piece = board[x1][y1]
    if piece is None:
        return
    if (x2, y2) in get_legal_moves(board, x1, y1):
        if board[x2][y2] is not None:
            if board[x2][y2][0] != piece[0]:  # check if captured piece is of opposite color
                board[x2][y2] = piece
                board[x1][y1] = None
            else:
                return
        else:
            board[x2][y2] = piece
            board[x1][y1] = None


Exit = False
lx, ly = 7, 7
selectedPiece = None
selectedPieceMoves = []
mover = "w"
hundred = 100

while not Exit:
    screensize = screen.get_size()
    hundred = min(screensize) // 8
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            lastx, lasty = lx, ly
            lx, ly = mouse_pos[1] // hundred, mouse_pos[0] // hundred
            piece = board[lx][ly]
            if piece is not None and not ((lx, ly) in get_legal_moves(board, lastx, lasty)):
                selectedPiece = (lx, ly)
                selectedPieceMoves = get_legal_moves(board, *selectedPiece)
            else:
                if (lx, ly) in selectedPieceMoves and mover == board[selectedPiece[0]][selectedPiece[1]][0]:
                    move_piece(selectedPiece, (lx, ly), board)
                    selectedPiece = None
                    selectedPieceMoves = []
                    if mover == "w":
                        mover = "b"
                    else:
                        mover = "w"
                    fen = boardToFen(board, mover)
                    print(fen)
                    # print("%s%d" % (ranks[lasty], lastx)) # dont trust it
            
    screen.fill(0)
    for y in range(0, 8):
        for x in range(0, 8):
            piece = board[x][y]
            pygame.draw.rect(screen, iOWS(x, y), pygame.Rect(y*hundred,x*hundred,y*hundred+hundred,x*hundred+hundred))
            if piece is not None:
                filename = "peices\\{}.png".format(piece)
                image = pygame.image.load(filename)
                image = pygame.transform.scale(image, (hundred, hundred))
                screen.blit(image, (y*hundred, x*hundred))
            if (x, y) == selectedPiece:
                pygame.draw.rect(screen, 0xff0000, pygame.Rect(y*hundred,x*hundred,y*hundred+hundred,x*hundred+hundred), 2)
            if (x, y) in selectedPieceMoves:
                pygame.draw.circle(screen, 0x00ff00, (y*hundred+(hundred // 2), x*hundred+(hundred // 2)), hundred // 5)


    pygame.display.flip()

pygame.quit()
