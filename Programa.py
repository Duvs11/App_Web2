from flask import Flask, render_template, request, redirect, url_for
from db import db
from Propietarios import Propietario

class Programa:
    
    def __init__(self):

        self.app=Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///propietarios.sqlite3"

        # agrega a DataBase
        db.init_app(self.app)

        self.app.add_url_rule('/', view_func=self.nuevoRegistro)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET", "POST"])
        
        # Iniciar el servidor
        
        with self.app.app_context():
            db.create_all()
            self.app.run(debug=True)

    def nuevoRegistro(self):
        return render_template('mostrarTodos.html', propietarios=Propietario.query.all())
    
    def agregar(self):
        # return "Hola Mundo Flask"
        
        # Verificar si debe envíar el formulario o procesar los datos
        if request.method=="POST":

            # Crear un objeto de la clase Estudiante con los valores del fórmulario
            nombreP=request.form['nombreP']
            tipoPropiedad=request.form['tipoPropiedad']
            matriculaCatastral=request.form['matriculaCatastral']

            miPropietario=Propietario(nombreP, tipoPropiedad, matriculaCatastral)
                                    
            # Guardar el obeto en la báse de datos

            db.session.add(miPropietario)
            db.session.commit()
            
            return redirect(url_for('nuevoRegistro'))

        return render_template('nuevoRegistro.html')
    
miPrograma = Programa()