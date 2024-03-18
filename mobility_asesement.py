import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class assesement(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 831)
        MainWindow.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #1e1e2f;\n"
"border:none;\n"
"color:#ffffff;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.titlebox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titlebox.sizePolicy().hasHeightForWidth())
        self.titlebox.setSizePolicy(sizePolicy)
        self.titlebox.setObjectName("titlebox")
        self.title = QtWidgets.QHBoxLayout(self.titlebox)
        self.title.setObjectName("title")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.title.addItem(spacerItem)
        self.Title = QtWidgets.QLabel(self.titlebox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        self.Title.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("border:none;")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.title.addWidget(self.Title)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.title.addItem(spacerItem1)
        self.verticalLayout_11.addWidget(self.titlebox)
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setObjectName("groupbox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupbox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.regionsBox = QtWidgets.QGroupBox(self.groupbox)
        self.regionsBox.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.regionsBox.setObjectName("regionsBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.regionsBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.regionsBox)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border:none;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton = QtWidgets.QRadioButton(self.regionsBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.regionsBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.regionsBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_10.addWidget(self.regionsBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 198, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem2)
        self.FlexionBox = QtWidgets.QGroupBox(self.groupbox)
        self.FlexionBox.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.FlexionBox.setObjectName("FlexionBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.FlexionBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.measurments_1 = QtWidgets.QGroupBox(self.FlexionBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurments_1.sizePolicy().hasHeightForWidth())
        self.measurments_1.setSizePolicy(sizePolicy)
        self.measurments_1.setObjectName("measurments_1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.measurments_1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.flexion_deg = QtWidgets.QLCDNumber(self.measurments_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flexion_deg.sizePolicy().hasHeightForWidth())
        self.flexion_deg.setSizePolicy(sizePolicy)
        self.flexion_deg.setMaximumSize(QtCore.QSize(16777215, 40))
        self.flexion_deg.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.flexion_deg.setObjectName("flexion_deg")
        self.horizontalLayout_2.addWidget(self.flexion_deg)
        self.flex_deg_label = QtWidgets.QLabel(self.measurments_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flex_deg_label.sizePolicy().hasHeightForWidth())
        self.flex_deg_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flex_deg_label.setFont(font)
        self.flex_deg_label.setObjectName("flex_deg_label")
        self.horizontalLayout_2.addWidget(self.flex_deg_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.flexion_per = QtWidgets.QLCDNumber(self.measurments_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flexion_per.sizePolicy().hasHeightForWidth())
        self.flexion_per.setSizePolicy(sizePolicy)
        self.flexion_per.setMaximumSize(QtCore.QSize(16777215, 40))
        self.flexion_per.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.flexion_per.setObjectName("flexion_per")
        self.horizontalLayout_3.addWidget(self.flexion_per)
        self.flex_per_label = QtWidgets.QLabel(self.measurments_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flex_per_label.sizePolicy().hasHeightForWidth())
        self.flex_per_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flex_per_label.setFont(font)
        self.flex_per_label.setObjectName("flex_per_label")
        self.horizontalLayout_3.addWidget(self.flex_per_label)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.Status_1 = QtWidgets.QLabel(self.measurments_1)
        self.Status_1.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"font: 75 10pt \"MS Shell Dlg 2\" ;\n"
"")
        self.Status_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Status_1.setObjectName("Status_1")
        self.verticalLayout_5.addWidget(self.Status_1)
        self.horizontalLayout_8.addWidget(self.measurments_1)
        self.Flexion_image = QtWidgets.QLabel(self.FlexionBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Flexion_image.sizePolicy().hasHeightForWidth())
        self.Flexion_image.setSizePolicy(sizePolicy)
        self.Flexion_image.setText("")
        self.Flexion_image.setPixmap(QtGui.QPixmap("flexion.PNG"))
        self.Flexion_image.setScaledContents(True)
        self.Flexion_image.setObjectName("Flexion_image")
        self.horizontalLayout_8.addWidget(self.Flexion_image)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_10.addWidget(self.FlexionBox)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.abductionBox = QtWidgets.QGroupBox(self.groupbox)
        self.abductionBox.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.abductionBox.setObjectName("abductionBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.abductionBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.measurments_2 = QtWidgets.QGroupBox(self.abductionBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurments_2.sizePolicy().hasHeightForWidth())
        self.measurments_2.setSizePolicy(sizePolicy)
        self.measurments_2.setObjectName("measurments_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.measurments_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.flexion_deg_2 = QtWidgets.QLCDNumber(self.measurments_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flexion_deg_2.sizePolicy().hasHeightForWidth())
        self.flexion_deg_2.setSizePolicy(sizePolicy)
        self.flexion_deg_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.flexion_deg_2.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.flexion_deg_2.setObjectName("flexion_deg_2")
        self.horizontalLayout_10.addWidget(self.flexion_deg_2)
        self.flex_deg_label_2 = QtWidgets.QLabel(self.measurments_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flex_deg_label_2.sizePolicy().hasHeightForWidth())
        self.flex_deg_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flex_deg_label_2.setFont(font)
        self.flex_deg_label_2.setObjectName("flex_deg_label_2")
        self.horizontalLayout_10.addWidget(self.flex_deg_label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.flexion_per_2 = QtWidgets.QLCDNumber(self.measurments_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flexion_per_2.sizePolicy().hasHeightForWidth())
        self.flexion_per_2.setSizePolicy(sizePolicy)
        self.flexion_per_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.flexion_per_2.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.flexion_per_2.setObjectName("flexion_per_2")
        self.horizontalLayout_11.addWidget(self.flexion_per_2)
        self.flex_per_label_2 = QtWidgets.QLabel(self.measurments_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flex_per_label_2.sizePolicy().hasHeightForWidth())
        self.flex_per_label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flex_per_label_2.setFont(font)
        self.flex_per_label_2.setObjectName("flex_per_label_2")
        self.horizontalLayout_11.addWidget(self.flex_per_label_2)
        spacerItem4 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.Status_2 = QtWidgets.QLabel(self.measurments_2)
        self.Status_2.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"font: 75 10pt \"MS Shell Dlg 2\" ;\n"
"")
        self.Status_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Status_2.setObjectName("Status_2")
        self.verticalLayout_6.addWidget(self.Status_2)
        self.horizontalLayout_9.addWidget(self.measurments_2)
        self.Flexion_image_2 = QtWidgets.QLabel(self.abductionBox)
        self.Flexion_image_2.setText("")
        self.Flexion_image_2.setPixmap(QtGui.QPixmap("abduction.PNG"))
        self.Flexion_image_2.setScaledContents(True)
        self.Flexion_image_2.setObjectName("Flexion_image_2")
        self.horizontalLayout_9.addWidget(self.Flexion_image_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.abductionBox)
        self.extensionBox_3 = QtWidgets.QGroupBox(self.groupbox)
        self.extensionBox_3.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.extensionBox_3.setObjectName("extensionBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.extensionBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.measurments_3 = QtWidgets.QGroupBox(self.extensionBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurments_3.sizePolicy().hasHeightForWidth())
        self.measurments_3.setSizePolicy(sizePolicy)
        self.measurments_3.setObjectName("measurments_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.measurments_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.flexion_deg_3 = QtWidgets.QLCDNumber(self.measurments_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flexion_deg_3.sizePolicy().hasHeightForWidth())
        self.flexion_deg_3.setSizePolicy(sizePolicy)
        self.flexion_deg_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.flexion_deg_3.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.flexion_deg_3.setObjectName("flexion_deg_3")
        self.horizontalLayout_13.addWidget(self.flexion_deg_3)
        self.flex_deg_label_3 = QtWidgets.QLabel(self.measurments_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flex_deg_label_3.sizePolicy().hasHeightForWidth())
        self.flex_deg_label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flex_deg_label_3.setFont(font)
        self.flex_deg_label_3.setObjectName("flex_deg_label_3")
        self.horizontalLayout_13.addWidget(self.flex_deg_label_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.flexion_per_3 = QtWidgets.QLCDNumber(self.measurments_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flexion_per_3.sizePolicy().hasHeightForWidth())
        self.flexion_per_3.setSizePolicy(sizePolicy)
        self.flexion_per_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.flexion_per_3.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.flexion_per_3.setObjectName("flexion_per_3")
        self.horizontalLayout_14.addWidget(self.flexion_per_3)
        self.flex_per_label_3 = QtWidgets.QLabel(self.measurments_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flex_per_label_3.sizePolicy().hasHeightForWidth())
        self.flex_per_label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.flex_per_label_3.setFont(font)
        self.flex_per_label_3.setObjectName("flex_per_label_3")
        self.horizontalLayout_14.addWidget(self.flex_per_label_3)
        spacerItem5 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.Status_3 = QtWidgets.QLabel(self.measurments_3)
        self.Status_3.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;\n"
"font: 75 10pt \"MS Shell Dlg 2\" ;\n"
"")
        self.Status_3.setAlignment(QtCore.Qt.AlignCenter)
        self.Status_3.setObjectName("Status_3")
        self.verticalLayout_7.addWidget(self.Status_3)
        self.horizontalLayout_12.addWidget(self.measurments_3)
        self.Flexion_image_3 = QtWidgets.QLabel(self.extensionBox_3)
        self.Flexion_image_3.setText("")
        self.Flexion_image_3.setPixmap(QtGui.QPixmap("extension.PNG"))
        self.Flexion_image_3.setScaledContents(True)
        self.Flexion_image_3.setObjectName("Flexion_image_3")
        self.horizontalLayout_12.addWidget(self.Flexion_image_3)
        self.gridLayout_4.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.extensionBox_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_11.addWidget(self.groupbox)
        self.returnBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnBox.sizePolicy().hasHeightForWidth())
        self.returnBox.setSizePolicy(sizePolicy)
        self.returnBox.setObjectName("returnBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.returnBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(738, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.returnbutton = QtWidgets.QPushButton(self.returnBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnbutton.sizePolicy().hasHeightForWidth())
        self.returnbutton.setSizePolicy(sizePolicy)
        self.returnbutton.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.returnbutton.setFont(font)
        self.returnbutton.setStyleSheet("border: 1.2px solid #ffffff;\n"
"border-style: outset;\n"
"border-radius: 15px;")
        self.returnbutton.setObjectName("returnbutton")
        self.horizontalLayout.addWidget(self.returnbutton)
        self.verticalLayout_11.addWidget(self.returnBox)
        self.gridLayout.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Shoulder Mobility Assesement"))
        self.label.setText(_translate("MainWindow", "Choose Current Region: "))
        self.radioButton.setText(_translate("MainWindow", "Flexion"))
        self.radioButton_2.setText(_translate("MainWindow", "Abduction"))
        self.radioButton_3.setText(_translate("MainWindow", "Hyperextension"))
        self.flex_deg_label.setText(_translate("MainWindow", "Degrees"))
        self.flex_per_label.setText(_translate("MainWindow", "%"))
        self.Status_1.setText(_translate("MainWindow", "TextLabel"))
        self.flex_deg_label_2.setText(_translate("MainWindow", "Degrees"))
        self.flex_per_label_2.setText(_translate("MainWindow", "%"))
        self.Status_2.setText(_translate("MainWindow", "TextLabel"))
        self.flex_deg_label_3.setText(_translate("MainWindow", "Degrees"))
        self.flex_per_label_3.setText(_translate("MainWindow", "%"))
        self.Status_3.setText(_translate("MainWindow", "TextLabel"))
        self.returnbutton.setText(_translate("MainWindow", "Return"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = assesement()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())