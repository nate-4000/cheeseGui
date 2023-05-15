import pygame
from getLegalMoves import get_legal_moves

pygame.init()

board = [
    ["br", "bn", "bb", "bk", "bq", "bb", "bn", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wn", "wb", "wk", "wq", "wb", "wn", "wr"]
]

screen = pygame.display.set_mode((800,800))

def iOWS(x, y):
    # If x+y is odd, the square is black; if it's even, the square is white
    if (x + y) % 2 == 0:
        return 0x7f7f7f  # white
    else:
        return 0xf7f7f7  # black

def board_to_fen(board, player):
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
    
def move_piece(selected_piece, pos, board):
    x1, y1 = selected_piece
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
selected_piece = None
selected_piece_moves = []
mover = "w"

while not Exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Exit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            lastx, lasty = lx, ly
            lx, ly = mouse_pos[1] // 100, mouse_pos[0] // 100
            piece = board[lx][ly]
            if piece is not None and not ((lx, ly) in get_legal_moves(board, lastx, lasty)):
                selected_piece = (lx, ly)
                selected_piece_moves = get_legal_moves(board, *selected_piece)
            else:
                if (lx, ly) in selected_piece_moves and mover == board[selected_piece[0]][selected_piece[1]][0]:
                    move_piece(selected_piece, (lx, ly), board)
                    selected_piece = None
                    selected_piece_moves = []
                    if mover == "w":
                        mover = "b"
                    else:
                        mover = "w"
                    print(board_to_fen(board, mover))
            
    screen.fill(0)
    for y in range(0, 8):
        for x in range(0, 8):
            pygame.draw.rect(screen, iOWS(x, y), pygame.Rect(y*100,x*100,y*100+100,x*100+100))
            if (x, y) == selected_piece:
                pygame.draw.rect(screen, 0xff0000, pygame.Rect(y*100,x*100,y*100+100,x*100+100), 5)
            if (x, y) in selected_piece_moves:
                pygame.draw.circle(screen, 0x00ff00, (y*100+50, x*100+50), 20)
            piece = board[x][y]
            if piece is not None:
                filename = "peices\\{}.png".format(piece)
                image = pygame.image.load(filename)
                image = pygame.transform.scale(image, (100, 100))
                screen.blit(image, (y*100, x*100))

    pygame.display.flip()

pygame.quit()