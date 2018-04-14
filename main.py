
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PhoeEdit")








        self.show()


app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
