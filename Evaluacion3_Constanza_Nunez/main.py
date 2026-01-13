# Importamos Flask y las funciones necesarias
from flask import Flask, render_template, request

# Creamos la aplicación Flask
app = Flask(__name__)

# -------------------------------
# página principal: donde se muestra el menú con los dos botones
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# -------------------------------------------------------------------------
# Ejercicio 1:
# Formulario con 3 notas (10–70) y asistencia (0%–100%).
# Al enviar,  debe calcular el promedio y determinar si está aprobado o reprobado.
# Condiciones: promedio >= 40 y asistencia >= 75% (⌐■_■)
# ---------------------------------------------------------------------------
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        try:
            # Capturamos las notas y asistencia desde el formulario
            n1 = int(request.form['nota1'])
            n2 = int(request.form['nota2'])
            n3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            # Calculamos el promedio
            promedio = (n1 + n2 + n3) / 3

            # Evaluamos las condiciones de aprobación
            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

            # Resultado final que se mostrará en la página
            resultado = f"Promedio: {promedio:.2f}, Estado: {estado}"
        except ValueError:
            resultado = "Ingresa valores válidos."
    return render_template('ejercicio1.html', resultado=resultado)

# ---------------------------------------------------------------------------------------------------
# Ejercicio 2:
# Formulario con 3 nombres. ᓚᘏᗢ
# Al enviar, debe mostrar el nombre más largo y la cantidad de caracteres de dicho nombre.
# -----------------------------------------------------------------------------------------------------
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    if request.method == 'POST':
        # Capturamos los nombres desde el formulario
        nombre1 = request.form['nombre1'].strip()
        nombre2 = request.form['nombre2'].strip()
        nombre3 = request.form['nombre3'].strip()

        # Creamos la lista y buscamos el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        mayor = max(nombres, key=len)

        # Resultado final que se mostrará en la página
        resultado = f"El nombre más largo es '{mayor}' con {len(mayor)} caracteres."
    return render_template('ejercicio2.html', resultado=resultado)

# ------------------------------------------------------------------------------------
# Ejecutamos la aplicación en modo debug
# -------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
