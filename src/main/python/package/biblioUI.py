# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biblioUI.ui',
# licensing of 'biblioUI.ui' applies.
#
# Created: Sun Oct 13 13:44:50 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_form_biblio(object):
    def setupUi(self, form_biblio):
        form_biblio.setObjectName("form_biblio")
        form_biblio.resize(700, 600)
        form_biblio.setMinimumSize(QtCore.QSize(700, 600))
        form_biblio.setMaximumSize(QtCore.QSize(700, 600))
        self.gridLayout = QtWidgets.QGridLayout(form_biblio)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(form_biblio)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_liste = QtWidgets.QWidget()
        self.tab_liste.setObjectName("tab_liste")
        self.lw_listeLivre = QtWidgets.QListWidget(self.tab_liste)
        self.lw_listeLivre.setGeometry(QtCore.QRect(100, 50, 471, 471))
        self.lw_listeLivre.setObjectName("lw_listeLivre")
        self.btn_effacer_livre = QtWidgets.QPushButton(self.tab_liste)
        self.btn_effacer_livre.setGeometry(QtCore.QRect(100, 10, 131, 32))
        self.btn_effacer_livre.setObjectName("btn_effacer_livre")
        self.btn_preter_livre = QtWidgets.QPushButton(self.tab_liste)
        self.btn_preter_livre.setGeometry(QtCore.QRect(250, 10, 131, 32))
        self.btn_preter_livre.setObjectName("btn_preter_livre")
        self.btn_lire_info = QtWidgets.QPushButton(self.tab_liste)
        self.btn_lire_info.setGeometry(QtCore.QRect(400, 10, 171, 32))
        self.btn_lire_info.setObjectName("btn_lire_info")
        self.tabWidget.addTab(self.tab_liste, "")
        self.tab_info = QtWidgets.QWidget()
        self.tab_info.setObjectName("tab_info")
        self.lb_titre_info = QtWidgets.QLabel(self.tab_info)
        self.lb_titre_info.setGeometry(QtCore.QRect(60, 20, 131, 21))
        self.lb_titre_info.setObjectName("lb_titre_info")
        self.le_titre_info = QtWidgets.QLineEdit(self.tab_info)
        self.le_titre_info.setGeometry(QtCore.QRect(230, 20, 301, 21))
        self.le_titre_info.setReadOnly(True)
        self.le_titre_info.setObjectName("le_titre_info")
        self.lb_serie_info = QtWidgets.QLabel(self.tab_info)
        self.lb_serie_info.setGeometry(QtCore.QRect(60, 50, 60, 16))
        self.lb_serie_info.setObjectName("lb_serie_info")
        self.le_serie_info = QtWidgets.QLineEdit(self.tab_info)
        self.le_serie_info.setGeometry(QtCore.QRect(230, 50, 301, 21))
        self.le_serie_info.setReadOnly(True)
        self.le_serie_info.setObjectName("le_serie_info")
        self.txt_sinopsis_info = QtWidgets.QTextBrowser(self.tab_info)
        self.txt_sinopsis_info.setGeometry(QtCore.QRect(230, 120, 301, 191))
        self.txt_sinopsis_info.setReadOnly(True)
        self.txt_sinopsis_info.setObjectName("txt_sinopsis_info")
        self.lb_sinopsis_info = QtWidgets.QLabel(self.tab_info)
        self.lb_sinopsis_info.setGeometry(QtCore.QRect(60, 120, 131, 21))
        self.lb_sinopsis_info.setObjectName("lb_sinopsis_info")
        self.le_pret_info = QtWidgets.QLineEdit(self.tab_info)
        self.le_pret_info.setGeometry(QtCore.QRect(230, 340, 301, 21))
        self.le_pret_info.setReadOnly(True)
        self.le_pret_info.setObjectName("le_pret_info")
        self.le_auteur_info = QtWidgets.QLineEdit(self.tab_info)
        self.le_auteur_info.setEnabled(True)
        self.le_auteur_info.setGeometry(QtCore.QRect(230, 80, 301, 21))
        self.le_auteur_info.setReadOnly(True)
        self.le_auteur_info.setObjectName("le_auteur_info")
        self.lb_auteur_info = QtWidgets.QLabel(self.tab_info)
        self.lb_auteur_info.setGeometry(QtCore.QRect(60, 80, 60, 16))
        self.lb_auteur_info.setObjectName("lb_auteur_info")
        self.chk_pret_info = QtWidgets.QCheckBox(self.tab_info)
        self.chk_pret_info.setGeometry(QtCore.QRect(60, 340, 161, 20))
        self.chk_pret_info.setTristate(False)
        self.chk_pret_info.setObjectName("chk_pret_info")
        self.btn_modifier = QtWidgets.QPushButton(self.tab_info)
        self.btn_modifier.setGeometry(QtCore.QRect(260, 390, 113, 32))
        self.btn_modifier.setObjectName("btn_modifier")
        self.tabWidget.addTab(self.tab_info, "")
        self.tab_ajouter = QtWidgets.QWidget()
        self.tab_ajouter.setObjectName("tab_ajouter")
        self.btn_enregistrer = QtWidgets.QPushButton(self.tab_ajouter)
        self.btn_enregistrer.setGeometry(QtCore.QRect(260, 380, 221, 31))
        self.btn_enregistrer.setObjectName("btn_enregistrer")
        self.btn_annuler = QtWidgets.QPushButton(self.tab_ajouter)
        self.btn_annuler.setGeometry(QtCore.QRect(110, 400, 113, 32))
        self.btn_annuler.setObjectName("btn_annuler")
        self.le_titre_ajout = QtWidgets.QLineEdit(self.tab_ajouter)
        self.le_titre_ajout.setGeometry(QtCore.QRect(230, 20, 301, 21))
        self.le_titre_ajout.setObjectName("le_titre_ajout")
        self.lb_titre_ajout = QtWidgets.QLabel(self.tab_ajouter)
        self.lb_titre_ajout.setGeometry(QtCore.QRect(60, 20, 131, 21))
        self.lb_titre_ajout.setObjectName("lb_titre_ajout")
        self.lb_sinopsis_ajout = QtWidgets.QLabel(self.tab_ajouter)
        self.lb_sinopsis_ajout.setGeometry(QtCore.QRect(60, 120, 131, 21))
        self.lb_sinopsis_ajout.setObjectName("lb_sinopsis_ajout")
        self.lb_serie_ajout = QtWidgets.QLabel(self.tab_ajouter)
        self.lb_serie_ajout.setGeometry(QtCore.QRect(60, 50, 60, 16))
        self.lb_serie_ajout.setObjectName("lb_serie_ajout")
        self.le_serie_ajout = QtWidgets.QLineEdit(self.tab_ajouter)
        self.le_serie_ajout.setGeometry(QtCore.QRect(230, 50, 301, 21))
        self.le_serie_ajout.setObjectName("le_serie_ajout")
        self.lb_auteur_ajout = QtWidgets.QLabel(self.tab_ajouter)
        self.lb_auteur_ajout.setGeometry(QtCore.QRect(60, 80, 60, 16))
        self.lb_auteur_ajout.setObjectName("lb_auteur_ajout")
        self.le_auteur_ajout = QtWidgets.QLineEdit(self.tab_ajouter)
        self.le_auteur_ajout.setGeometry(QtCore.QRect(230, 80, 301, 21))
        self.le_auteur_ajout.setObjectName("le_auteur_ajout")
        self.chk_pret_ajout = QtWidgets.QCheckBox(self.tab_ajouter)
        self.chk_pret_ajout.setGeometry(QtCore.QRect(60, 340, 161, 20))
        self.chk_pret_ajout.setTristate(False)
        self.chk_pret_ajout.setObjectName("chk_pret_ajout")
        self.le_pret_ajout = QtWidgets.QLineEdit(self.tab_ajouter)
        self.le_pret_ajout.setGeometry(QtCore.QRect(230, 340, 301, 21))
        self.le_pret_ajout.setObjectName("le_pret_ajout")
        self.txt_sinopsis_ajout = QtWidgets.QPlainTextEdit(self.tab_ajouter)
        self.txt_sinopsis_ajout.setGeometry(QtCore.QRect(230, 120, 301, 211))
        self.txt_sinopsis_ajout.setObjectName("txt_sinopsis_ajout")
        self.btn_modifier_exec = QtWidgets.QPushButton(self.tab_ajouter)
        self.btn_modifier_exec.setGeometry(QtCore.QRect(260, 420, 221, 31))
        self.btn_modifier_exec.setObjectName("btn_modifier_exec")
        self.tabWidget.addTab(self.tab_ajouter, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(form_biblio)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(form_biblio)

    def retranslateUi(self, form_biblio):
        form_biblio.setWindowTitle(QtWidgets.QApplication.translate("form_biblio", "BiblioTeck", None, -1))
        self.btn_effacer_livre.setText(QtWidgets.QApplication.translate("form_biblio", "Effacer un livre", None, -1))
        self.btn_preter_livre.setText(QtWidgets.QApplication.translate("form_biblio", "Preter un livre", None, -1))
        self.btn_lire_info.setText(QtWidgets.QApplication.translate("form_biblio", "Lire les informations", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_liste), QtWidgets.QApplication.translate("form_biblio", "Liste des livres", None, -1))
        self.lb_titre_info.setText(QtWidgets.QApplication.translate("form_biblio", "Titre", None, -1))
        self.lb_serie_info.setText(QtWidgets.QApplication.translate("form_biblio", "Série", None, -1))
        self.lb_sinopsis_info.setText(QtWidgets.QApplication.translate("form_biblio", "Sinopsis", None, -1))
        self.lb_auteur_info.setText(QtWidgets.QApplication.translate("form_biblio", "Auteur", None, -1))
        self.chk_pret_info.setText(QtWidgets.QApplication.translate("form_biblio", "En prêt chez :", None, -1))
        self.btn_modifier.setText(QtWidgets.QApplication.translate("form_biblio", "modifier", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_info), QtWidgets.QApplication.translate("form_biblio", "Information sur un livre", None, -1))
        self.btn_enregistrer.setText(QtWidgets.QApplication.translate("form_biblio", "Enregistrer un nouveau livre", None, -1))
        self.btn_annuler.setText(QtWidgets.QApplication.translate("form_biblio", "Annuler", None, -1))
        self.lb_titre_ajout.setText(QtWidgets.QApplication.translate("form_biblio", "Titre", None, -1))
        self.lb_sinopsis_ajout.setText(QtWidgets.QApplication.translate("form_biblio", "Sinopsis", None, -1))
        self.lb_serie_ajout.setText(QtWidgets.QApplication.translate("form_biblio", "Série", None, -1))
        self.lb_auteur_ajout.setText(QtWidgets.QApplication.translate("form_biblio", "Auteur", None, -1))
        self.chk_pret_ajout.setText(QtWidgets.QApplication.translate("form_biblio", "En prêt chez :", None, -1))
        self.btn_modifier_exec.setText(QtWidgets.QApplication.translate("form_biblio", "Modifier un livre existant", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ajouter), QtWidgets.QApplication.translate("form_biblio", "Ajouter/modifier un livre", None, -1))

