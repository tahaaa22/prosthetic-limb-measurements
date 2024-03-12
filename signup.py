import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class SignUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(587, 622)
        MainWindow.setStyleSheet("background-color: #1e1e2f;\n"
"border: 1.2px solid #ffffff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelbox = QtWidgets.QGroupBox(self.centralwidget)
        self.labelbox.setStyleSheet("border:none;")
        self.labelbox.setObjectName("labelbox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.labelbox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(88, 9, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.labelbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setToolTip("")
        self.label.setWhatsThis("")
        self.label.setStyleSheet("color: rgb(225, 225, 225);font-size:48pt;\n"
"border:None;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(118, 9, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.labelbox, 0, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.inputbox = QtWidgets.QGroupBox(self.centralwidget)
        self.inputbox.setStyleSheet("border:none;")
        self.inputbox.setObjectName("inputbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.inputbox)
        self.verticalLayout.setSpacing(34)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.inputbox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-size:15pt;\n"
"color:rgb(142, 142, 213);\n"
"border: None;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.username = QtWidgets.QLineEdit(self.inputbox)
        self.username.setStyleSheet("font-size:13pt; color:rgb(243,243,243);\n"
"border: 2px solid  white;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"")
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(63)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.inputbox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-size:15pt;\n"
"color:rgb(142, 142, 213);\n"
"Border: None;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.password = QtWidgets.QLineEdit(self.inputbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setStyleSheet("font-size:13pt; color:rgb(243,243,243);\n"
"border: 2px solid  white;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.password.setMaxLength(7)
        self.password.setObjectName("password")
        self.horizontalLayout.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(63)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.inputbox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size:15pt;\n"
"color:rgb(142, 142, 213);\n"
"Border: None;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.password_2 = QtWidgets.QLineEdit(self.inputbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_2.sizePolicy().hasHeightForWidth())
        self.password_2.setSizePolicy(sizePolicy)
        self.password_2.setStyleSheet("font-size:13pt; color:rgb(243,243,243);\n"
"border: 2px solid  white;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.password_2.setMaxLength(7)
        self.password_2.setObjectName("password_2")
        self.horizontalLayout_5.addWidget(self.password_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.inputbox)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-size:15pt;\n"
"color:rgb(142, 142, 213);\n"
"Border: None;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.radioButton = QtWidgets.QRadioButton(self.inputbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color:white;\n"
"border:none;")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.inputbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color:white;\n"
"border:none;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addWidget(self.inputbox, 2, 0, 2, 2)
        self.loginbox = QtWidgets.QGroupBox(self.centralwidget)
        self.loginbox.setStyleSheet("border:none;")
        self.loginbox.setObjectName("loginbox")
        self.gridLayout = QtWidgets.QGridLayout(self.loginbox)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem3 = QtWidgets.QSpacerItem(118, 9, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.loginbutton = QtWidgets.QPushButton(self.loginbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginbutton.sizePolicy().hasHeightForWidth())
        self.loginbutton.setSizePolicy(sizePolicy)
        self.loginbutton.setMaximumSize(QtCore.QSize(200, 52))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("color:rgb(142, 142, 213); \n"
"border: 1.2px solid  rgb(142, 142, 213);\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.loginbutton.setObjectName("loginbutton")
        self.gridLayout.addWidget(self.loginbutton, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(118, 14, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.loginbox, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SignUp"))
        self.label_3.setText(_translate("MainWindow", "UserName:"))
        self.label_2.setText(_translate("MainWindow", "Password:"))
        self.label_4.setText(_translate("MainWindow", "Confirm Password:"))
        self.label_5.setText(_translate("MainWindow", "Gender: "))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.loginbutton.setText(_translate("MainWindow", "SignUp"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SignUp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
