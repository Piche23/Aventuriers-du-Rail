from database.database import db

# Notez que tous les champs de mock-data ne sont pas pris en compte
class Joueur(db.Model):
    __tablename__ = "Joueur"
    jou_id = db.Column(db.Integer, primary_key=True)
    jou_nom = db.Column(db.Text, nullable=False)


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
    sco_plateau = db.Column(db.Integer, db.ForeignKey('Plateau.pla_id'))
    sco_joueur = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    sco_score = db.Column(db.Integer, nullable=False)
