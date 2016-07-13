# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program_layout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 440)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Ahmed/.designer/backup/eye.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("QRadioButton::indicator\n"
"{\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel {\n"
"   font-size: 18px;  \n"
"}\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 18px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(9, 9, 791, 420))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Pristina"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.capture_bt = QtGui.QPushButton(self.tab)
        self.capture_bt.setGeometry(QtCore.QRect(230, 310, 150, 50))
        self.capture_bt.setStyleSheet(_fromUtf8(""))
        self.capture_bt.setObjectName(_fromUtf8("capture_bt"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(50, 100, 101, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(50, 190, 121, 51))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.type_text = QtGui.QTextEdit(self.tab)
        self.type_text.setGeometry(QtCore.QRect(220, 40, 140, 40))
        self.type_text.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.type_text.setObjectName(_fromUtf8("type_text"))
        self.store_bt = QtGui.QPushButton(self.tab)
        self.store_bt.setGeometry(QtCore.QRect(400, 310, 150, 50))
        self.store_bt.setStyleSheet(_fromUtf8(""))
        self.store_bt.setObjectName(_fromUtf8("store_bt"))
        self.videoFrame = QtGui.QLabel(self.tab)
        self.videoFrame.setGeometry(QtCore.QRect(405, 20, 341, 241))
        self.videoFrame.setText(_fromUtf8(""))
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(50, 150, 71, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.wight_text = QtGui.QLineEdit(self.tab)
        self.wight_text.setGeometry(QtCore.QRect(220, 150, 140, 40))
        self.wight_text.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.wight_text.setObjectName(_fromUtf8("wight_text"))
        self.in_check = QtGui.QRadioButton(self.tab)
        self.in_check.setGeometry(QtCore.QRect(220, 270, 51, 16))
        self.in_check.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.in_check.setObjectName(_fromUtf8("in_check"))
        self.out_check = QtGui.QRadioButton(self.tab)
        self.out_check.setGeometry(QtCore.QRect(340, 270, 71, 21))
        self.out_check.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.out_check.setObjectName(_fromUtf8("out_check"))
        self.exdate = QtGui.QDateEdit(self.tab)
        self.exdate.setGeometry(QtCore.QRect(220, 200, 140, 40))
        self.exdate.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.exdate.setObjectName(_fromUtf8("exdate"))
        self.Quantity_val = QtGui.QSpinBox(self.tab)
        self.Quantity_val.setGeometry(QtCore.QRect(220, 100, 140, 40))
        self.Quantity_val.setStyleSheet(_fromUtf8("font: 16pt \"MS Shell Dlg 2\";"))
        self.Quantity_val.setObjectName(_fromUtf8("Quantity_val"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 61, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tablefood = QtGui.QTableWidget(self.tab_5)
        self.tablefood.setGeometry(QtCore.QRect(10, 0, 761, 300))
        self.tablefood.setStyleSheet(_fromUtf8("\n"
"font: 12pt \"MS Shell Dlg 2\";"))
        self.tablefood.setObjectName(_fromUtf8("tablefood"))
        self.tablefood.setColumnCount(7)
        self.tablefood.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tablefood.setHorizontalHeaderItem(6, item)
        self.update_food = QtGui.QPushButton(self.tab_5)
        self.update_food.setGeometry(QtCore.QRect(315, 310, 150, 50))
        self.update_food.setObjectName(_fromUtf8("update_food"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tablelist = QtGui.QTableWidget(self.tab_2)
        self.tablelist.setGeometry(QtCore.QRect(10, 0, 330, 300))
        self.tablelist.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.tablelist.setObjectName(_fromUtf8("tablelist"))
        self.tablelist.setColumnCount(3)
        self.tablelist.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.tablelist.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablelist.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablelist.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablelist.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablelist.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablelist.setHorizontalHeaderItem(2, item)
        self.update_list = QtGui.QPushButton(self.tab_2)
        self.update_list.setGeometry(QtCore.QRect(315, 310, 150, 50))
        self.update_list.setObjectName(_fromUtf8("update_list"))
        self.instock = QtGui.QTableWidget(self.tab_2)
        self.instock.setGeometry(QtCore.QRect(435, 0, 330, 300))
        self.instock.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.instock.setObjectName(_fromUtf8("instock"))
        self.instock.setColumnCount(1)
        self.instock.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.instock.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.instock.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.instock.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.instock.setHorizontalHeaderItem(0, item)
        self.instock.horizontalHeader().setDefaultSectionSize(320)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.web = QtWebKit.QWebView(self.tab_3)
        self.web.setGeometry(QtCore.QRect(9, 9, 761, 401))
        self.web.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.web.setObjectName(_fromUtf8("web"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_2 = QtGui.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 181, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.temp_bar = QtGui.QProgressBar(self.tab_4)
        self.temp_bar.setGeometry(QtCore.QRect(370, 20, 211, 23))
        self.temp_bar.setProperty("value", 24)
        self.temp_bar.setObjectName(_fromUtf8("temp_bar"))
        self.dist_bar = QtGui.QProgressBar(self.tab_4)
        self.dist_bar.setGeometry(QtCore.QRect(370, 80, 211, 23))
        self.dist_bar.setProperty("value", 24)
        self.dist_bar.setObjectName(_fromUtf8("dist_bar"))
        self.dist_val = QtGui.QLabel(self.tab_4)
        self.dist_val.setGeometry(QtCore.QRect(270, 80, 46, 13))
        self.dist_val.setText(_fromUtf8(""))
        self.dist_val.setObjectName(_fromUtf8("dist_val"))
        self.temp_val = QtGui.QLabel(self.tab_4)
        self.temp_val.setGeometry(QtCore.QRect(270, 20, 46, 13))
        self.temp_val.setText(_fromUtf8(""))
        self.temp_val.setObjectName(_fromUtf8("temp_val"))
        self.label = QtGui.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(40, 20, 161, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.notrun = QtGui.QCommandLinkButton(self.tab_4)
        self.notrun.setGeometry(QtCore.QRect(420, 120, 350, 40))
        self.notrun.setObjectName(_fromUtf8("notrun"))
        self.noice = QtGui.QCommandLinkButton(self.tab_4)
        self.noice.setGeometry(QtCore.QRect(0, 120, 350, 40))
        self.noice.setObjectName(_fromUtf8("noice"))
        self.toocold = QtGui.QCommandLinkButton(self.tab_4)
        self.toocold.setGeometry(QtCore.QRect(420, 170, 350, 41))
        self.toocold.setObjectName(_fromUtf8("toocold"))
        self.toowarm = QtGui.QCommandLinkButton(self.tab_4)
        self.toowarm.setGeometry(QtCore.QRect(0, 170, 350, 40))
        self.toowarm.setObjectName(_fromUtf8("toowarm"))
        self.tableWidget = QtGui.QTableWidget(self.tab_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 230, 781, 141))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(4)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(800)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(33)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(19)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "refrigerator eye", None))
        self.capture_bt.setText(_translate("Form", "Capture", None))
        self.label_4.setText(_translate("Form", "Quantity :", None))
        self.label_5.setText(_translate("Form", "Expiring date :", None))
        self.store_bt.setText(_translate("Form", "Store", None))
        self.label_6.setText(_translate("Form", "weight :", None))
        self.in_check.setText(_translate("Form", "IN", None))
        self.out_check.setText(_translate("Form", "OUT", None))
        self.label_3.setText(_translate("Form", "Type :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "status", None))
        item = self.tablefood.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.tablefood.verticalHeaderItem(1)
        item.setText(_translate("Form", "2", None))
        item = self.tablefood.verticalHeaderItem(2)
        item.setText(_translate("Form", "3", None))
        item = self.tablefood.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.tablefood.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Quantity", None))
        item = self.tablefood.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Calories", None))
        item = self.tablefood.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Fat", None))
        item = self.tablefood.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Sugars", None))
        item = self.tablefood.horizontalHeaderItem(5)
        item.setText(_translate("Form", "In date", None))
        item = self.tablefood.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Expiring date", None))
        self.update_food.setText(_translate("Form", "Update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Stored Food", None))
        item = self.tablelist.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.tablelist.verticalHeaderItem(1)
        item.setText(_translate("Form", "2", None))
        item = self.tablelist.verticalHeaderItem(2)
        item.setText(_translate("Form", "3", None))
        item = self.tablelist.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Type", None))
        item = self.tablelist.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Quantity", None))
        item = self.tablelist.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Price", None))
        self.update_list.setText(_translate("Form", "Update", None))
        item = self.instock.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.instock.verticalHeaderItem(1)
        item.setText(_translate("Form", "2", None))
        item = self.instock.verticalHeaderItem(2)
        item.setText(_translate("Form", "3", None))
        item = self.instock.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Pormotions & In Stock ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "shopping list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "recipes", None))
        self.label_2.setText(_translate("Form", "Distance from wall", None))
        self.label.setText(_translate("Form", "Temperature", None))
        self.notrun.setText(_translate("Form", "My refrigerator isn’t running", None))
        self.noice.setText(_translate("Form", "My  refrigerator isn’t making ice", None))
        self.toocold.setText(_translate("Form", "My refrigerator is too cold", None))
        self.toowarm.setText(_translate("Form", "My refrigerator is too warm", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Notification area", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "troubleshooting", None))

from PyQt4 import QtWebKit
