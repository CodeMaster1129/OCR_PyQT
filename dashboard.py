# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dashboard(object):
    def setupUi(self, dashboard):
        dashboard.setObjectName("dashboard")
        dashboard.resize(1516, 878)
        font = QtGui.QFont()
        font.setPointSize(12)
        dashboard.setFont(font)
        self.centralwidget = QtWidgets.QWidget(dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.upload_btn = QtWidgets.QPushButton(self.centralwidget)
        self.upload_btn.setGeometry(QtCore.QRect(650, 70, 361, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_btn.sizePolicy().hasHeightForWidth())
        self.upload_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.upload_btn.setFont(font)
        self.upload_btn.setObjectName("upload_btn")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(148, 203, 601, 651))
        self.graphicsView.setObjectName("graphicsView")
        self.rotate_left_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rotate_left_btn.setGeometry(QtCore.QRect(660, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rotate_left_btn.setFont(font)
        self.rotate_left_btn.setObjectName("rotate_left_btn")
        self.rotate_right_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rotate_right_btn.setGeometry(QtCore.QRect(560, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rotate_right_btn.setFont(font)
        self.rotate_right_btn.setObjectName("rotate_right_btn")
        self.zoom_in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in_btn.setGeometry(QtCore.QRect(150, 162, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zoom_in_btn.setFont(font)
        self.zoom_in_btn.setObjectName("zoom_in_btn")
        self.zoom_out_btn = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out_btn.setGeometry(QtCore.QRect(240, 162, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.zoom_out_btn.setFont(font)
        self.zoom_out_btn.setObjectName("zoom_out_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 20, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(31, 171, 46, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 70, 211, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 70, 171, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1060, 160, 159, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 88, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 450, 78, 19))
        self.label_6.setObjectName("label_6")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 620, 60, 19))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 770, 75, 19))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(772, 210, 78, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(772, 260, 100, 19))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(772, 310, 70, 19))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(772, 360, 32, 19))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(772, 410, 51, 19))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(830, 470, 36, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.doc_number = QtWidgets.QLineEdit(self.centralwidget)
        self.doc_number.setGeometry(QtCore.QRect(992, 260, 491, 25))
        self.doc_number.setObjectName("doc_number")
        self.bp_name = QtWidgets.QLineEdit(self.centralwidget)
        self.bp_name.setGeometry(QtCore.QRect(990, 310, 491, 25))
        self.bp_name.setObjectName("bp_name")
        self.date = QtWidgets.QLineEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(990, 360, 491, 25))
        self.date.setObjectName("date")
        self.terms = QtWidgets.QLineEdit(self.centralwidget)
        self.terms.setGeometry(QtCore.QRect(990, 410, 491, 25))
        self.terms.setObjectName("terms")
        self.description = QtWidgets.QLineEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(933, 510, 451, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.description.setFont(font)
        self.description.setObjectName("description")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1050, 470, 177, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1366, 470, 101, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.amount = QtWidgets.QLineEdit(self.centralwidget)
        self.amount.setGeometry(QtCore.QRect(1396, 510, 81, 25))
        self.amount.setObjectName("amount")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(772, 560, 141, 19))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(772, 610, 141, 19))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(772, 660, 141, 19))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(772, 710, 121, 19))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(772, 760, 131, 19))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(772, 810, 141, 19))
        self.label_25.setObjectName("label_25")
        self.round_off = QtWidgets.QLineEdit(self.centralwidget)
        self.round_off.setGeometry(QtCore.QRect(1396, 660, 81, 25))
        self.round_off.setObjectName("round_off")
        self.gst = QtWidgets.QLineEdit(self.centralwidget)
        self.gst.setGeometry(QtCore.QRect(1396, 710, 81, 25))
        self.gst.setObjectName("gst")
        self.vat = QtWidgets.QLineEdit(self.centralwidget)
        self.vat.setGeometry(QtCore.QRect(1396, 760, 81, 25))
        self.vat.setObjectName("vat")
        self.net_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.net_amount.setGeometry(QtCore.QRect(1396, 810, 81, 25))
        self.net_amount.setObjectName("net_amount")
        self.discount = QtWidgets.QLineEdit(self.centralwidget)
        self.discount.setGeometry(QtCore.QRect(1396, 610, 81, 25))
        self.discount.setObjectName("discount")
        self.total = QtWidgets.QLineEdit(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(1396, 560, 81, 25))
        self.total.setObjectName("total")
        self.doc_type = QtWidgets.QComboBox(self.centralwidget)
        self.doc_type.setGeometry(QtCore.QRect(992, 210, 491, 25))
        self.doc_type.setObjectName("doc_type")
        self.doc_type.addItem("")
        self.doc_type.addItem("")
        self.doc_type.addItem("")
        self.doc_type.addItem("")
        self.doc_type.addItem("")
        self.doc_type.addItem("")
        self.code = QtWidgets.QComboBox(self.centralwidget)
        self.code.setGeometry(QtCore.QRect(772, 510, 151, 25))
        self.code.setObjectName("code")
        self.code.addItem("")
        self.code.addItem("")
        self.code.addItem("")
        self.code.addItem("")
        self.code.addItem("")
        self.code.addItem("")
        self.code.addItem("")
        self.code.addItem("")
        self.code.addItem("")
        self.code.addItem("")
        self.file_name = QtWidgets.QLabel(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(140, 120, 558, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_name.sizePolicy().hasHeightForWidth())
        self.file_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.file_name.setFont(font)
        self.file_name.setAlignment(QtCore.Qt.AlignCenter)
        self.file_name.setObjectName("file_name")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(800, 130, 649, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(1190, 70, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAutoFillBackground(False)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        dashboard.setCentralWidget(self.centralwidget)

        self.retranslateUi(dashboard)
        QtCore.QMetaObject.connectSlotsByName(dashboard)

    def retranslateUi(self, dashboard):
        _translate = QtCore.QCoreApplication.translate
        dashboard.setWindowTitle(_translate("dashboard", "Dashboard"))
        self.upload_btn.setText(_translate("dashboard", "Upload"))
        self.rotate_left_btn.setText(_translate("dashboard", "Rotate Left"))
        self.rotate_right_btn.setText(_translate("dashboard", "Rotate Right"))
        self.zoom_in_btn.setText(_translate("dashboard", "Zoom In"))
        self.zoom_out_btn.setText(_translate("dashboard", "Zoom Out"))
        self.label.setText(_translate("dashboard", "HOME PAGE"))
        self.label_2.setText(_translate("dashboard", "TODO"))
        self.label_7.setText(_translate("dashboard", "Company Name"))
        self.label_8.setText(_translate("dashboard", "Company Logo"))
        self.label_9.setText(_translate("dashboard", "Document Details"))
        self.label_5.setText(_translate("dashboard", "PROCESSED"))
        self.label_6.setText(_translate("dashboard", "ARCHIVED"))
        self.label_10.setText(_translate("dashboard", "REPORT"))
        self.label_11.setText(_translate("dashboard", "SETTINGS"))
        self.label_12.setText(_translate("dashboard", "Doc. Type:"))
        self.label_13.setText(_translate("dashboard", "Doc. Number:"))
        self.label_14.setText(_translate("dashboard", "BP Name:"))
        self.label_15.setText(_translate("dashboard", "Date"))
        self.label_16.setText(_translate("dashboard", "Terms:"))
        self.label_17.setText(_translate("dashboard", "Code"))
        self.doc_number.setText(_translate("dashboard", "20623"))
        self.bp_name.setText(_translate("dashboard", "SECONDS LOCKS REPAIR"))
        self.date.setText(_translate("dashboard", "JULY 07, 2024"))
        self.terms.setText(_translate("dashboard", "CASH"))
        self.description.setText(_translate("dashboard", "Fossil_fossil_Battery_replacement_one year warranty"))
        self.label_18.setText(_translate("dashboard", "Description / QTY / Price"))
        self.label_19.setText(_translate("dashboard", "Amount"))
        self.amount.setText(_translate("dashboard", "84.00"))
        self.label_20.setText(_translate("dashboard", "Total"))
        self.label_21.setText(_translate("dashboard", "Discout:"))
        self.label_22.setText(_translate("dashboard", "Round-Off:"))
        self.label_23.setText(_translate("dashboard", "GST:"))
        self.label_24.setText(_translate("dashboard", "VAT:"))
        self.label_25.setText(_translate("dashboard", "Net Amount"))
        self.round_off.setText(_translate("dashboard", "84.00"))
        self.gst.setText(_translate("dashboard", "84.00"))
        self.vat.setText(_translate("dashboard", "84.00"))
        self.net_amount.setText(_translate("dashboard", "84.00"))
        self.discount.setText(_translate("dashboard", "84.00"))
        self.total.setText(_translate("dashboard", "84.00"))
        self.doc_type.setItemText(0, _translate("dashboard", "Sales Invoice"))
        self.doc_type.setItemText(1, _translate("dashboard", "Sales Credit Note"))
        self.doc_type.setItemText(2, _translate("dashboard", "Purchase Invoice"))
        self.doc_type.setItemText(3, _translate("dashboard", "Purchase Debit Note"))
        self.doc_type.setItemText(4, _translate("dashboard", "Customer Receipt"))
        self.doc_type.setItemText(5, _translate("dashboard", "Vendor Payment"))
        self.code.setItemText(0, _translate("dashboard", "40110"))
        self.code.setItemText(1, _translate("dashboard", "40115"))
        self.code.setItemText(2, _translate("dashboard", "50110"))
        self.code.setItemText(3, _translate("dashboard", "50115"))
        self.code.setItemText(4, _translate("dashboard", "61000"))
        self.code.setItemText(5, _translate("dashboard", "61200"))
        self.code.setItemText(6, _translate("dashboard", "61300"))
        self.code.setItemText(7, _translate("dashboard", "61400"))
        self.code.setItemText(8, _translate("dashboard", "61500"))
        self.code.setItemText(9, _translate("dashboard", "61600"))
        self.file_name.setText(_translate("dashboard", "FILE(Uploaded)-Name"))
        self.label_4.setText(_translate("dashboard", "Published"))
        self.lineEdit_9.setText(_translate("dashboard", "SEARCH BAR(BP Name)"))
