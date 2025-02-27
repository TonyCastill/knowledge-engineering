from flask import Flask, render_template, request, jsonify
import rule_engine

app = Flask(__name__)

# Definir las reglas con sus respectivos puntajes
# 5 o mayor es de bajo riesgo
# -5 o menor es alto riesgo 
# Entre rango es riesgo moderado

# 10 o mayor es bajo riesgo
# entre 9 y -9 riesgo moderado
# -10 o menor es alto riesgo
rules = [
    # Edad
    (rule_engine.Rule("edad < 20"), 6),
    (rule_engine.Rule("edad >= 20 and edad <= 30"), 3),
    (rule_engine.Rule("edad >= 31 and edad <= 40"), 0),
    (rule_engine.Rule("edad >= 41 and edad <= 50"), -2),
    (rule_engine.Rule("edad > 50"), -8),

    # Estado de Salud
    (rule_engine.Rule("estado_salud == 'saludable'"), 3),
    (rule_engine.Rule("estado_salud == 'obesidad'"), 4),
    (rule_engine.Rule("estado_salud == 'crónico'"), -6),

    # Historial Médico Familiar
    (rule_engine.Rule("historial_familiar == 'no'"), 2),
    (rule_engine.Rule("historial_familiar == 'sí'"), -4),

    # Estilo de Vida
    (rule_engine.Rule("estilo_vida == 'activo'"), 3),
    (rule_engine.Rule("estilo_vida == 'sedentario'"), -3),

    # Ocupación
    (rule_engine.Rule("ocupacion in ['bombero', 'minero', 'piloto']"), -5),
    (rule_engine.Rule("ocupacion not in ['bombero', 'minero', 'piloto']"), 3),

    # Hábitos
    (rule_engine.Rule("fumador == 'sí'"), -5),
    (rule_engine.Rule("fumador == 'no'"), 2),
    (rule_engine.Rule("alcohol_excesivo == 'sí'"), -3),
    (rule_engine.Rule("alcohol_excesivo == 'no'"), 2),

    # Historial de Seguro
    (rule_engine.Rule("historial_seguro == 'sin problemas'"), 2),
    (rule_engine.Rule("historial_seguro == 'reclamos frecuentes'"), -4),
]

def calcular_puntaje(cliente):
    puntaje_total = 0
    for rule, puntos in rules:
        if rule.matches(cliente):
            print(rule,": ",puntos)
            puntaje_total += puntos  # Ahora usamos una tupla y sumamos el valor directamente
    return puntaje_total

def evaluar_riesgo(cliente):
    puntaje = calcular_puntaje(cliente)

    if puntaje >= 10:
        return "Bajo Riesgo"#,puntaje
    elif puntaje <= -10:
        return "Alto Riesgo"#,puntaje
    else:
        return "Riesgo Moderado"#,puntaje

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
