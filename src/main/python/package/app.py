from package.livre import Livre, get_livre
from PySide2 import QtWidgets, QtCore
from package.biblioUI import Ui_form_biblio
from pathlib import Path
from package.chemin import data_base_biblio
import sqlite3
import os


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "PupilPremiumTable.db")

class App(QtWidgets.QWidget, Ui_form_biblio):
    def __init__(self):
        super().__init__()
        self.setupDB()
        self.setupUi(self)
        self.setWindowTitle("BiblioTeck")
        self.populate_livre()
        self.setup_connection()
        self.tabWidget.setCurrentIndex(0)

    def populate_livre(self):
        contenu = get_livre()
        for livre in contenu:
            lw_items = QtWidgets.QListWidgetItem(livre.title)
            lw_items.setData(QtCore.Qt.UserRole, livre)
            self.lw_listeLivre.addItem(lw_items)

    def setup_connection(self):
        self.btn_lire_info.clicked.connect(self.lire_livre)
        self.btn_enregistrer.clicked.connect(self.ajouterLivre)
        self.btn_effacer_livre.clicked.connect(self.retirerLivre)
        self.btn_annuler.clicked.connect(self.annuler)
        self.btn_modifier.clicked.connect(self.modifierLivre)
        self.btn_modifier_exec.clicked.connect(self.modifierFinal)
        self.btn_preter_livre.clicked.connect(self.preter)

    def ajouterLivre(self):
        if not self.le_titre_ajout.text():
            return False
        titre_ajout = self.le_titre_ajout.text()
        serie_ajout = self.le_serie_ajout.text()
        auteur_ajout = self.le_auteur_ajout.text()
        sinopsis_ajout = self.txt_sinopsis_ajout.toPlainText()
        pret_ajout = self.le_pret_ajout.text()
        new_livre = Livre(titre_ajout, serie_ajout, auteur_ajout, sinopsis_ajout, pret_ajout)
        resultat = new_livre.ajouter_livres()
        if resultat:
            lw_items = QtWidgets.QListWidgetItem(new_livre.title)
            lw_items.setData(QtCore.Qt.UserRole, new_livre)
            self.lw_listeLivre.addItem(lw_items)
        self.le_titre_ajout.setText("")
        self.le_serie_ajout.setText("")
        self.le_auteur_ajout.setText("")
        self.txt_sinopsis_ajout.setPlainText("")
        self.le_pret_ajout.setText("")
        self.tabWidget.setCurrentIndex(0)

    def annuler(self):
        self.le_titre_ajout.setText("")
        self.le_serie_ajout.setText("")
        self.le_auteur_ajout.setText("")
        self.txt_sinopsis_ajout.setPlainText("")
        self.le_pret_ajout.setText("")
        self.tabWidget.setCurrentIndex(0)

    def retirerLivre(self):
        for selected_item in self.lw_listeLivre.selectedItems():
            livre = selected_item.data(QtCore.Qt.UserRole)
            livre.effacer_livre()
            self.lw_listeLivre.takeItem(self.lw_listeLivre.row(selected_item))

    def lire_livre(self):
        for choix_livre in self.lw_listeLivre.selectedItems():
            livre = choix_livre.data(QtCore.Qt.UserRole)
            if not livre:
                return False
            self.tabWidget.setCurrentIndex(1)
            livre_entier = self.get_info_livre(livre)
            self.le_titre_info.setText(str(livre_entier[0]))
            self.le_serie_info.setText(str(livre_entier[1]))
            self.le_auteur_info.setText(str(livre_entier[2]))
            self.txt_sinopsis_info.setText(str(livre_entier[3]))
            self.le_pret_info.setText(str(livre_entier[4]))
            if self.le_pret_info.text():
                self.chk_pret_info.setChecked(True)
            else:
                self.chk_pret_info.setChecked(False)

    def get_info_livre(self, livre):
        conn = sqlite3.connect(data_base_biblio)
        c = conn.cursor()
        c.execute("select * from listing where titre=:titre;", {"titre": str(livre)})
        liste = c.fetchall()
        conn.commit()
        conn.close()
        contenu = list(sum(liste, ()))
        resultat = [Livre(contenu, "", "", "", "") for contenu in contenu]
        return resultat

    def modifierLivre(self):
        if not self.le_titre_info.text():
            return False
        self.tabWidget.setCurrentIndex(2)
        self.le_titre_ajout.setText(self.le_titre_info.text())
        self.le_serie_ajout.setText(self.le_serie_info.text())
        self.le_auteur_ajout.setText(self.le_auteur_info.text())
        self.txt_sinopsis_ajout.setPlainText(self.txt_sinopsis_info.toPlainText())
        self.le_pret_ajout.setText(self.le_pret_info.text())
        if self.le_pret_ajout.text():
            self.chk_pret_ajout.setChecked(True)
        else:
            self.chk_pret_ajout.setChecked(False)

    def modifierFinal(self):
        livre_a_modifier = self.le_titre_info.text()
        self.le_titre_info.setText("")
        self.le_serie_info.setText("")
        self.le_auteur_info.setText("")
        self.txt_sinopsis_info.setPlainText("")
        self.le_pret_info.setText("")
        titre_modif = self.le_titre_ajout.text()
        serie_modif = self.le_serie_ajout.text()
        auteur_modif = self.le_auteur_ajout.text()
        sinopsis_modif = self.txt_sinopsis_ajout.toPlainText()
        pret_modif = self.le_pret_ajout.text()
        modif_livre = Livre(titre_modif, serie_modif, auteur_modif, sinopsis_modif, pret_modif)
        resultat = modif_livre.modifier_livres(livre_a_modifier)
        if resultat:
            self.lw_listeLivre.clear()
            self.populate_livre()
            self.annuler()
        if self.le_pret_ajout.text():
            self.chk_pret_ajout.setChecked(True)
        else:
            self.chk_pret_ajout.setChecked(False)

    def preter(self):
        self.lire_livre()
        self.modifierLivre()
        self.chk_pret_ajout.setChecked(True)

    def setupDB(self):
        os.makedirs(os.path.join(Path.home(), ".biblioTeck"), exist_ok=True)
        connex = sqlite3.connect(data_base_biblio)
        c = connex.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS listing (titre text, serie text, auteur text, synopsis text, preteur text)")
        connex.commit()
        c.close()
        connex.close()
