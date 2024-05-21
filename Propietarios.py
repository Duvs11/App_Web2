from db import db

class Propietario(db.Model):

    # Nombre de tabla

    __tablename__="Propietario"

    # Conjuntos de atributos (campos dela tabla)

    # Toda tabla deba tener ua llave primaria, valor único de ese campo

    # Llave primaria
    id=db.Column(db.Integer, primary_key=True)

    nombreP=db.Column(db.String(50))
    tipoPropiedad=db.Column(db.String(70))
    matriculaCatastral=db.Column(db.String(15))

    # Metodo contructor para mapear datos a los campos definidos

    def __init__(self, nombreP, tipoPropiedad, matriculaCatastral):

        self.nombreP=nombreP
        self.tipoPropiedad=tipoPropiedad
        self.matriculaCatastral=matriculaCatastral