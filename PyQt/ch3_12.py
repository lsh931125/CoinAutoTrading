import sys
from PyQt5.QtWidgets import *

# 이벤트 루프를 생성하는 exec_() 메서드를 호출하기 위해 QApplication 객체 생성
app = QApplication(sys.argv)

label = QLabel("Hello")
label.show()

# 이벤트 루프 생성
app.exec_()