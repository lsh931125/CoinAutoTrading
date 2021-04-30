import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow): # QMainWindow 부모 클래스를 상속하는 MyWindow 자식 클래스
    def __init__(self): # 자식 클래스의 초기화자 __init__()
        # __init__() 은 자식 클래스인 MyWindow에도 있으므로
        # self.__init__()을 하게되면 자식의 __init__()을 호출하게 된다.
        # 따라서 부모 클래스에 정의된 __init__()을 호출하기위해
        # 부모 클래스를 찾아 리턴해주는 super()를 적은후 __init__()을 호출한 것이다.
        super().__init__()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
