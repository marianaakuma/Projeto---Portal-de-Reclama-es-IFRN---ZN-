from utils import db

class login(db.Model):
    __tablename__= "login"
    id = db.Column(db.Integer, primary_key = True)
    usuario  = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, usuario,senha):
        self.usuario = usuario
        self.senha = senha
    
    def __repr__(self):
        return "<login {}>".format(self.usuario)