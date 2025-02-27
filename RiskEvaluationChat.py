from flask import Flask, render_template, request, jsonify
import rule_engine

app = Flask(__name__)

# Definir las reglas con sus respectivos puntajes
rules = [
    # Edad
    (rule_engine.Rule("edad < 30"), 4),
    (rule_engine.Rule("edad >= 30 and edad < 40"), 2),
    (rule_engine.Rule("edad >= 40 and edad <= 50"), -2),
    (rule_engine.Rule("edad > 50"), -6),

    # Estado de Salud
    (rule_engine.Rule("estado_salud == 'saludable'"), 4),
    (rule_engine.Rule("estado_salud == 'crónico'"), -7),

    # Historial Médico Familiar
    (rule_engine.Rule("historial_familiar == 'no'"), 3),
    (rule_engine.Rule("historial_familiar == 'sí'"), -5),

    # Estilo de Vida
    (rule_engine.Rule("estilo_vida == 'activo'"), 4),
    (rule_engine.Rule("estilo_vida == 'sedentario'"), -3),

    # Ocupación
    (rule_engine.Rule("ocupacion in ['bombero', 'minero', 'piloto']"), -6),
    (rule_engine.Rule("ocupacion not in ['bombero', 'minero', 'piloto']"), 3),

    # Hábitos
    (rule_engine.Rule("fumador == 'sí'"), -5),
    (rule_engine.Rule("fumador == 'no'"), 3),
    (rule_engine.Rule("alcohol_excesivo == 'sí'"), -5),
    (rule_engine.Rule("alcohol_excesivo == 'no'"), 3),

    # Historial de Seguro
    (rule_engine.Rule("historial_seguro == 'sin problemas'"), 3),
    (rule_engine.Rule("historial_seguro == 'reclamos frecuentes'"), -3),
]

def calcular_puntaje(cliente):
    puntaje_total = 0
    for rule, puntos in rules:
        if rule.matches(cliente):
            puntaje_total += puntos  
    return puntaje_total

def evaluar_riesgo(cliente):
    puntaje = calcular_puntaje(cliente)

    if puntaje >= 10:
        return "Bajo Riesgo"
    elif puntaje <= -10:
        return "Alto Riesgo"
    else:
        return "Riesgo Moderado"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    datos = request.json
    nombre = datos.get("nombre", "Usuario")
    nivel_riesgo = evaluar_riesgo(datos)
    return jsonify({"riesgo": nivel_riesgo, "nombre": nombre})

if __name__ == '__main__':
    app.run(debug=True)
