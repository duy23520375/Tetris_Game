from block import Block
from location import Position
class LBlock(Block):
    def __init__(self):
        """
            Lớp đại diện cho khối hình chữ L trong Tetris.
            """
        super().__init__(id = 1)
        self.cells = {
            0: [Position(0,2),Position(1,0),Position(1,1),Position(1,2)],
            1: [Position(0,1),Position(1,1),Position(2,1),Position(2,2)],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,0)],
            3: [Position(0,0),Position(0,1),Position(1,1),Position(2,1)]
        }
class JBlock(Block):
    def __init__(self):
        """
            Lớp đại diện cho khối hình chữ J trong Tetris.
            """
        super().__init__(id = 2)
        self.cells = {
            0: [Position(0,0),Position(1,0),Position(1,1),Position(1,2)],
            1: [Position(0,1),Position(0,2),Position(1,1),Position(2,1)],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,2)],
            3: [Position(0,1),Position(1,1),Position(2,0),Position(2,1)]
        }
class IBlock(Block):
    """
        Lớp đại diện cho khối hình chữ I trong Tetris.
        """
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(1,0),Position(1,1),Position(1,2),Position(1,3)],
            1: [Position(0,2),Position(1,2),Position(2,2),Position(3,2)],
            2: [Position(2,0),Position(2,1),Position(2,2),Position(2,3)],
            3: [Position(0,1),Position(1,1),Position(2,1),Position(3,1)]
        }
class OBlock(Block):
    """
        Lớp đại diện cho khối hình chữ O trong Tetris.
        """
    def __init__(self):
        super().__init__(id = 3)
        self.cells = {
            0: [Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            1: [Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            2: [Position(0,0),Position(0,1),Position(1,0),Position(1,1)],
            3: [Position(0,0),Position(0,1),Position(1,0),Position(1,1)]
        }
class SBlock(Block):
    """
        Lớp đại diện cho khối hình chữ S trong Tetris.
        """
    def __init__(self):
        super().__init__(id = 4)
        self.cells = {
            0: [Position(0,1),Position(0,2),Position(1,0),Position(1,1)],
            1: [Position(0,1),Position(1,1),Position(1,2),Position(2,2)],
            2: [Position(1,1),Position(1,2),Position(2,0),Position(2,1)],
            3: [Position(0,0),Position(1,0),Position(1,1),Position(2,1)]
        }
class TBlock(Block):
    """
        Lớp đại diện cho khối hình chữ T trong Tetris.
        """
    def __init__(self):
        super().__init__(id = 5)
        self.cells = {
            0: [Position(0,1),Position(1,0),Position(1,1),Position(1,2)],
            1: [Position(0,1),Position(1,1),Position(1,2),Position(2,1)],
            2: [Position(1,0),Position(1,1),Position(1,2),Position(2,1)],
            3: [Position(0,1),Position(1,0),Position(1,1),Position(2,1)]
        }
class ZBlock(Block):
    """
        Lớp đại diện cho khối hình chữ Z trong Tetris.
        """
    def __init__(self):
        super().__init__(id = 6)
        self.cells = {
            0: [Position(0,0),Position(0,1),Position(1,1),Position(1,2)],
            1: [Position(0,2),Position(1,1),Position(1,2),Position(2,1)],
            2: [Position(1,0),Position(1,1),Position(2,1),Position(2,2)],
            3: [Position(0,1),Position(1,0),Position(1,1),Position(2,0)]
        }
