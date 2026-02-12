def checkmate(board):
    lines = board.strip().split('\n')
    if not lines:
        print("Empty board ja")
        return

    #grid
    grid = []
    character = set("KPRBQ.")
    
    for line in lines:
        cleaned_line = ""
        for crt in line:
            cleaned_line += crt if crt in character else "."
        grid.append(cleaned_line)

    #size board
    rows = len(grid)
    cols = len(grid[0])

    #square
    if any(len(row) != rows for row in grid):
        print("Board is not square!!!!!!!!")
        return

    #king position
    king_posi = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'K':
                king_posi.append((r, c))

    #king
    if len(king_posi) == 0:
        print("king not found na ka")
        return
    elif len(king_posi) > 1:
        print("found a lot of kings!!!!!")
        return

    king_r, king_c = king_posi[0]

    #bound
    def bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    #check pawn
    pawn_offsets = [(-1), (1)] 
    
    for offset in pawn_offsets:
        p_r, p_c = king_r + 1, king_c + offset
        if bounds(p_r, p_c) and grid[p_r][p_c] == 'P':
            print("Success")
            return

    #scan direction
    def scan_dir(directions, enemy):
        for dr, dc in directions:
            curr_r, curr_c = king_r + dr, king_c + dc 
            while bounds(curr_r, curr_c):
                piece = grid[curr_r][curr_c]
                if piece in enemy:
                    return True
                if piece != '.':
                    break
                
                curr_r += dr
                curr_c += dc

        return False

    #direction
    straight_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    diag_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    #checj Rook,Queen 
    if scan_dir(straight_moves, "RQ"):
        print("Success")
        return

    #check bishop,Queen 
    if scan_dir(diag_moves, "BQ"):
        print("Success")
        return
    print("Fail")