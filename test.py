import copy


def add_coin(board, coin, column) :
    """
    This function takes a list of lists representing the current state of board, the character reprensenting the current player's coin
    and an integer reprensenting the column in which the player is inserting their coin.
    Returns a list of lists reprensenting the new state of the board after the coin has been played.
    """
    column -= 1
    index = len(board) - 1
    while index >= 0:
        row = board[index]
        if row[column] == 0:
            row[column] = coin
            break
        else:
            index -= 1
        continue
    return board

def is_winner(board, coin):
    result = False
    for index, row in enumerate(board):
        for i, item in enumerate(row):
            j = i + 1
            if j >= len(row)-1:
                j = len(row)-1
            if item == row[j] == coin and i != j:
                idx = index + 1
                if idx >= len(board)-1:
                    idx = len(board)-1
                if board[idx][i] == board[idx][j] == coin and index != idx:
                    result = True
            else:
                continue
    return result


# print(is_winner([[0, 0, 0, 0], ['R', 'Y', 'Y', 'R'], [
#       'R', 'R', 'Y', 'R'], ['R', 'R', 'Y', 'R']], 'R'))


def heuristic(board, coin):
    result = 0
    for index, currentRow in enumerate(board):
        if index < len(board)-1:
            for i, item in enumerate(currentRow):
                if i < len(currentRow)-1:
                    j = i + 1
                    nextRowIndex = index + 1
                    nextRow = board[nextRowIndex]
                    tempArray = [item, currentRow[j], nextRow[i], nextRow[j]]
                    if tempArray.count(coin) == 4:
                        result += 1000
                    elif tempArray.count(coin) == 3:
                        result += 100
                    elif tempArray.count(coin) == 2 and tempArray.count(0) == 2:
                        result += 10
                    elif tempArray.count(coin) == 1 and tempArray.count(0) == 3:
                        result += 1
                    else: result += 0
                else: break
        else:
            break
    return result

# print(heuristic([[0, 0, 0, 0], ['R', 'Y', 'Y', 'R'], [
#       'R', 'R', 'Y', 'R'], ['R', 'R', 'Y', 'R']], 'Y'))



def ai_move(board, coin):
    dict = {}
    if board:
        """
        Find column
        """
        for index, value in enumerate(board[0]):
            """
            Make sure using the initial board instead of the updated one.
            """
            newBoard = copy.deepcopy(board)
            tempBoard = add_coin(newBoard, coin, index)
            score = heuristic(tempBoard, coin)
            if score not in dict:
                dict[score] = tempBoard
    print(dict)
    return dict[max(dict.keys())]



#ai_move([[0,0,0,0,0],[0,0,0,0,0],['R',0,0,0,0],['Y','R',0,'R','Y']], 'Y')
#print(ai_move([[0,0,0,0,0],['Y',0,0,0,0],['R',0,0,0,'Y'],['Y','R',0,'R','Y']], 'Y'))
#print(ai_move([[0,0,0,0]], 'Y'))

def moves_exist(board) :
    """
    A move can still be made if any blank space exists on the top row
    """
    if 0 in board[0] :
        return True
    return False
def nice_print(board) :
    """
    Formats the board for nicer display
    """
    for line in board :
        print(*line)
def play_game(rows, cols) :
    """
    Plays a game with a human player against your AI
    """
    # Instantiate an empty board
    board = [([0]*cols) for i in range(rows)]
    # Continue playing as long as a legal move can still be made
    while(moves_exist(board)) :
        # AI plays first with the red tokens
        board = ai_move(board, 'R')
        nice_print(board)
        # Check if the AI Player has won the game
        if (is_winner(board, 'R')) :
            print('AI Wins!')
            break
        # Player moves next with the yellow tokens
        player_move = input('Enter your move: ')
        board = add_coin(board, 'Y', int(player_move))
        if (is_winner(board, 'Y')) :
            print('You win!')
            break

play_game(5, 7)

#print(ai_move([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]],"Y"))
#print(heuristic([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 'Y', 0, 0, 0, 0, 0]], "Y"))