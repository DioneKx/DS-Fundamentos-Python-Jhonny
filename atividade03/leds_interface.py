from PyQt5 import uic, QtWidgets

import mysql.connector
import ctypes

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_leds",
)

def senbChoice():
    
    if leds.ledRed.isChecked():
        _choice = leds.ledRed.text()
    elif leds.ledGreen.isChecked():
        _choice = leds.ledGreen.text()
    elif leds.ledYellow.isChecked():
        _choice = leds.ledYellow.text()
    else:
        _choice = "Não Informado"
    
    cursor = db.cursor()
    sql = "INSERT INTO tbl_leds (_led) VALUES (%s);"
    db_data = [str(_choice)]
    cursor.execute(sql, db_data)
    db.commit()
    ctypes.windll.user32.MessageBoxW(0, "Led escolhido com sucesso!", "Isso ai!!!", 0)

app = QtWidgets.QApplication([])
leds = uic.loadUi("leds_interface.ui")
leds.sendBtn.clicked.connect(senbChoice)

leds.show()
app.exec()