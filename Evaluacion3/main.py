from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])


        if 10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70 and 0 <= asistencia <= 100:
            promedio = round((nota1 + nota2 + nota3) / 3, 0)


            if promedio >= 40 and asistencia >= 75:
                estado = 'Aprobado'
            else:
                estado = 'Reprobado'

            return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mas_largo = None
    cantidad_caracteres = 0

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        if len(nombre1) >= len(nombre2) and len(nombre1) >= len(nombre3):
            nombre_mas_largo = nombre1
            cantidad_caracteres = len(nombre1)
        elif len(nombre2) >= len(nombre1) and len(nombre2) >= len(nombre3):
            nombre_mas_largo = nombre2
            cantidad_caracteres = len(nombre2)
        else:
            nombre_mas_largo = nombre3
            cantidad_caracteres = len(nombre3)

    return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)

if __name__ == '__main__':
    app.run(debug=True)