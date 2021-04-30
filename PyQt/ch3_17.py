import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,500,500)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("icon.png"))
        btn = QPushButton("버튼1",self)
        btn.move(20,20)
        btn2 = QPushButton("버튼2",self)
        btn2.move(120,20)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()