import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 첫 번째 인자부터 윈도우가 출력되는 x축 위치, y축 위치, 윈도우의 너비, 윈도우의 높이
        self.setGeometry(100, 200, 300, 400)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()