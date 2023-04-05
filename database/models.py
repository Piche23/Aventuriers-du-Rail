from datetime import datetime

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

    def ajouter_plateau(nom: str):
        new_plateau = Plateau()
        new_plateau.pla_nom = nom
        db.session.add(new_plateau)
        db.session.commit()

    def get_plateau_par_nom(nom: str):
        return db.session.query(Plateau).filter(Plateau.pla_nom == nom).first()

    def get_by_id(id: int):
        return db.session.query(Plateau).filter(Plateau.pla_id == id).first()

    def get_all_plateau():
        return db.session.query(Plateau).all()

    def modifier_plateau(self, nom="null"):
        if nom != "null" and nom != '':
            self.pla_nom = nom


class Partie(db.Model):
    __tablename__ = "Partie"
    par_id = db.Column(db.Integer, primary_key=True)
    par_plateau = db.Column(db.Integer, db.ForeignKey('Plateau.pla_id'))
    par_joueur1 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur2 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur3 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur4 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur5 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_joueur6 = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    par_score_joueur1 = db.Column(db.Integer, nullable=False)
    par_score_joueur2 = db.Column(db.Integer, nullable=False)
    par_score_joueur3 = db.Column(db.Integer)
    par_score_joueur4 = db.Column(db.Integer)
    par_score_joueur5 = db.Column(db.Integer)
    par_score_joueur6 = db.Column(db.Integer)
    par_date = db.Column(db.DateTime)

    def ajouter_partie(plateau, joueur1, joueur2, joueur3, joueur4, joueur5, joueur6,
                       score_joueur1, score_joueur2, score_joueur3, score_joueur4,
                       score_joueur5, score_joueur6, date):
        Date = datetime.strptime(date, '%Y-%m-%d')
        new_partie = Partie(par_plateau=plateau, par_joueur1=joueur1, par_joueur2=joueur2,
                            par_joueur3=joueur3, par_joueur4=joueur4, par_joueur5=joueur5,
                            par_joueur6=joueur6, par_score_joueur1=score_joueur1,
                            par_score_joueur2=score_joueur2, par_score_joueur3=score_joueur3,
                            par_score_joueur4=score_joueur4, par_score_joueur5=score_joueur5,
                            par_score_joueur6=score_joueur6, par_date=Date)
        db.session.add(new_partie)
        db.session.commit()

    def get_by_id(id: int):
        return db.session.query(Partie).filter(Partie.par_id == id).first()

    def get_all_partie():
        return db.session.query(Partie).all()

    def modifier_partie(self, plateau, joueur1, joueur2, score_joueur1, score_joueur2, date,
                        joueur3, joueur4, joueur5, joueur6, score_joueur3, score_joueur4,
                        score_joueur5, score_joueur6):
        if plateau != "null" and plateau != '':
            self.par_plateau = plateau
        if joueur1 != "null" and joueur1 != '':
            self.par_joueur1 = joueur1
        if joueur2 != "null" and joueur2 != '':
            self.par_joueur2 = joueur2
        self.par_joueur3 = joueur3
        self.par_joueur4 = joueur4
        self.par_joueur5 = joueur5
        self.par_joueur6 = joueur6
        if score_joueur1 != "null" and score_joueur1 != '':
            self.par_score_joueur1 = score_joueur1
        if score_joueur2 != "null" and score_joueur2 != '':
            self.par_score_joueur2 = score_joueur2
        self.par_score_joueur3 = score_joueur3
        self.par_score_joueur4 = score_joueur4
        self.par_score_joueur5 = score_joueur5
        self.par_score_joueur6 = score_joueur6
        if date != "null" and date != '':
            Date = datetime.strptime(date, '%Y-%m-%d')
            self.par_date = Date


class Score(db.Model):
    __tablename__ = "Score"
    sco_id = db.Column(db.Integer, primary_key=True)
    sco_plateau = db.Column(db.Integer, db.ForeignKey('Plateau.pla_id'))
    sco_joueur = db.Column(db.Integer, db.ForeignKey('Joueur.jou_id'))
    sco_score = db.Column(db.Integer, nullable=False)

    def ajouter_score(plateau, joueur, score):
        new_score = Score(par_plateau=plateau, sco_joueur=joueur, sco_score=score)
        db.session.add(new_score)
        db.session.commit()

    def get_by_id(id: int):
        return db.session.query(Score).filter(Score.sco_id == id).first()

    def get_all_score():
        return db.session.query(Score).all()

    def modifier_score(self, plateau, joueur, score):
        if plateau != "null" and plateau != '':
            self.sco_plateau = plateau
        if joueur != "null" and joueur != '':
            self.sco_joueur = joueur
        if score != "null" and score != '':
            self.sco_score = score
