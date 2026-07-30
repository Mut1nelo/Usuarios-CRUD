from flask import Flask, render_template, request, redirect
from usuario import Usuario

app = Flask(__name__)

@app.route('/')
def index():
    usuarios = Usuario.get_all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/crear_usuario', methods=['POST'])
def nuevo_usuario():
    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.save(datos)
    return redirect('/')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == "__main__":
    app.run(debug=True)