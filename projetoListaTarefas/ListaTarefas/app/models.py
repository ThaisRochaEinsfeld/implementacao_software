from app import db

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"<Tarefa {self.descricao}>"
