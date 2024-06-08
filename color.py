class Colors:
    """
        Định nghĩa các màu sắc được sử dụng cho các khối Tetris.
        Attributes:
            dark_gray (tuple): Mã màu RGB cho màu đen xám.
            green (tuple): Mã màu RGB cho màu xanh lá cây.
            red (tuple): Mã màu RGB cho màu đỏ.
            orange (tuple): Mã màu RGB cho màu cam.
            yellow (tuple): Mã màu RGB cho màu vàng.
            purple (tuple): Mã màu RGB cho màu tím.
            cyan (tuple) : Mã màu RGB cho màu lục lam
            blue (tuple): Mã màu RGB cho màu xanh dương.
            dark_blue (tuple): Mã màu RGB cho màu xanh đen.
        Method:
            get_cell_colors()
        """
    dark_gray = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    dark_blue = (44, 44, 127)
    @classmethod
    def get_cell_colors(cls):
        """
            Danh sách các màu sắc của các ô khối.
            Return:
                list: Danh sách các mã màu RGB của các ô khối.
                """
        return [cls.dark_gray,cls.green,cls.red,cls.orange,cls.yellow,cls.purple,cls.cyan,cls.blue]
