# Tic Tac Toe Game

# Create Player's class with name and symbol
class Player:  
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

# Create Game's Class, handling board, moves and gameplay
class TicTacToe:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = 0  # Start with player1
        self.board = [" "] * 9 # 3x3 board
        self.scores = {player1.name: 0, player2.name: 0} # Track wins

    def print_board(self):
        # Display board and current score/names
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")
        print(f"{self.players[0].name} ({self.players[0].symbol}): {self.scores[self.players[0].name]}  |  "
              f"{self.players[1].name} ({self.players[1].symbol}): {self.scores[self.players[1].name]}")

    def make_move(self, input_str):
        # Proccess players' moves
        try:
            row, col = map(int, input_str.split()) # Convert input like 1 3 to row=1, col=3
            if not (1 <= row <= 3) or not (1 <= col <= 3):
                # Validate input range(1-3)
                raise ValueError("Number must between 1-3")
            
            # Convert to 0-based board index(0-8)
            position = (row - 1) * 3 + (col - 1)

            if self.board[position] != " ":
                # Check for empty spot if true return false
                print("Position already taken!")
                return False
            # Place the player's symbol 
            self.board[position] = self.players[self.current_player].symbol
            return True
        except (ValueError, IndexError):
            print("Invalid input! Use 'row col' (e.g., '1 3')")
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for winner
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return self.players[self.current_player] # Return winner
        return None # no winner yet 

    def is_board_full(self): # Check if board is full for tie
        return " " not in self.board

    def play_turn(self):
        # Handle player's turn
        player = self.players[self.current_player]
        print(f"\n{player.name}'s turn ({player.symbol})")
        while True:
            move = input("Enter row and column (1-3, e.g., '2 3') or 'quit': ")
            if move.lower() == 'quit':
                return False # Exit if input=quit
            if self.make_move(move):
                break # Valid move
        return True

    def play_game(self): # Main game loop
        while True:
            self.print_board()
            # Handle player's move 
            if not self.play_turn():
                print("Game ended!")
                break
            
            # Check for winner 
            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"\n{winner.name} wins!")
                self.scores[winner.name] += 1
                break
            
            # Check for tie
            if self.is_board_full():
                self.print_board()
                print("\nIt's a tie!")
                break

            self.current_player = 1 - self.current_player  # Switch players

        # Ask to play again
        if input("\nPlay again? (y/n): ").lower() == 'y':
            self.board = [" "] * 9 # Reset board 
            self.current_player = 0 # Player1 starts
            self.play_game()

# Start the game
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe Game!")
    player1 = Player(input("Player 1 name (X): "), "X")
    player2 = Player(input("Player 2 name (O): "), "O")
    game = TicTacToe(player1, player2)
    game.play_game()