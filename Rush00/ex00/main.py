from checkmate import checkmate

def main():
    print("Test 1:")
    board1 = """\
.....
..R..
..K..
.....
....."""
    checkmate(board1)
    print("@" * 20)

    print("Test 2:")
    board2 = """\
.....
.....
..K..
.....
....."""
    checkmate(board2)
    print("@" * 20)

#     print("Test 3:")
#     board3 = """\
# .....
# .....
# ..K..
# .P...
# ....."""
#     checkmate(board3)
#     print("@" * 20)


    print("Test 4")
    board2 = """\
R...
.K.....
..P.
....\
"""
    checkmate(board2)
    print("@" * 20)

    print("Test 5")
    board2 = """\
R...
.K..
..K.
....\
"""
    checkmate(board2)
    print("@" * 20)

    print("Test 6")
    board2 = """\
...
R...
....
..P.
....\
"""
    checkmate(board2)
    print("@" * 20)

    #เพิ่มเติม
    print("Test 7")
    board2 = """\
..K.
..P.
..Q.\
"""
    checkmate(board2)
    print("@" * 20)
    
    print("Test 8")
    board3 = """\
...
.K.
P.P\
"""
    checkmate(board3)
    print("@" * 20)

    print("Test 9")
    board4 = """\
....
.Q..
....\
"""
    checkmate(board4)

if __name__ == "__main__":
    main()
