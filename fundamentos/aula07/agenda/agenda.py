from PyQt5 import uic, QtWidgets

import mysql.connector
from reportlab.pdfgen import canvas

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bd_schedule",
)

def registerContact():
    _id = agenda.id_contact.text()
    name = agenda.name_contact.text()
    email = agenda.email_contact.text()
    tel = agenda.tel_contact.text()
    
    if agenda.residencial_type.isChecked():
        _type = agenda.residencial_type.text()
    elif agenda.celular_type.isChecked():
        _type = agenda.celular_type.text()
    else:
        _type = "Não Informado"
    
    cursor = db.cursor()
    sql = "INSERT INTO tbl_schedules (_id, _name, _email, _tel, _type) VALUES (%s, %s, %s, %s, %s)"
    db_data = (int(_id), str(name), str(email), str(tel), str(_type))
    cursor.execute(sql, db_data)
    db.commit()

app = QtWidgets.QApplication([])
agenda = uic.loadUi("agenda.ui")
agenda.btnRegister.clicked.connect(registerContact)

agenda.show()
app.exec()