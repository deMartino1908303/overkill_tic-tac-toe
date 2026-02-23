import math as m
from random import randint
from collections import deque
class TicTacToe():
    def __init__(self):
        self.board = [0]*9
        self.x_stack = deque()
        self.y_stack = deque()
    
    def print_board(self):
        for ii in [0, 3, 6]:
            print("", *self.board[ii: ii+3], sep="|", end="|\n")
        print("\n")
    
    def __ceck_win(self):
        for ii in [0, 3, 6]:
            if sum(self.board[ii:ii+3]) == 3:
                return True
            elif sum(self.board[ii:ii+3]) == -3:
                return True
        
        for ii in [0, 1, 2]:
            if sum(self.board[ii:ii+7:3]) == 3:
                return True
            elif sum(self.board[ii:ii+7:3]) == -3:
                return True
        
        if sum(self.board[0:9:4]) == 3 or sum(self.board[2:7:2]) == 3:
            return True

        if sum(self.board[0:9:4]) == -3 or sum(self.board[2:7:2]) == -3:
            return True
        
        return False
    
    def play_turn(self, move, player):
        
        self.board[move] = player

        if player == 1:
            self.x_stack.append(move)

            if len(self.x_stack) > 3 :
                reset = self.x_stack.popleft()
                self.board[reset] = 0

        elif player == 2:
            self.y_stack.append(move)

            if len(self.y_stack) > 3 :
                reset = self.y_stack.popleft()
                self.board[reset] = 0
        
        esito = self.__ceck_win()

        if esito:
            return True
        
        return False
        


if __name__ == "__main__":
    test = TicTacToe()
    test.play_turn(0, 1)
    test.play_turn(1, 1)
    test.play_turn(3, 1)
    test.play_turn(4, 1)
    test.play_turn(5, 1)

