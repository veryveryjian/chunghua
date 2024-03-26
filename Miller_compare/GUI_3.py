# PyQt5를 사용하는 경우
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])
ui = uic.loadUi("path/to/your_design.ui")
ui.show()
app.exec_()
