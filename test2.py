import copy

def add_coin(board, coin, column) :
    """
    This function takes a list of lists representing the current state of board, the character reprensenting the current player's coin
    and an integer reprensenting the column in which the player is inserting their coin.
    Returns a list of lists reprensenting the new state of the board after the coin has been played.
    """
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

def is_winner(board, coin) :
    """
    This function takes a list of lists representing the current state of the board and the current player's coin.
    Returns True if the player using the coin coins has won the game in the current board position and False otherwise. 
    """
    for indexRow, row in enumerate(board):
        result = False 
        # To avoid array out of bound
        if indexRow < len(board) - 1 and result == False:
            for index, item in enumerate(row):               
                # To avoid array out of bound
                if index < len(row) - 1 and item == coin:
                    result = row[index] == row[index+1] == coin and board[indexRow+1][index] == board[indexRow+1][index+1] == coin
                    if result:
                        break
        if result:
            break
    return result

def heuristic(board, coin) :
    """
    This function takes a list of lists representing the current state of the board and the current player's coin.
    Returns the result of heuristic value.
    """
    result = 0
    for indexRow, row in enumerate(board):
        for index, item in enumerate(row):
            
            # To avoid array out of bound
            if index < len(row) - 1 and indexRow < len(board) - 1:
                array_temp = [row[index], row[index+1],
                              board[indexRow+1][index], board[indexRow+1][index+1]]
                numOfCoin = array_temp.count(coin)
                numOfEmpty = array_temp.count(0)
                if numOfCoin == 1 and numOfEmpty == 3:
                    result += 1
                elif numOfCoin == 2 and numOfEmpty == 2:
                    result += 10
                elif numOfCoin == 3 and numOfEmpty == 1:
                    result += 100
                elif numOfCoin == 4:
                    result += 1000
                else:
                    result += 0
    return result

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
    return dict[max(dict.keys())]

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

# is_winner([[0, "R", 0, 0, 0, 0, 0],
# [0, "R", "Y", 0, 0, 0, 0],
# [0, "R", "R", 0,0, 0, 0],
# [0, "Y", "Y", "Y", 0, "R", 0],
# [0, "R", "Y", "Y", 0, "R", 0]],"Y")
