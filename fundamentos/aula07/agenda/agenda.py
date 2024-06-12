from PyQt5 import uic, QtWidgets

import mysql.connector
from reportlab.pdfgen import canvas
import ctypes

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
    db_data = "SELECT a._id, a._name, a._email, a._tel, a._type FROM tbl_schedules AS a;"
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
        
    if len(str(name)) > 0 and len(str(email)) > 0 and len(str(tel)) > 0 and len(str(_type)) > 0:
        cursor = db.cursor()
        sql = "INSERT INTO tbl_schedules (_name, _email, _tel, _type) VALUES (%s, %s, %s, %s)"
        db_data = (str(name), str(email), str(tel), str(_type))
        cursor.execute(sql, db_data)
        db.commit()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Por favor, insira todos os dados...", "Dados inválidos", 0)

def edit_show():
    agenda_edit.show()

def editContact():
    _id = agenda_edit.id_contact_edit.text()
    name = agenda_edit.name_contact_edit.text()
    email = agenda_edit.email_contact_edit.text()
    tel = agenda_edit.tel_contact_edit.text()
    
    if agenda_edit.residencial_type_edit.isChecked():
        _type = agenda_edit.residencial_type_edit.text()
    elif agenda_edit.celular_type_edit.isChecked():
        _type = agenda_edit.celular_type_edit.text()
    else:
        _type = "Não Informado"
    
    if len(str(_id)) > 0 and len(str(name)) > 0 and len(str(email)) > 0 and len(str(tel)) > 0 and len(str(_type)) > 0:
        cursor = db.cursor()
        sql = "UPDATE tbl_schedules SET _name = %s, _email = %s, _tel = %s, _type = %s WHERE _id = %s"
        db_data = (str(name), str(email), str(tel), str(_type), str(_id))
        cursor.execute(sql, db_data)
        print(db_data)
        db.commit()
        listContact()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Por favor, insira todos os dados...", "Dados inválidos", 0)


app = QtWidgets.QApplication([])
agenda = uic.loadUi("agenda.ui")

agenda.btnRegister.clicked.connect(registerContact)
agenda.pdf_generator.clicked.connect(pdfGenerator)
agenda.delete_contact.clicked.connect(deleteContact)
agenda.alter_contact.clicked.connect(edit_show)
agenda.tabs.tabBarClicked.connect(listContact)

agenda_edit = uic.loadUi("agenda_edit.ui")
agenda_edit.btnEdit.clicked.connect(editContact)

listContact()
agenda.show()
app.exec()