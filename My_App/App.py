from PyQt5 import QtWidgets
from My_App.Ui import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)  # here we setup ui file

        self.msg = QMessageBox()
        self.y_win_count = 0
        self.x_win_count = 0
        self.temp = []
        self.main_board = [None, None, None,  # our board
                           None, None, None,
                           None, None, None]
        self.x_result_label_2.setText('-')
        self.x_result_label_3.setText('-')
        self.label_2.setText('X')
        self.pushButton.setText('')
        self.pushButton_2.setText('')
        self.pushButton_3.setText('')
        self.pushButton_4.setText('')
        self.pushButton_5.setText('')
        self.pushButton_6.setText('')
        self.pushButton_7.setText('')
        self.pushButton_8.setText('')
        self.pushButton_9.setText('')

        self.turn = 'X'  # x/o

        self.restart_button.clicked.connect(self.reset)

        self.pushButton.clicked.connect(lambda: self.game(self.pushButton, self.turn, 0))
        self.pushButton_2.clicked.connect(lambda: self.game(self.pushButton_2, self.turn, 1))
        self.pushButton_3.clicked.connect(lambda: self.game(self.pushButton_3, self.turn, 3))
        self.pushButton_4.clicked.connect(lambda: self.game(self.pushButton_4, self.turn, 4))
        self.pushButton_5.clicked.connect(lambda: self.game(self.pushButton_5, self.turn, 2))
        self.pushButton_6.clicked.connect(lambda: self.game(self.pushButton_6, self.turn, 5))
        self.pushButton_7.clicked.connect(lambda: self.game(self.pushButton_7, self.turn, 8))
        self.pushButton_8.clicked.connect(lambda: self.game(self.pushButton_8, self.turn, 7))
        self.pushButton_9.clicked.connect(lambda: self.game(self.pushButton_9, self.turn, 6))

    def game(self, push_button, turn, value):
        if self.check_availability(push_button, turn, value):
            if self.result() == 'win':
                if self.turn == 'X':
                    self.x_win_count += 1
                    self.x_result_label_2.setText(str(self.x_win_count))
                elif self.turn == 'O':
                    self.y_win_count += 1
                    self.x_result_label_3.setText(str(self.y_win_count))
                self.msg.setWindowTitle("Result's")
                self.msg.setText(f"{self.turn} Win's")
                self.msg.setIcon(QMessageBox.Information)
                self.msg.exec_()
                self.reset()
            elif self.result() == 'draw':
                self.msg.setWindowTitle("Result's")
                self.msg.setText('DRAW')
                self.msg.setIcon(QMessageBox.Information)
                self.msg.exec_()
                self.reset()
            else:
                self.label_2.setText(self.change_turn())  # change turn

    def check_availability(self, p_b, tur, val):
        if self.main_board[val] is None:
            self.main_board[val] = tur
            p_b.setText(tur)
            return True
        return False

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn == 'O':
            self.turn = 'X'
        return self.turn

    def result(self):
        self.temp = [self.turn, self.turn, self.turn]
        if self.check_row():
            return 'win'
        if self.check_column():
            return 'win'
        if self.check_diagonal():
            return 'win'
        if None not in self.main_board:
            return 'draw'

    def check_row(self):
        if self.temp == self.main_board[0:3] or self.temp == self.main_board[3:6] or self.temp == self.main_board[6:9]:
            return True

    def check_column(self):
        col_1 = [self.main_board[0], self.main_board[3], self.main_board[6]]
        col_2 = [self.main_board[1], self.main_board[4], self.main_board[7]]
        col_3 = [self.main_board[2], self.main_board[5], self.main_board[8]]
        if self.temp == col_1 or self.temp == col_2 or self.temp == col_3:
            return True

    def check_diagonal(self):
        dia_1 = [self.main_board[0], self.main_board[4], self.main_board[8]]
        dia_2 = [self.main_board[2], self.main_board[4], self.main_board[6]]
        if self.temp == dia_1 or self.temp == dia_2:
            return True

    def reset(self):
        self.turn = 'X'
        self.main_board = [None, None, None, None, None, None, None, None, None]
        self.label_2.setText('X')
        self.pushButton.setText('')
        self.pushButton_2.setText('')
        self.pushButton_3.setText('')
        self.pushButton_4.setText('')
        self.pushButton_5.setText('')
        self.pushButton_6.setText('')
        self.pushButton_7.setText('')
        self.pushButton_8.setText('')
        self.pushButton_9.setText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = MyMainWindow()
    win.show()
    app.exec_()
