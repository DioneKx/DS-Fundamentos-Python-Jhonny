from PyQt5 import uic, QtWidgets

import mysql.connector
from reportlab.pdfgen import canvas

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "bd_schedule",
)

def pdfGenerator():
    cursor = db.cursor()
    db_data = "SELECT * FROM tbl_schedules"
    cursor.execute(db_data)
    listed = cursor.fetchall()
    
    y = 0
    pdf = canvas.Canvas("lista_contatos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "lista de Contatos")
    
    pdf.setFont("Times-Bold", 12)
    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "NOME")
    pdf.drawString(210, 750, "EMAIL")
    pdf.drawString(350, 750, "EMAIL")
    pdf.drawString(450, 750, "TIPO DE CONTATO")

    for i in range(0, len(listed)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(listed[i] [0]))
        pdf.drawString(110, 750 - y, str(listed[i] [1]))
        pdf.drawString(210, 750 - y, str(listed[i] [2]))
        pdf.drawString(350, 750 - y, str(listed[i] [3]))
        pdf.drawString(450, 750 - y, str(listed[i] [4]))
        
    pdf.save()
    print("PDF gerado com sucesso!")

def deleteContact():
    lineContact = agenda.contactList.currentRow()
    agenda.contactList.removeRow(lineContact)
    
    cursor = db.cursor()
    db_data = "SELECT _id FROM tbl_schedules"
    cursor.execute(db_data)
    listed = cursor.fetchall()
    id = listed[lineContact][0]
    cursor.execute("DELETE FROM tbl_schedules WHERE _id =" + str(id))
    db.commit()
    
    print("Contato deletado.")

def listContact():
    cursor = db.cursor()
    db_data = "SELECT * FROM tbl_schedules"
    cursor.execute(db_data)
    listed = cursor.fetchall()
    
    agenda.contactList.setRowCount(len(listed))
    agenda.contactList.setColumnCount(5)
    
    for i in range (0, len(listed)):
        for f in range(0, 5):
            agenda.contactList.setItem(i, f, QtWidgets.QTableWidgetItem(str(listed[i][f])))


def registerContact():
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
    sql = "INSERT INTO tbl_schedules (_name, _email, _tel, _type) VALUES (%s, %s, %s, %s)"
    db_data = (str(name), str(email), str(tel), str(_type))
    cursor.execute(sql, db_data)
    db.commit()

app = QtWidgets.QApplication([])
agenda = uic.loadUi("agenda.ui")
agenda.btnRegister.clicked.connect(registerContact)
agenda.pdf_generator.clicked.connect(pdfGenerator)
agenda.delete_contact.clicked.connect(deleteContact)
agenda.tabs.tabBarClicked.connect(listContact)

listContact()
agenda.show()
app.exec()