import threading
import tkinter as tk
import tkinter.messagebox as msgbox
from .display import Display


# TkinterGUI显示平台
class TkinterDisplay(Display):
    def __init__(self, game, show_interval=0.001):
        super(TkinterDisplay, self).__init__(game, show_interval)

        self.width = 600
        self.height = 600
        self.margin = 30
        self.cell = (self.width - self.margin * 2) / self.game.board.width
        self.piece_cell = self.cell * 0.8
        self._draw_board()
        self.auto = False
        self.active_piece = None
        self.active_piece_pre_left = 0
        self.active_piece_pre_top = 0

    # 落子
    def put_piece(self, player, location, done):
        super(TkinterDisplay, self).put_piece(player, location, done)

        x, y = location
        self._draw_piece(player, x, y)
        self._redraw_active_location(x, y)

    def mainloop(self):
        self.window.mainloop()
        self.exit = True

    # 画棋谱
    def _draw_board(self):
        self.window = tk.Tk()
        self.window.title("五子棋")

        self.btn_text = tk.StringVar()
        self.btn_text.set("开始")
        self.btn_start = tk.Button(self.window, textvariable=self.btn_text, width=12, height=3, command=self._auto_play)
        self.btn_start.pack()

        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height)
        for i in range(self.game.board.width):
            self.canvas.create_line(self.margin + i * self.cell, self.margin, self.margin + i * self.cell, self.margin + (self.game.board.height - 1) * self.cell)
        for j in range(self.game.board.height):
            self.canvas.create_line(self.margin, self.margin + j * self.cell, self.margin + (self.game.board.width - 1) * self.cell, self.margin + j * self.cell)
        self.canvas.pack()

    def _auto_play(self):
        self.auto = not self.auto
        if self.auto:
            self.btn_text.set("暂停")
            threading.Timer(self.show_interval, self._play).start()
        else:
            self.btn_text.set("继续")

    def _play(self):
        if not self.exit:
            if self.auto:
                if not self.game.play():
                    self.step += 1
                    threading.Timer(self.show_interval, self._play).start()
                else:
                    self.show_game_over()

    # 画棋子
    def _draw_piece(self, player, x, y):
        color = 'darkGray'
        if player.index < player.other_index:
            color = 'black'
        left = self.margin + x * self.cell - self.piece_cell / 2
        top = self.margin + y * self.cell - self.piece_cell / 2
        self.canvas.create_oval(left, top, left + self.piece_cell, top + self.piece_cell, fill=color, outline=color)

    # 画最后落子的位置
    def _redraw_active_location(self, x, y):
        left = self.margin + x * self.cell - self.piece_cell / 2 - 2
        top = self.margin + y * self.cell - self.piece_cell / 2 - 2
        if self.active_piece is None:
            self.active_piece = self.canvas.create_oval(left, top, left + self.piece_cell + 4, top + self.piece_cell + 4)
        else:
            move_x = left - self.active_piece_pre_left
            move_y = top - self.active_piece_pre_top
            self.canvas.move(self.active_piece, move_x, move_y)
        self.active_piece_pre_left = left
        self.active_piece_pre_top = top

    # 弹出游戏结束对话框
    def show_game_over(self):
        self.auto = False
        self.btn_start['state'] = 'disabled'
        if self.win_player is not None:
            msgbox.showinfo("游戏结束", str(self.win_player) + " 赢了！共走步数：" + str(self.step))
        else:
            msgbox.showinfo("游戏结束", "平局！共走步数：" + str(self.step))

    # 通过画布坐标转换成落子位置
    def parse_location(self, left, top):
        x = int(round((left - self.margin) / self.cell))
        y = int(round((top - self.margin) / self.cell))
        if self.game.board.validate((x, y)):
            return x, y
        return None
