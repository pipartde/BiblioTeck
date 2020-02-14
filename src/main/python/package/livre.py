import sqlite3
import logging
from package.chemin import data_base_biblio

def get_livre():
    conn = sqlite3.connect(data_base_biblio)
    c = conn.cursor()
    c.execute("select titre from listing order by titre asc;")
    liste = c.fetchall()
    conn.commit()
    conn.close()
    contenu = list(sum(liste, ()))
    resultat = [Livre(contenu, "", "", "", "") for contenu in contenu]
    return resultat


class Livre:
    def __init__(self, title, serie, auteur, sinopsis, pret):
        self.title = title.title()
        self.serie = serie.title()
        self.auteur = auteur.title()
        self.sinopsis = sinopsis.capitalize()
        self.pret = pret.title()

    def __str__(self):
        return self.title

    def _get_livres(self):
        conn = sqlite3.connect(data_base_biblio)
        c = conn.cursor()
        c.execute("select titre from listing order by titre asc;")
        liste = c.fetchall()
        conn.commit()
        c.close()
        conn.close()
        contenu = list(sum(liste, ()))
        return contenu

    def _write_livres(self, title, serie, auteur, sinopsis, pret):
        conn = sqlite3.connect(data_base_biblio)
        c = conn.cursor()
        liste = {"titre": title, "serie": serie, "auteur": auteur, "sinopsis": sinopsis, "pret": pret}
        c.execute("INSERT INTO listing values (:titre, :serie, :auteur, :sinopsis, :pret)", liste)
        conn.commit()
        conn.close()

    def _modif_livres(self, title, serie, auteur, sinopsis, pret, titreinit):
        conn = sqlite3.connect(data_base_biblio)
        c = conn.cursor()
        update = "UPDATE listing SET titre=?, serie= ?, auteur= ?, synopsis= ?, preteur= ? WHERE titre= ?"
        data = (str(title), str(serie), str(auteur), str(sinopsis), str(pret), str(titreinit))
        c.execute(update, data)
        conn.commit()
        c.close()
        conn.close()

    def ajouter_livres(self):
        livres = self._get_livres()
        if self.title not in livres:
            self._write_livres(self.title, self.serie, self.auteur, self.sinopsis, self.pret)
            return True
        else:
            logging.warning(f"Le livre {self.title} est déjà enregistré.")
            return False

    def effacer_livre(self):
        livres = self._get_livres()
        if self.title in livres:
            conn = sqlite3.connect(data_base_biblio)
            c = conn.cursor()
            c.execute("DELETE FROM listing WHERE titre = :a", {"a": self.title})
            conn.commit()
            conn.close()

    def modifier_livres(self, titreinitial):
        self._modif_livres(self.title, self.serie, self.auteur, self.sinopsis, self.pret, titreinitial)
        return True

    def get_titre(self, titre):
        conn = sqlite3.connect(data_base_biblio)
        c = conn.cursor()
        c.execute("select titre from listing where titre=(:titre);", {"titre": titre})
        title = c.fetchall()
        conn.commit()
        conn.close()
        contenu = list(sum(title, ()))
        resultat = [Livre(contenu, "", "", "", "") for contenu in contenu]
        return resultat


if __name__ == "__main__":
    pass
    # bouquin = Livre("le monde ne suffit pas", "james bond", "moi", "un histoire de gentil et de méchant", "personne")
    # print(bouquin)
