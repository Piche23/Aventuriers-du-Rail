from database.database import db


# Notez que tous les champs de mock-data ne sont pas pris en compte
class Joueur(db.Model):
    __tablename__ = "Joueur"
    jou_id = db.Column(db.Integer, primary_key=True)
    jou_nom = db.Column(db.Text, nullable=False)

    def ajouter_joueur(nom: str):
        new_joueur = Joueur()
        new_joueur.jou_nom = nom
        db.session.add(new_joueur)
        db.session.commit()

    def get_joueur_par_nom(nom: str):
        return db.session.query(Joueur).filter(Joueur.jou_nom == nom).first()

    def get_by_id(id: int):
        return db.session.query(Joueur).filter(Joueur.jou_id == id).first()

    def get_all_joueur():
        return db.session.query(Joueur).all()

    def modifier_joueur(self, nom="null"):
        if nom != "null" and nom != '':
            self.jou_nom = nom


class Plateau(db.Model):
    __tablename__ = "Plateau"
    pla_id = db.Column(db.Integer, primary_key=True)
    pla_nom = db.Column(db.Text, nullable=False)


class Partie(db.Model):
    __tablename__ = "Partie"
    par_id = db.Column(db.Integer, primary_key=True)
    par_joueur1 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur2 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur3 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur4 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur5 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur6 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_score_joueur1 = db.Column(db.Integer, nullable=False)
    par_score_joueur2 = db.Column(db.Integer, nullable=False)
    par_score_joueur3 = db.Column(db.Integer, nullable=False)
    par_score_joueur4 = db.Column(db.Integer, nullable=False)
    par_score_joueur5 = db.Column(db.Integer, nullable=False)
    par_score_joueur6 = db.Column(db.Integer, nullable=False)
    par_date = db.Column(db.DateTime)


class Score(db.Model):
    __tablename__ = "Score"
    sco_id = db.Column(db.Integer, primary_key=True)
    sco_plateau = db.Column(db.Integer, db.ForeignKey('Plateau.pla_id'))
    sco_joueur = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    sco_score = db.Column(db.Integer, nullable=False)
