from db import db

class Estudiante(db.Model):

    # Nombre de tabla

    __tablename__="estudiante"

    # Conjuntos de atributos (campos dela tabla)

    # Toda tabla deba tener ua llave primaria, valor único de ese campo

    # Llave primaria
    id=db.Column(db.Integer, primary_key=True)

    nombre=db.Column(db.String(50))
    email=db.Column(db.String(70))
    codigo=db.Column(db.String(15))

    # Metodo contructor para mapear datos a los campos definidos

    def __init__(self, nombre, email, codigo):

        self.nombre=nombre
        self.email=email
        self.codigo=codigo