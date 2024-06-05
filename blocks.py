from block import Block
from location import Possition
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)
        self.cells = {
            0: [Possition(0,2),Possition(1,0),Possition(1,1),Possition(1,2)],
            1: [Possition(0,1),Possition(1,1),Possition(2,1),Possition(2,2)],
            2: [Possition(1,0),Possition(1,1),Possition(1,2),Possition(2,0)],
            3: [Possition(0,0),Possition(0,1),Possition(1,1),Possition(2,1)]
        }
class JBlock(Block):
    def __init__(self):
        super().__init__(id = 2)
        self.cells = {
            0: [Possition(0,0),Possition(1,0),Possition(1,1),Possition(1,2)],
            1: [Possition(0,1),Possition(0,2),Possition(1,1),Possition(2,1)],
            2: [Possition(1,0),Possition(1,1),Possition(1,2),Possition(2,2)],
            3: [Possition(0,1),Possition(1,1),Possition(2,0),Possition(2,1)]
        }
class IBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Possition(1,0),Possition(1,1),Possition(1,2),Possition(1,3)],
            1: [Possition(0,2),Possition(1,2),Possition(2,2),Possition(3,2)],
            2: [Possition(2,0),Possition(2,1),Possition(2,2),Possition(2,3)],
            3: [Possition(0,1),Possition(1,1),Possition(2,1),Possition(3,1)]
        }
class OBlock(Block):
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Possition(0,0),Possition(0,1),Possition(1,0),Possition(1,1)],
            1: [Possition(0,0),Possition(0,1),Possition(1,0),Possition(1,1)],
            2: [Possition(0,0),Possition(0,1),Possition(1,0),Possition(1,1)],
            3: [Possition(0,0),Possition(0,1),Possition(1,0),Possition(1,1)]
        }
class SBlock(Block):
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Possition(0,1),Possition(0,2),Possition(1,0),Possition(1,1)],
            1: [Possition(0,1),Possition(1,1),Possition(1,2),Possition(2,2)],
            2: [Possition(1,1),Possition(1,2),Possition(2,0),Possition(2,1)],
            3: [Possition(0,0),Possition(1,0),Possition(1,1),Possition(2,1)]
        }
class TBlock(Block):
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Possition(0,1),Possition(1,0),Possition(1,1),Possition(1,2)],
            1: [Possition(0,1),Possition(1,1),Possition(1,2),Possition(2,1)],
            2: [Possition(1,0),Possition(1,1),Possition(1,2),Possition(2,1)],
            3: [Possition(0,1),Possition(1,0),Possition(1,1),Possition(2,1)]
        }
class ZBlock(Block):
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Possition(0,0),Possition(0,1),Possition(1,1),Possition(1,2)],
            1: [Possition(0,2),Possition(1,1),Possition(1,2),Possition(2,1)],
            2: [Possition(1,0),Possition(1,1),Possition(2,1),Possition(2,2)],
            3: [Possition(0,1),Possition(1,0),Possition(1,1),Possition(2,0)]
        }