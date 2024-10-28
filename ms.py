import random

def generateSquare(n):
    magicSquare = [[0] * n for _ in range(n)]
    i, j = 0, n // 2
    for num in range(1, n * n + 1):
        magicSquare[i][j] = num
        next_i, next_j = (i - 1) % n, (j + 1) % n
        if magicSquare[next_i][next_j]:
            next_i, next_j = (i + 1) % n, j
        i, j = next_i, next_j
    return magicSquare

def printMagicSquare(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol):
    print("Magic Square:")
    for row in magicSquare:
        print(' | '.join(
            f'{player_symbol}' if num in player_moves else
            f'{computer_symbol}' if num in computer_moves else
            f'{num}'
            for num in row
        ))
        print('-' * 9)
def transposeSquare(matrix):
    n = len(matrix)
    transpose = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            transpose[i][j] = matrix[j][i]
    
    return transpose
def reverseColumn(square):
    for row in square:
        row.reverse()  
    return square

def checkWin(magicSquare, moves):
    magic_constant = sum(magicSquare[0])
    return any(
        sum(magicSquare[i][j] for j in range(len(magicSquare)) if magicSquare[i][j] in moves) == magic_constant or
        sum(magicSquare[j][i] for j in range(len(magicSquare)) if magicSquare[j][i] in moves) == magic_constant
        for i in range(len(magicSquare))
    ) or sum(magicSquare[i][i] for i in range(len(magicSquare)) if magicSquare[i][i] in moves) == magic_constant or \
       sum(magicSquare[i][len(magicSquare) - 1 - i] for i in range(len(magicSquare)) if magicSquare[i][len(magicSquare) - 1 - i] in moves) == magic_constant

def findWinningMove(magicSquare, moves, available_numbers):
    for number in available_numbers:
        if checkWin(magicSquare, moves + [number]):
            return number
    return None

def toss():
    return random.choice([0, 1])

def getValidInput(prompt, valid_options):
    while True:
        choice = input(prompt)
        if choice == "-0":  
            print("Invalid input! '-0' is not allowed.")
            continue
        try:
            choice = int(choice)
            if choice not in valid_options:
                print(f"Invalid input! Choose from {valid_options}.")
                continue
            return choice  
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def playGame(magicSquare):
    available_numbers = [num for row in magicSquare for num in row]
    player_moves, computer_moves = [], []
    printMagicSquare(magicSquare, player_moves, computer_moves, " ", " ")

    human_choice = getValidInput('Select "0" or "1" for the toss: ', [0, 1])
    player_symbol, computer_symbol = ('X', 'O') if toss() == human_choice else ('O', 'X')
    current_player = player_symbol

    while True:
        if current_player == player_symbol:
            player_move = getValidInput("Select a number from the board: ", available_numbers)
            player_moves.append(player_move)
        else:
            move = (findWinningMove(magicSquare, computer_moves, available_numbers) or
                    findWinningMove(magicSquare, player_moves, available_numbers) or
                    random.choice(available_numbers))
            print(f"Computer's choice: {move}")
            computer_moves.append(move)

        available_numbers.remove(player_moves[-1] if current_player == player_symbol else move)
        printMagicSquare(magicSquare, player_moves, computer_moves, player_symbol, computer_symbol)

        if checkWin(magicSquare, computer_moves):
            print("Computer wins!")
            return
        elif checkWin(magicSquare, player_moves):
            print("Player wins!")
            return
        if not available_numbers:
            print("It's a draw!")
            return
        
        current_player = player_symbol if current_player == computer_symbol else computer_symbol

def main():
    while True:
        magicSquare = generateSquare(3)
        transpose = transposeSquare(magicSquare)
        reverse= reverseColumn(transpose)
        playGame(reverse)
        while True:
            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no','YES','NO']:
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")
        
        if play_again == 'no':
            print("Thanks for playing!")
            break

main()