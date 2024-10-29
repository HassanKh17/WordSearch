"""
Introduction to Programming: Coursework 1
Please write your name
@author:Hassan Khawaja Ahmed Roohi

"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None:
    # This checks whether the puzzled passed is valid or not
    if valid_puzzle(puzzle) == False:
        print("ValueError, Invalid puzzle")
    # This checks whether the wordlist passed is valid or not
    if valid_wordlist(wordlist) == False:
        print("ValueError, Invalid Wordlist")

    else:
        final_list = []
        for word in wordlist:
            word = word.upper()
            temp = get_positions(puzzle, word)
            if temp is not None:
                final_list.append(temp)
        coloured_display(puzzle, final_list)

# The purpose of this function is to check whether the puzzle is valid or not


def valid_puzzle(puzzle: list) -> bool:
    # This checks whether the items in the sublists are strings or not
    if all(isinstance(item, (str)) for item in puzzle):
        itr = iter(puzzle)
        stringlen = len(next(itr))
        # This checks if the all the sublists in the lists are of the same length
        if not all(len(puzzle) == stringlen for puzzle in itr):
            print("Puzzle is Invalid: Not same length of string")
            return False
        else:
            print("Puzzle is Valid")
            return True
    else:
        print("Invalid Puzzle: Not a string")
        return False

# This function checks if the wordlist is valid or not


def valid_wordlist(wordlist: list) -> bool:
    # This checks that the wordlist only consists of integers
    if all(isinstance(word, (str)) for word in wordlist):
        print("Word list is valid")
        return True
    else:
        print("Invalid Word list")
        return False

# This functions returns the list of the coordinates of the characters when a word is found


def get_positions(puzzle: list, word: str) -> list:
    # This refers to first letter of the word we have to find coordinates for
    fWord = word[0]
    # This is the list in which the coordinates would be passed on
    allSol = []
    # This loop will go through the outer list of the list puzzle
    for row in range(0, len(puzzle)):
        # This loop will go through each sublist of the list
        for col in range(0, len(puzzle[row])):
            # This checks whether a letter in the character matches the first letter of the word we are finding
            if fWord == puzzle[row][col]:

                # ==================================================
                # Horizontal Right
                # ==================================================
               # This checks if there are enough characters on right side of the character same as the first letter of the word we are finding
                if len(word) <= (len(puzzle[0])-col):
                    list2 = []
                    indextuple = []
                    r = row
                    c = col
                    # This will read all the characters on the same row incrementing column each time, starting from the first matching character until it has read as many characters as lenght of the word we finding
                    for z in range(c, c+len(word)):
                        # This will append the characters read into the list
                        list2.append(puzzle[r][z])
                        # This will apend the coordinates of characters as tuple into a list
                        indextuple.append(tuple((r, z)))
                        # This will convert our word string into a list of string so it can be comapared later
                        checklist = list(word)
                    # This checks if the characters read are same as the word we were finding
                    if list2 == checklist:
                        allSol.append(indextuple)

# ==================================================
                # Horizontal Left
# ==================================================
# This checks if there are enough characters on left side of the character same as the first letter of the word we are finding
                if len(word) <= (col+1):
                    list2 = []
                    indextuple = []
                    r = row
                    c = col
                    # This will read all the characters on the same row decrementing column each time, starting from the first matching character until it has read as many characters as lenght of the word we finding
                    for z in range(c, ((c)-len(word)), -1):
                        # This will append the characters read into the list
                        list2.append(puzzle[r][z])
                        # This will apend the coordinates of characters as tuple into a list
                        indextuple.append(tuple((r, z)))
                        # This will convert our word string into a list of string so it can be comapared later
                        checklist = list(word)
                    # This checks if the characters read are same as the word we were finding
                    if list2 == checklist:
                        allSol.append(indextuple)

# ==================================================
                # Vertical Down
# ==================================================
# This checks if there are enough characters on down side of the character same as the first letter of the word we are finding
                if len(word) <= (len(puzzle)-row):
                    list2 = []
                    indextuple = []
                    r = row
                    c = col
                    # This will read all the characters on the same column incrementing row each time, starting from the first matching character until it has read as many characters as lenght of the word we finding
                    for z in range(r, r+(len(word))):
                        # This will append the characters read into the list
                        list2.append(puzzle[z][c])
                        # This will apend the coordinates of characters as tuple into a list
                        indextuple.append(tuple((z, c)))
                        # This will convert our word string into a list of string so it can be comapared later
                        checklist = list(word)
                    # This checks if the characters read are same as the word we were finding
                    if list2 == checklist:
                        allSol.append(indextuple)

# ==================================================
                # Vertical Up
# ==================================================
# This checks if there are enough characters on up side of the character same as the first letter of the word we are finding
                if len(word) <= (row+1):
                    list2 = []
                    indextuple = []
                    r = row
                    c = col
                    # This will read all the characters on the same column decrementing row each time, starting from the first matching character until it has read as many characters as lenght of the word we finding
                    for z in range(r, (r-len(word)), -1):
                        # This will append the characters read into the list
                        list2.append(puzzle[z][c])
                        # This will apend the coordinates of characters as tuple into a list
                        indextuple.append(tuple((z, c)))
                        # This will convert our word string into a list of string so it can be comapared later
                        checklist = list(word)
                    # This checks if the characters read are same as the word we were finding
                    if list2 == checklist:
                        allSol.append(indextuple)

# ==================================================
                # Diagonal Up Right
# ==================================================
# This checks if there are enough characters on diagonal up right side of the character same as the first letter of the word we are finding
                if (len(word) <= len(puzzle[0])-col) and (row+1):
                    list2 = []
                    indextuple = []
                    r = row
                    c = col
                    # This will read all the characters on the same row incrementing column each time, starting from the first matching character until it has read as many characters as lenght of the word we finding
                    for z in range(c, c+len(word)):
                        # This will append the characters read into the list
                        list2.append(puzzle[r][z])
                        # This will apend the coordinates of characters as tuple into a list
                        indextuple.append(tuple((r, z)))
                        # This will convert our word string into a list of string so it can be comapared later
                        checklist = list(word)
                        # This decrements the row number each time
                        r -= 1
                    # This checks if the characters read are same as the word we were finding
                    if list2 == checklist:
                        allSol.append(indextuple)

# ==================================================
                # Diagonal Down Right
# ==================================================
# This checks if there are enough characters on diagonal down right side of the character same as the first letter of the word we are finding
                if len(word) <= (len(puzzle[0])-col) and len(puzzle)-row:
                    list2 = []
                    indextuple = []
                    r = row
                    c = col
                    # This will read all the characters on the same row incrementing column each time, starting from the first matching character until it has read as many characters as lenght of the word we finding
                    for z in range(c, c+len(word)):
                        # This checks if the last row has been reached
                        if r == 11:
                            r -= 1
                        # This will append the characters read into the list
                        list2.append(puzzle[r][z])
                        # This will apend the coordinates of characters as tuple into a list
                        indextuple.append(tuple((r, z)))
                        # This will convert our word string into a list of string so it can be comapared later
                        checklist = list(word)
                        # This increments the row number
                        r += 1
                    # This checks if the characters read are same as the word we were finding
                    if list2 == checklist:
                        allSol.append(indextuple)

# ==================================================
                # Diagonal Up Left
# ==================================================
# This checks if there are enough characters on diagonal up left side of the character same as the first letter of the word we are finding
                if (len(word) <= col+1) and (row+1):
                    list2 = []
                    indextuple = []
                    c = col
                    r = row
                    # This will read all the characters on the same row decrementing column each time, starting from the first matching character until it has read as many characters as lenght of the word we finding
                    for z in range(c, ((c)-len(word)), -1):
                        # This will append the characters read into the list
                        list2.append(puzzle[r][z])
                        # This will apend the coordinates of characters as tuple into a list
                        indextuple.append(tuple((r, z)))
                        # This will convert our word string into a list of string so it can be comapared later
                        checklist = list(word)
                        # This decrements the row number
                        r -= 1
                    # This checks if the characters read are same as the word we were finding
                    if list2 == checklist:
                        allSol.append(indextuple)

# ==================================================
                # Diagonal Left Down
# ==================================================
# This checks if there are enough characters on diagonal down left side of the character same as the first letter of the word we are finding
                if len(word) <= (col+1) and len(puzzle)-row:
                    list2 = []
                    indextuple = []
                    r = row
                    c = col
                    # This will read all the characters on the same row decrementing column each time, starting from the first matching character until it has read as many characters as lenght of the word we finding
                    for z in range(c, (c-len(word)), -1):
                        if r == 11:
                            r -= 1
                        # This will append the characters read into the list
                        list2.append(puzzle[r][z])
                        # This will apend the coordinates of characters as tuple into a list
                        indextuple.append(tuple((r, z)))
                        # This will convert our word string into a list of string so it can be comapared later
                        checklist = list(word)
                        # This increments the row number
                        r += 1
                    # This checks if the characters read are same as the word we were finding
                    if list2 == checklist:
                        allSol.append(indextuple)

    return (allSol)


# This function is responsible for producing the basic display
def basic_display(grid: list) -> None:
    # This loops through the outer list so going through each sublist
    for row in range(0, len(grid)):
        # This loops through the sublist so going through the each string of character
        for col in range(0, len(grid[row])):
            # This prints each character is sublist and separate them by a space and moves to next line when a sub string ends
            print(" "+grid[row][col]+" ", end="")
        print(sep="")

# This function is responsible for producing the colored display


def coloured_display(grid: list, positions: list) -> None:
    # This loop goes through the outer list of the grid
    for row in range(0, len(grid)):
        # This loop goes through each sublist of the grid
        for col in range(0, len(grid[row])):
            cGrid = [""]
            # This loop goes through the outer list which carries the sublists carrying the indices
            for i in range(0, len(positions)):
                # This loop goes through the sublist whihc contains the coordinates of words
                for j in range(0, len(positions[i])):
                    # This loop goes through each coordinate of the character
                    for k in range(0, len(positions[i][j])):
                        comp = tuple((row, col))
                        if comp == positions[i][j][k]:
                            cGrid[0] = grid[row][col]
            # This checks if the coordinate in the grid are same as the character's coordinate
            if cGrid[0] == grid[row][col]:
                # This colors the (row,column) of the characters we have found
                print("\033[42m"+" "+grid[row][col]+" "+"\033[0m", end="")
            else:
                print(" "+grid[row][col]+" ", end="")
        print(sep="")


# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist1 = ["yellow", "worb", "owqn",
                      "PINK", "naw", "beai", "tab", "glde"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist1))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_puzzle1 = ["BXHPBLACK", "BGOIEFWFI", "NYQNPDHAQ", "QGTKGREEN",
                    "WHITEBLUE", "ORANGEGUY", "UBLYELLOW", "KXMGZPDRR", "BROWNTRED"]

    print("puzzle1 is", valid_puzzle(good_puzzle))
    print("puzzle2 is", valid_puzzle(bad_puzzle1))
    print("puzzle3 is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle2 = ["BXHPBLACK", "BGOIEFWFI", "NYQNPDHAQ", "QGTKGREEN",
               "WHITEBLUE", "ORANGEGUY", "UBLYELLOW", "KXMGZPDRR", "BROWNTRED"]

    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle2)
    #basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle2 = ["BXHPBLACK", "BGOIEFWFI", "NYQNPDHAQ", "QGTKGREEN",
               "WHITEBLUE", "ORANGEGUY", "UBLYELLOW", "KXMGZPDRR", "BROWNTRED"]
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    #get_positions(puzzle2, "TESTING")
    print(get_positions(puzzle2, "YELLOW"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]

    final_list = []
    for word in good_wordlist2:
        word = word.upper()
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # basic solution
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    test_get_positions()
    # test_wordsearch()
