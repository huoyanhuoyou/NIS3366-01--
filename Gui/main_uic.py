# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
from Gui import image_rc

class Ui_manage(object):
    def setupUi(self, manage):
        if not manage.objectName():
            manage.setObjectName(u"manage")
        manage.resize(916, 437)
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(14)
        manage.setFont(font)
        manage.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(manage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(manage)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 30))
        self.header.setMaximumSize(QSize(16777215, 30))
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.header.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header)
        self.header_left.setObjectName(u"header_left")
        self.header_left.setFrameShape(QFrame.StyledPanel)
        self.header_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.header_left)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.header_left)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 0))
        self.label.setMaximumSize(QSize(30, 16777215))
        self.label.setPixmap(QPixmap(u":/icon/images/icon/logo.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label)

        self.label_2 = QLabel(self.header_left)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setStyleStrategy(QFont.NoAntialias)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_left)

        self.header_right = QFrame(self.header)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setMinimumSize(QSize(120, 0))
        self.header_right.setMaximumSize(QSize(120, 16777215))
        self.header_right.setStyleSheet(u"")
        self.header_right.setFrameShape(QFrame.StyledPanel)
        self.header_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.min_btn = QPushButton(self.header_right)
        self.min_btn.setObjectName(u"min_btn")
        self.min_btn.setMinimumSize(QSize(0, 30))
        self.min_btn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/white/images/white/icon-line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.min_btn)

        self.max_btn = QPushButton(self.header_right)
        self.max_btn.setObjectName(u"max_btn")
        self.max_btn.setMinimumSize(QSize(0, 30))
        self.max_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/white/images/white/icon-max.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.max_btn.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.max_btn)

        self.close_btn = QPushButton(self.header_right)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/white/images/white/icon-close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.close_btn)


        self.horizontalLayout.addWidget(self.header_right)


        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(manage)
        self.body.setObjectName(u"body")
        self.body.setStyleSheet(u"")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.body.setLineWidth(0)
        self.horizontalLayout_8 = QHBoxLayout(self.body)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.body_left = QFrame(self.body)
        self.body_left.setObjectName(u"body_left")
        self.body_left.setMinimumSize(QSize(120, 0))
        self.body_left.setMaximumSize(QSize(120, 16777215))
        self.body_left.setStyleSheet(u"")
        self.body_left.setFrameShape(QFrame.StyledPanel)
        self.body_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.body_left)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 6, 5, 0)
        self.extend_btn = QPushButton(self.body_left)
        self.extend_btn.setObjectName(u"extend_btn")
        self.extend_btn.setMinimumSize(QSize(36, 36))
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setStyleStrategy(QFont.NoAntialias)
        self.extend_btn.setFont(font2)
        self.extend_btn.setStyleSheet(u"")
        self.extend_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.extend_btn)

        self.manage_btn = QPushButton(self.body_left)
        self.manage_btn.setObjectName(u"manage_btn")
        self.manage_btn.setMinimumSize(QSize(36, 36))
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.manage_btn.setFont(font3)
        self.manage_btn.setStyleSheet(u"")
        self.manage_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.manage_btn)

        self.setting_btn = QPushButton(self.body_left)
        self.setting_btn.setObjectName(u"setting_btn")
        self.setting_btn.setMinimumSize(QSize(36, 36))
        self.setting_btn.setFont(font3)
        self.setting_btn.setStyleSheet(u"")
        self.setting_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.setting_btn)

        self.about_btn = QPushButton(self.body_left)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setMinimumSize(QSize(36, 36))
        self.about_btn.setFont(font3)
        self.about_btn.setStyleSheet(u"")
        self.about_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_2.addWidget(self.about_btn)

        self.exit_btn = QPushButton(self.body_left)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(36, 36))
        self.exit_btn.setFont(font3)
        self.exit_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.exit_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 208, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.body_left)

        self.body_right = QFrame(self.body)
        self.body_right.setObjectName(u"body_right")
        self.body_right.setFrameShape(QFrame.StyledPanel)
        self.body_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.body_right)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.stacked_page = QStackedWidget(self.body_right)
        self.stacked_page.setObjectName(u"stacked_page")
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(10)
        self.stacked_page.setFont(font4)
        self.stacked_page.setStyleSheet(u"")
        self.stacked_page.setLineWidth(0)
        self.manage_page = QWidget()
        self.manage_page.setObjectName(u"manage_page")
        self.verticalLayout_4 = QVBoxLayout(self.manage_page)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 15, 0, 0)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.add_btn = QPushButton(self.manage_page)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(80, 32))
        self.add_btn.setMaximumSize(QSize(80, 32))
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.add_btn.setFont(font5)
        self.add_btn.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.add_btn)

        self.del_btn = QPushButton(self.manage_page)
        self.del_btn.setObjectName(u"del_btn")
        self.del_btn.setMinimumSize(QSize(80, 32))
        self.del_btn.setMaximumSize(QSize(80, 32))
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(12)
        self.del_btn.setFont(font6)
        self.del_btn.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.del_btn)

        self.label_6 = QLabel(self.manage_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(80, 32))
        self.label_6.setMaximumSize(QSize(80, 32))
        self.label_6.setFont(font6)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_6)

        self.comboBox = QComboBox(self.manage_page)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(120, 32))
        self.comboBox.setMaximumSize(QSize(120, 32))
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        self.comboBox.setFont(font7)
        self.comboBox.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.comboBox)

        self.keyword = QLineEdit(self.manage_page)
        self.keyword.setObjectName(u"keyword")
        self.keyword.setMinimumSize(QSize(180, 32))
        self.keyword.setMaximumSize(QSize(180, 32))
        self.keyword.setFont(font6)
        self.keyword.setStyleSheet(u"")
        self.keyword.setMaxLength(20)

        self.horizontalLayout_11.addWidget(self.keyword)

        self.search = QPushButton(self.manage_page)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(80, 32))
        self.search.setMaximumSize(QSize(80, 32))
        self.search.setFont(font6)
        self.search.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.search)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.tableWidget = QTableWidget(self.manage_page)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(700, 0))
        self.tableWidget.setFont(font7)
        self.tableWidget.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.stacked_page.addWidget(self.manage_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout_5 = QVBoxLayout(self.setting_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.setting_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(50, 25))
        self.scrollArea.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 783, 373))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(500, 180))
        self.groupBox.setMaximumSize(QSize(1000, 180))
        font8 = QFont()
        font8.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font8.setPointSize(13)
        font8.setBold(True)
        self.groupBox.setFont(font8)
        self.groupBox.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(40, -1, 0, 0)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setMaximumSize(QSize(100, 16777215))
        font9 = QFont()
        font9.setFamilies([u"\u5b8b\u4f53"])
        font9.setPointSize(12)
        self.label_3.setFont(font9)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.db_label = QLabel(self.groupBox)
        self.db_label.setObjectName(u"db_label")
        font10 = QFont()
        font10.setFamilies([u"\u5b8b\u4f53"])
        font10.setPointSize(12)
        font10.setUnderline(False)
        self.db_label.setFont(font10)
        self.db_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.db_label, 0, 1, 1, 1)

        self.db_bth = QPushButton(self.groupBox)
        self.db_bth.setObjectName(u"db_bth")
        self.db_bth.setMinimumSize(QSize(60, 25))
        self.db_bth.setMaximumSize(QSize(60, 25))
        self.db_bth.setFont(font9)
        self.db_bth.setStyleSheet(u"")

        self.gridLayout.addWidget(self.db_bth, 0, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 16777215))
        self.label_4.setFont(font9)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.path_label = QLabel(self.groupBox)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setFont(font9)
        self.path_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.path_label, 1, 1, 1, 1)

        self.path_btn = QPushButton(self.groupBox)
        self.path_btn.setObjectName(u"path_btn")
        self.path_btn.setMaximumSize(QSize(60, 25))
        self.path_btn.setFont(font9)
        self.path_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.path_btn, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 16777215))
        self.label_5.setFont(font9)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.log_label = QLabel(self.groupBox)
        self.log_label.setObjectName(u"log_label")
        self.log_label.setFont(font9)
        self.log_label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.log_label, 2, 1, 1, 1)

        self.log_btn = QPushButton(self.groupBox)
        self.log_btn.setObjectName(u"log_btn")
        self.log_btn.setMaximumSize(QSize(60, 25))
        self.log_btn.setFont(font9)
        self.log_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.log_btn, 2, 2, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(1000, 580))
        font11 = QFont()
        font11.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font11.setPointSize(14)
        font11.setBold(True)
        self.groupBox_2.setFont(font11)
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setContentsMargins(30, 40, -1, 0)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(100, 16777215))
        self.label_9.setFont(font9)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.pub_key_label = QLabel(self.groupBox_2)
        self.pub_key_label.setObjectName(u"pub_key_label")
        self.pub_key_label.setFont(font9)
        self.pub_key_label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pub_key_label, 0, 1, 1, 1)

        self.public_btn = QPushButton(self.groupBox_2)
        self.public_btn.setObjectName(u"public_btn")
        self.public_btn.setMinimumSize(QSize(60, 25))
        self.public_btn.setMaximumSize(QSize(60, 25))
        self.public_btn.setFont(font9)
        self.public_btn.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.public_btn, 0, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(100, 0))
        self.label_10.setMaximumSize(QSize(100, 16777215))
        self.label_10.setFont(font9)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.priv_key_label = QLabel(self.groupBox_2)
        self.priv_key_label.setObjectName(u"priv_key_label")
        self.priv_key_label.setFont(font9)
        self.priv_key_label.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.priv_key_label, 1, 1, 1, 1)

        self.private_btn = QPushButton(self.groupBox_2)
        self.private_btn.setObjectName(u"private_btn")
        self.private_btn.setMinimumSize(QSize(60, 25))
        self.private_btn.setMaximumSize(QSize(60, 25))
        self.private_btn.setFont(font9)
        self.private_btn.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.private_btn, 1, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 3)


        self.verticalLayout_6.addWidget(self.groupBox_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.stacked_page.addWidget(self.setting_page)
        self.about_page = QWidget()
        self.about_page.setObjectName(u"about_page")
        self.verticalLayout_8 = QVBoxLayout(self.about_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.about_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 775, 1040))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 50))
        self.label_7.setMaximumSize(QSize(16777215, 50))
        font12 = QFont()
        font12.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font12.setPointSize(16)
        font12.setBold(False)
        self.label_7.setFont(font12)
        self.label_7.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_7)

        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 250))
        self.textBrowser.setFont(font6)

        self.verticalLayout_7.addWidget(self.textBrowser)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 50))
        self.label_8.setMaximumSize(QSize(16777215, 50))
        font13 = QFont()
        font13.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font13.setPointSize(16)
        self.label_8.setFont(font13)
        self.label_8.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_8)

        self.textBrowser_2 = QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMinimumSize(QSize(0, 300))
        self.textBrowser_2.setFont(font6)

        self.verticalLayout_7.addWidget(self.textBrowser_2)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 50))
        self.label_11.setFont(font13)
        self.label_11.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.label_11)

        self.textBrowser_3 = QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setMinimumSize(QSize(0, 240))
        self.textBrowser_3.setFont(font6)

        self.verticalLayout_7.addWidget(self.textBrowser_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.stacked_page.addWidget(self.about_page)

        self.horizontalLayout_9.addWidget(self.stacked_page)


        self.horizontalLayout_8.addWidget(self.body_right)


        self.verticalLayout.addWidget(self.body)

        self.booter = QFrame(manage)
        self.booter.setObjectName(u"booter")
        self.booter.setMinimumSize(QSize(0, 30))
        self.booter.setMaximumSize(QSize(16777215, 30))
        self.booter.setStyleSheet(u"")
        self.booter.setFrameShape(QFrame.StyledPanel)
        self.booter.setFrameShadow(QFrame.Raised)
        self.booter.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.booter)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(self.booter)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(240, 0))
        self.info_frame.setMaximumSize(QSize(240, 16777215))
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.info_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.status_info = QLabel(self.info_frame)
        self.status_info.setObjectName(u"status_info")
        self.status_info.setMinimumSize(QSize(240, 0))
        self.status_info.setMaximumSize(QSize(240, 16777215))
        self.status_info.setFont(font4)
        self.status_info.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.status_info)


        self.horizontalLayout_4.addWidget(self.info_frame)

        self.progress_frame = QFrame(self.booter)
        self.progress_frame.setObjectName(u"progress_frame")
        self.progress_frame.setFrameShape(QFrame.StyledPanel)
        self.progress_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.progress_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.progress_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.horizontalLayout_5.addWidget(self.progressBar)


        self.horizontalLayout_4.addWidget(self.progress_frame)

        self.time_frame = QFrame(self.booter)
        self.time_frame.setObjectName(u"time_frame")
        self.time_frame.setMinimumSize(QSize(200, 0))
        self.time_frame.setMaximumSize(QSize(200, 16777215))
        self.time_frame.setFrameShape(QFrame.StyledPanel)
        self.time_frame.setFrameShadow(QFrame.Raised)
        self.time_frame.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.time_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.state_time = QLabel(self.time_frame)
        self.state_time.setObjectName(u"state_time")
        self.state_time.setMinimumSize(QSize(200, 0))
        self.state_time.setMaximumSize(QSize(200, 16777215))
        font14 = QFont()
        font14.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font14.setPointSize(11)
        self.state_time.setFont(font14)
        self.state_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.state_time)


        self.horizontalLayout_4.addWidget(self.time_frame)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(8, 6, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.set_size = QFrame(self.booter)
        self.set_size.setObjectName(u"set_size")
        self.set_size.setMinimumSize(QSize(10, 10))
        self.set_size.setMaximumSize(QSize(10, 10))
        self.set_size.setLayoutDirection(Qt.RightToLeft)
        self.set_size.setAutoFillBackground(False)
        self.set_size.setStyleSheet(u"")
        self.set_size.setFrameShape(QFrame.StyledPanel)
        self.set_size.setFrameShadow(QFrame.Raised)
        self.set_size.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.set_size)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.booter)


        self.retranslateUi(manage)
        self.close_btn.clicked.connect(manage.close)
        self.min_btn.clicked.connect(manage.showMinimized)

        self.stacked_page.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(manage)
    # setupUi

    def retranslateUi(self, manage):
        manage.setWindowTitle(QCoreApplication.translate("manage", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("manage", u"\u5bc6\u7801\u7ba1\u7406\u5668", None))
        self.min_btn.setText("")
        self.max_btn.setText("")
        self.close_btn.setText("")
        self.extend_btn.setText(QCoreApplication.translate("manage", u"\u6269\u5c55", None))
        self.manage_btn.setText(QCoreApplication.translate("manage", u"\u7ba1\u7406", None))
        self.setting_btn.setText(QCoreApplication.translate("manage", u"\u8bbe\u7f6e", None))
        self.about_btn.setText(QCoreApplication.translate("manage", u"\u5173\u4e8e", None))
        self.exit_btn.setText(QCoreApplication.translate("manage", u"\u9000\u51fa", None))
        self.add_btn.setText(QCoreApplication.translate("manage", u"\u589e\u52a0", None))
        self.del_btn.setText(QCoreApplication.translate("manage", u"\u5220\u9664", None))
        self.label_6.setText(QCoreApplication.translate("manage", u"\u68c0\u7d22\u6761\u4ef6", None))
        self.keyword.setPlaceholderText(QCoreApplication.translate("manage", u"\u8bf7\u8f93\u5165\u5173\u952e\u8bcd", None))
        self.search.setText(QCoreApplication.translate("manage", u"\u68c0\u7d22", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("manage", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("manage", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("manage", u"\u8d26\u53f7", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("manage", u"\u52a0\u5bc6\u5bc6\u7801", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("manage", u"\u5907\u6ce8", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("manage", u"\u521b\u5efa\u65f6\u95f4", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("manage", u"\u5bc6\u7801\u5f3a\u5ea6", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("manage", u"\u67e5\u770b\u5bc6\u7801", None));
        self.groupBox.setTitle(QCoreApplication.translate("manage", u"\u914d\u7f6e\u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("manage", u"\u6570\u636e\u5e93\u6587\u4ef6", None))
        self.db_label.setText(QCoreApplication.translate("manage", u"E:\\Python_code\\manage\\config\\path.json", None))
        self.db_bth.setText(QCoreApplication.translate("manage", u"\u6d4f\u89c8", None))
        self.label_4.setText(QCoreApplication.translate("manage", u"\u914d\u7f6e\u6587\u4ef6", None))
        self.path_label.setText(QCoreApplication.translate("manage", u"E:\\Python_code\\manage\\config\\path.json", None))
        self.path_btn.setText(QCoreApplication.translate("manage", u"\u6d4f\u89c8", None))
        self.label_5.setText(QCoreApplication.translate("manage", u"\u65e5\u5fd7\u6587\u4ef6", None))
        self.log_label.setText(QCoreApplication.translate("manage", u"E:\\Python_code\\manage\\config\\path.json", None))
        self.log_btn.setText(QCoreApplication.translate("manage", u"\u6d4f\u89c8", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("manage", u"\u5bc6\u94a5", None))
        self.label_9.setText(QCoreApplication.translate("manage", u"\u516c\u94a5", None))
        self.pub_key_label.setText(QCoreApplication.translate("manage", u"E:\\Python_code\\manage\\config\\path.json", None))
        self.public_btn.setText(QCoreApplication.translate("manage", u"\u6d4f\u89c8", None))
        self.label_10.setText(QCoreApplication.translate("manage", u"\u79c1\u94a5", None))
        self.priv_key_label.setText(QCoreApplication.translate("manage", u"E:\\Python_code\\manage\\config\\path.json", None))
        self.private_btn.setText(QCoreApplication.translate("manage", u"\u6d4f\u89c8", None))
        self.label_13.setText(QCoreApplication.translate("manage", u"\u79c1\u94a5\u8bf7\u59a5\u5584\u4fdd\u7ba1\uff0c\u5c3d\u91cf\u4e0e\u8be5\u8f6f\u4ef6\u5206\u79bb\uff0c\u9700\u8981\u89e3\u5bc6\u65f6\u518d\u52a0\u8f7d", None))
        self.label_7.setText(QCoreApplication.translate("manage", u"\u5f00\u53d1\u521d\u8877", None))
        self.textBrowser.setHtml(QCoreApplication.translate("manage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u5F88\u591A\u5C0F\u4F19\u4F34\u5E94\u8BE5\u90FD\u6709\u88AB\u76D7\u53F7\u7684\u7ECF\u5386\u5427\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u4E0D\u5F97\u4E0D\u8BF4\u6709\u4E9B\u9ED1\u5BA2\u786E\u5B9E\u975E\u5E38\u5389\u5BB3\uFF0C\u8F7B\u8F7B\u677E\u677E\u5C31\u80FD\u628A\u4F60\u7684\u8D26\u53F7\u76D7\u8D70\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u4E5F\u53EF\u80FD\u662F\u81EA\u5DF1\u8BBE\u7F6E\u7684\u5BC6\u7801\u5B9E\u5728\u592A\u7B80\u5355\u4E86\uFF0C\u6BD4\u5982123456\u8FD9\u79CD\u5BC6\u7801\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u8FD9\u79CD\u5BC6\u7801\u786E\u5B9E\u5F88\u5BB9\u6613\u8BB0\uFF0C\u4F46\u5B83\u5728\u5F88\u591A\u7206\u7834\u5B57\u5178\u4E2D\u90FD\u662F\u7B2C\u4E00\u4E2A\uFF0C\u4E5F\u5C31\u610F\u5473\u7740\u522B\u4EBA\u53EA\u8981\u4E00\u8BD5\u4FBF\u77E5\u9053\u4F60\u7684\u5BC6\u7801\u4E86\u3002</p>\n"
                                                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u5728\u8FD9\u8D8A\u6765\u8D8A\u900F\u660E\u7684\u4E16\u754C\u4E0A\uFF0C\u6211\u4EEC\u8FD8\u662F\u4FDD\u62A4\u4E00\u4E0B\u81EA\u5DF1\uFF0C\u4E0D\u8981\u518D\u7528\u90A3\u79CD\u5F31\u5BC6\u7801\u4E86\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u4E8E\u662F\u6211\u4EEC\u5F00\u53D1\u4E86\u8FD9\u6B3E\u5BC6\u7801\u7BA1\u7406\u5668\uFF0C\u65E8\u5728\u5E2E\u52A9\u5927\u5BB6\u66F4\u65B9\u4FBF\u5730\u7BA1\u7406\u81EA\u5DF1\u7684\u5BC6\u7801\uFF0C\u4E0D\u7528\u518D\u62C5\u5FC3\u8BB0\u4E0D\u4F4F\u4F17\u591A\u590D\u6742\u7684\u5BC6\u7801\u3002</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("manage", u"\u4f7f\u7528\u58f0\u660e", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("manage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u7a0b\u5e8f\u5728\u4f7f\u7528\u8fc7\u7a0b\u4e2d\u6240\u5b58\u50a8\u7684\u6570\u636e\u90fd\u5728\u672c\u5730\u6570\u636e\u5e93\u4e2d\uff0c\u8bf7\u52ff\u968f\u610f\u5c06\u79c1\u94a5\u4ee5\u53ca\u6570\u636e\u5e93\u6cc4\u9732</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u4e3a\u4e86\u4fdd\u8bc1\u6570\u636e\u5b89\u5168\uff0c\u8f6f\u4ef6\u4e0d\u4f1a\u8054\u7f51\u8bf7\u6c42\uff01\uff01\uff01\uff01\uff01\uff01</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u4e0d\u4f1a\u81ea\u52a8\u66f4\u65b0\u7b49\u7b49\u3002</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u8f6f\u4ef6\u4e2d\u6700\u91cd\u8981\u7684\u6570\u636e\u90fd\u7ecf\u8fc7\u52a0\u5bc6\uff0c\u4f46\u662f\u5982\u679c\u6709\u79c1\u94a5\u5b58\u5728\u4e5f\u662f\u53ef\u4ee5\u89e3\u5bc6\u7684\uff0c\u6240\u4ee5\u4f7f\u7528\u8fc7\u7a0b\u4e2d\u8bf7\u59a5\u5584\u4fdd\u7ba1\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u5185\u7f6e\u968f\u673a\u5bc6\u7801\u751f\u6210\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; font-size:16px; color:#55ff7f;\">	\u5927\u5199\u5b57\u6bcd\uff1aA,B,C\u2026Z;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; font-size:16px; color:#55ff7f;\">	\u5c0f\u5199\u5b57\u6bcd\uff1aa,b,c\u2026z;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; font-size:16px; color:#55ff7f;\">	\u6570\u5b57\uff1a0,1,2\u20269;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'inherit'; font-size:16px; color:#55ff7f;\">	\u7279\u6b8a\u7b26\u53f7\uff1a~,!,@,#,$,%,^;</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("manage", u"\u8f6f\u4ef6\u4f5c\u8005", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("manage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u6211\u4EEC\u7ECF\u9A8C\u6709\u9650\uFF0C\u53EF\u80FD\u7A0B\u5E8F\u4E5F\u8FD8\u5728\u5B58\u5728\u5F88\u591A\u95EE\u9898\uFF0C\u5982\u679C\u5927\u5BB6\u6709\u4EC0\u4E48\u597D\u7684\u5EFA\u8BAE\uFF0C\u6B22\u8FCE\u8054\u7CFB\u6211\u4EEC\u63D0\u51FA\uFF0C\u6211\u4EEC\u4F1A\u5C3D\u91CF\u5B8C\u5584\u8F6F\u4EF6\u3002</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    \u8054\u7cfb\u4f5c\u8005\uff1a</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5fae          \u4fe1\uff1a<span style=\" color:#00ffff;\">https://valley-ov.cn</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Q           Q\uff1a<span style=\" color:#ffaa00;\">1842360030</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u90ae          \u7bb1:   <span style=\" color:#aa55ff;\">valley-ov@qq.com</span></p></body></html>", None))
        self.status_info.setText("")
        self.state_time.setText("")
    # retranslateUi

