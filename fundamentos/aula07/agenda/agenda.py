from PyQt5 import uic, QtWidgets

def main():
    print("ETEC")

app = QtWidgets.QApplication([])
agenda = uic.loadUi("agenda.ui")
agenda.btnRegister.clicked.connect(main)

agenda.show()
app.exec()