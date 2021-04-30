import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,500)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("icon.png"))
        btn = QPushButton("버튼1",self)
        btn.move(20,20)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()