# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 720)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("background-color: rgb(249, 249, 249);")
        self.username_line_edit = QtWidgets.QLineEdit(Form)
        self.username_line_edit.setGeometry(QtCore.QRect(56, 217, 288, 48))
        self.username_line_edit.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    color: rgb(51, 51, 51);\n"
"    font: 75 8pt \"Microsoft YaHei\";\n"
"    background-color: rgb(237, 237, 237);\n"
"}\n"
"QLineEdit::hover {\n"
"    background-color: rgb(231, 231, 231);\n"
"}\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(51, 51, 51);\n"
"    background-color: rgb(249, 249, 249);\n"
"}")
        self.username_line_edit.setObjectName("username_line_edit")
        self.password_line_edit = QtWidgets.QLineEdit(Form)
        self.password_line_edit.setGeometry(QtCore.QRect(56, 281, 288, 48))
        self.password_line_edit.setStyleSheet("QLineEdit {\n"
"    border-radius: 5px;\n"
"    color: rgb(51, 51, 51);\n"
"    font: 75 8pt \"Microsoft YaHei\";\n"
"    background-color: rgb(237, 237, 237);\n"
"}\n"
"QLineEdit::hover {\n"
"    background-color: rgb(231, 231, 231);\n"
"}\n"
"QLineEdit::focus {\n"
"    border: 2px solid rgb(51, 51, 51);\n"
"    background-color: rgb(249, 249, 249);\n"
"}")
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.sign_in_label = QtWidgets.QLabel(Form)
        self.sign_in_label.setGeometry(QtCore.QRect(160, 159, 80, 33))
        self.sign_in_label.setStyleSheet("border-image: url(:/resources/resources/Sign_in.png);")
        self.sign_in_label.setText("")
        self.sign_in_label.setObjectName("sign_in_label")
        self.facebook_button = QtWidgets.QPushButton(Form)
        self.facebook_button.setGeometry(QtCore.QRect(56, 353, 91, 32))
        self.facebook_button.setStyleSheet("QPushButton {\n"
"    border-image: url(:/resources/resources/Facebook.png);\n"
"}\n"
"QPushButton::hover {\n"
"    border-image: url(:/resources/resources/Facebook_hovered.png);\n"
"}")
        self.facebook_button.setText("")
        self.facebook_button.setObjectName("facebook_button")
        self.google_button = QtWidgets.QPushButton(Form)
        self.google_button.setGeometry(QtCore.QRect(155, 353, 90, 32))
        self.google_button.setStyleSheet("QPushButton {\n"
"    border-image: url(:/resources/resources/Google.png);\n"
"}\n"
"QPushButton::hover {\n"
"    border-image: url(:/resources/resources/Google_hovered.png);\n"
"}")
        self.google_button.setText("")
        self.google_button.setObjectName("google_button")
        self.apple_button = QtWidgets.QPushButton(Form)
        self.apple_button.setGeometry(QtCore.QRect(253, 353, 91, 32))
        self.apple_button.setStyleSheet("QPushButton {\n"
"    border-image: url(:/resources/resources/Apple.png);\n"
"}\n"
"QPushButton::hover {\n"
"    border-image: url(:/resources/resources/Apple_hovered.png);\n"
"}")
        self.apple_button.setText("")
        self.apple_button.setObjectName("apple_button")
        self.help_tooltip = QtWidgets.QPushButton(Form)
        self.help_tooltip.setGeometry(QtCore.QRect(326, 44, 22, 22))
        self.help_tooltip.setStyleSheet("border-image: url(:/resources/resources/Help2.png);")
        self.help_tooltip.setText("")
        self.help_tooltip.setObjectName("help_tooltip")
        self.stay_signed_in_checkbox = QtWidgets.QCheckBox(Form)
        self.stay_signed_in_checkbox.setGeometry(QtCore.QRect(56, 395, 17, 21))
        self.stay_signed_in_checkbox.setStyleSheet("QCheckBox::indicator:unchecked {\n"
"    border-image: url(:/resources/resources/Checkbox_unchecked.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border-image: url(:/resources/resources/Checkbox_unchecked_hovered.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-image: url(:/resources/resources/Checkbox_checked.png);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    border-image: url(:/resources/resources/Checkbox_checked_hovered.png);\n"
"}")
        self.stay_signed_in_checkbox.setText("")
        self.stay_signed_in_checkbox.setObjectName("stay_signed_in_checkbox")
        self.login_button = QtWidgets.QPushButton(Form)
        self.login_button.setGeometry(QtCore.QRect(168, 512, 64, 64))
        self.login_button.setStyleSheet("QPushButton {\n"
"    border-image: url(:/resources/resources/Login_button.png);\n"
"}\n"
"QPushButton::hover {\n"
"    border-image: url(:/resources/resources/Login_button_hovered.png);\n"
"}")
        self.login_button.setText("")
        self.login_button.setObjectName("login_button")
        self.version_label = QtWidgets.QLabel(Form)
        self.version_label.setGeometry(QtCore.QRect(298, 657, 48, 18))
        self.version_label.setStyleSheet("QLabel {\n"
"    border-image: url(:/resources/resources/version_label.png);\n"
"}\n"
"QLabel::hover {\n"
"    border-image: url(:/resources/resources/version_label_hovered.png);\n"
"}")
        self.version_label.setText("")
        self.version_label.setObjectName("version_label")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(156, 637, 88, 18))
        self.label_1.setStyleSheet("QLabel {\n"
"    border-image: url(:/resources/resources/Label_1.png);\n"
"}\n"
"QLabel::hover {\n"
"    border-image: url(:/resources/resources/Label_1_hovered.png);\n"
"}")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(149, 654, 102, 18))
        self.label_2.setStyleSheet("QLabel {\n"
"    border-image: url(:/resources/resources/Label_2.png);\n"
"}\n"
"QLabel::hover {\n"
"    border-image: url(:/resources/resources/Label_2_hovered.png);\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.checkbox_label = QtWidgets.QLabel(Form)
        self.checkbox_label.setGeometry(QtCore.QRect(77, 395, 94, 22))
        self.checkbox_label.setStyleSheet("QLabel {\n"
"    border-image: url(:/resources/resources/Checkbox_label.png);\n"
"}\n"
"QLabel::hover {\n"
"    border-image: url(:/resources/resources/Checkbox_label_hovered.png);\n"
"}")
        self.checkbox_label.setText("")
        self.checkbox_label.setObjectName("checkbox_label")
        self.riot_games_logo = QtWidgets.QLabel(Form)
        self.riot_games_logo.setGeometry(QtCore.QRect(138, 51, 126, 61))
        self.riot_games_logo.setStyleSheet("border-image: url(:/resources/resources/Riot_Games.png);")
        self.riot_games_logo.setText("")
        self.riot_games_logo.setObjectName("riot_games_logo")
        self.username_label = QtWidgets.QLabel(Form)
        self.username_label.setGeometry(QtCore.QRect(72, 236, 59, 8))
        self.username_label.setStyleSheet("border-image: url(:/resources/resources/Username_label.png);")
        self.username_label.setText("")
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(Form)
        self.password_label.setGeometry(QtCore.QRect(72, 300, 61, 8))
        self.password_label.setStyleSheet("border-image: url(:/resources/resources/Password_label.png);")
        self.password_label.setText("")
        self.password_label.setObjectName("password_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.help_tooltip, self.username_line_edit)
        Form.setTabOrder(self.username_line_edit, self.password_line_edit)
        Form.setTabOrder(self.password_line_edit, self.facebook_button)
        Form.setTabOrder(self.facebook_button, self.google_button)
        Form.setTabOrder(self.google_button, self.apple_button)
        Form.setTabOrder(self.apple_button, self.stay_signed_in_checkbox)
        Form.setTabOrder(self.stay_signed_in_checkbox, self.login_button)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Widget"))
import Widget_Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
