from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/reserva.py', methods=['POST'])
def reserva():
    nombre = request.form['nombre']
    fecha = request.form['fecha']
    hora = request.form['hora']
    
    # Aquí puedes agregar la lógica para procesar la reserva
    
    return render_template('confirmacion.html', nombre=nombre, fecha=fecha, hora=hora)

if __name__ == '__main__':
    app.run()
