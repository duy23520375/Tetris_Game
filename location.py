class Position:
    """
       Lớp đại diện cho vị trí của một khối hoặc ô trong lưới.
       Attributes:
           row (int): Vị trí hàng.
           col (int): Vị trí cột.
       """
    def __init__(self,row,col):
        self.row = row
        self.col = col
