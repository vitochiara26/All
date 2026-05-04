from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        if not self.moves:
            return self.position

        move = random.choice(self.moves)

        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        self.position = (new_x, new_y)
    
        self.path.append(self.position)

        return self.position
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    def level_up(self):
        diagonal_moves = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        for move in diagonal_moves:
            if not move in self.moves:
                self.moves.append(move)
